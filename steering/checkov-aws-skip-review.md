# IaC Checkov AWS — Skip Review

Steering file cho review logic và phát hiện outdated `#checkov:skip=` suppressions trong codebase.

## Khi nào load file này

- User nói: "review skip", "review suppression", "review logic skip", "kiểm tra skip"
- User nói: "check outdated skip", "review outdate", "skip nào hết hạn"
- User nói: "audit suppressions", "suppression quality"
- Sau khi scan xong, user muốn đánh giá skip hiện có trong code

---

## Command: `review-skip`

### Workflow

```
scan source → parse skip comments → cross-ref scan results → evaluate → report
```

### Step 1: Scan Source Code

```bash
grep -rn "checkov:skip" {target_dir} --include="*.tf" --include="*.yaml" --include="*.yml" \
  --exclude-dir=".terraform" --exclude-dir="vendor" --exclude-dir="node_modules"
```

Output mỗi match:
```
{file}:{line}: # checkov:skip={CHECK_ID}:{justification}
```

### Step 2: Parse Skip Comments

Extract structured data từ mỗi skip:

| Field | Source | Required |
|-------|--------|----------|
| file | grep output | ✅ |
| line | grep output | ✅ |
| check_id | after `checkov:skip=` before `:` | ✅ |
| justification | after second `:` | ✅ (empty = violation) |
| ticket | regex `[A-Z]+-\d+` trong justification | Optional |
| expires | regex `EXPIRES?:\s*\d{4}-\d{2}-\d{2}` trong nearby lines (±3) | Optional |
| approved_by | regex `Approved by:` trong nearby lines (±3) | Optional |
| compensating_controls | "Compensating controls:" section below skip | Optional |

### Step 3: Cross-Reference với Scan Results

Cho mỗi skip found:
1. Check nếu `check_id` có trong latest scan `results.json` → `skipped_checks[]`
2. Check nếu resource vẫn tồn tại (file + line still valid)
3. Check nếu check_id vẫn còn relevant (Checkov version compatibility)

### Step 4: Evaluate — Logic Review

Đánh giá mỗi suppression theo 4 tiêu chí:

#### Tiêu chí 1: Justification Quality

| Score | Criteria | Example |
|-------|----------|---------|
| ✅ STRONG | Business reason + compensating controls | "Public ALB by design. WAF + CloudFront restrict direct access." |
| ⚠️ ACCEPTABLE | Business reason only, no controls | "Dev environment — no sensitive data" |
| ❌ WEAK | Vague or no justification | "Not needed" / "Too expensive" / empty |
| 🚫 MISSING | No text after `:` | `# checkov:skip=CKV_AWS_18` |

#### Tiêu chí 2: Severity vs Justification Strength

| Check Severity | Minimum Justification Required |
|----------------|-------------------------------|
| CRITICAL | STRONG + ticket + approval + compensating controls |
| HIGH | STRONG + ticket OR compensating controls |
| MEDIUM | ACCEPTABLE hoặc tốt hơn |
| LOW | Any non-empty justification |

**Violation**: Suppress CRITICAL/HIGH check với justification WEAK/MISSING → flag immediately.

#### Tiêu chí 3: Known False Positive Patterns

Auto-approve (✅ VALID) nếu match pattern:

| Pattern | Check IDs | Condition |
|---------|-----------|-----------|
| GWLB + HTTPS check | CKV_AWS_2 | Resource type = `aws_lb_listener` + LB type = `gateway` |
| Module SG not attached | CKV2_AWS_5 | File trong `_modules/` hoặc `modules/` directory |
| EIP for NAT/DX | CKV2_AWS_19 | Resource name contains `nat` hoặc `dx` hoặc `direct_connect` |
| Lambda monitoring no VPC | CKV_AWS_117 | Lambda name contains `monitor`, `notif`, `alarm`, `log` AND no `vpc_config` block needed (calls AWS APIs only, no private resources) |
| Public ALB ingress | CKV_AWS_260 | Resource name contains `alb` hoặc `lb` + purpose is internet-facing |
| ALB egress to targets | CKV_AWS_382 | Resource associated with ALB/NLB |

Khi match → báo "✅ Known false positive — skip valid" NHƯNG vẫn kiểm tra justification text tồn tại.

#### Tiêu chí 4: Expiration Check

| Status | Condition |
|--------|-----------|
| 🟢 ACTIVE | No expiry set OR expiry > today |
| 🟡 EXPIRING SOON | Expiry within 30 days |
| 🔴 EXPIRED | Expiry date < today |
| ⚪ NO EXPIRY | Permanent skip — flag nếu severity >= HIGH |

---

## Command: `review-outdate`

### Workflow

```
parse skips → check expiration → check resource existence → check check validity → report
```

### Outdated Detection Rules

Một suppression là **OUTDATED** khi:

#### Rule 1: Expired Date
```hcl
# checkov:skip=CKV_AWS_8:Temporary instance for POC
# EXPIRES: 2024-03-31   ← ĐÃ QUA
```
→ 🔴 EXPIRED — cần remove skip và apply fix, hoặc renew với justification mới.

#### Rule 2: Resource Removed/Changed
Skip comment tồn tại nhưng:
- File không còn tồn tại
- Resource block đã bị xóa
- Resource đã được refactor (tên thay đổi)

→ 🔴 ORPHANED — dead code, cần cleanup.

#### Rule 3: Check Deprecated
Check ID không còn trong Checkov version hiện tại:
```bash
checkov --list --framework terraform 2>/dev/null | grep {CHECK_ID}
```
Nếu không tìm thấy → 🟡 DEPRECATED — skip vô nghĩa, có thể remove.

#### Rule 4: Compensating Control No Longer Active
Skip reference tới compensating control (WAF, CloudFront, VPN) nhưng:
- Control đã bị remove trong cùng repo
- Control reference outdated (stale reference)

→ ⚠️ STALE JUSTIFICATION — cần re-evaluate.

#### Rule 5: Environment Drift
Skip nói "dev environment" hoặc "non-production" nhưng:
- File path hoặc resource tags gợi ý production
- Variable/workspace name = `prod`

→ 🔴 ENVIRONMENT MISMATCH — high risk, immediate review.

#### Rule 6: Ticket Closed Without Resolution
Skip có ticket reference nhưng ticket đã closed:
- Không auto-check (cần manual verify)
- Flag: "⚠️ Verify ticket {TICKET-ID} status — is the temporary exception still valid?"

---

## Output Format

### Review Skip Report

```markdown
# 🔍 Skip Review Report — {date}

## Summary
| Metric | Count |
|--------|-------|
| Total Skips Found | {N} |
| ✅ Valid | {N} |
| ⚠️ Needs Attention | {N} |
| ❌ Invalid | {N} |
| 🔴 Outdated | {N} |

## Findings

### ❌ Invalid Suppressions (Immediate Action Required)

| # | File:Line | Check ID | Issue | Recommendation |
|---|-----------|----------|-------|----------------|
| 1 | `main.tf:42` | CKV_AWS_23 | No justification | Add business reason or remove skip |
| 2 | `rds.tf:15` | CKV_AWS_96 | CRITICAL check suppressed with weak reason | Requires security team approval |

### 🔴 Outdated Suppressions (Cleanup Required)

| # | File:Line | Check ID | Reason Outdated | Action |
|---|-----------|----------|-----------------|--------|
| 1 | `ec2.tf:30` | CKV_AWS_8 | EXPIRED: 2024-03-31 | Remove skip + encrypt EBS |
| 2 | `old-sg.tf:5` | CKV_AWS_23 | Resource removed | Delete skip comment |

### ⚠️ Needs Attention (Team Review)

| # | File:Line | Check ID | Issue | Question |
|---|-----------|----------|-------|----------|
| 1 | `kms.tf:22` | CKV_AWS_111 | HIGH severity, no compensating controls | Can KMS policy be scoped down? |

### ✅ Valid Suppressions

| # | File:Line | Check ID | Category | Justification (summary) |
|---|-----------|----------|----------|------------------------|
| 1 | `gwlb.tf:64` | CKV_AWS_2 | False Positive | GWLB uses GENEVE, not HTTP |
| 2 | `alb.tf:79` | CKV_AWS_260 | By Design | Public ALB + WAF |
```

### Review Outdate Report

```markdown
# ⏰ Outdated Skip Report — {date}

## Summary
| Status | Count |
|--------|-------|
| 🔴 Expired | {N} |
| 🔴 Orphaned | {N} |
| 🟡 Deprecated Check | {N} |
| ⚠️ Stale Justification | {N} |
| 🔴 Environment Mismatch | {N} |
| ⚠️ Ticket Unverified | {N} |
| 🟢 Current | {N} |

## Expired Suppressions

| # | File:Line | Check ID | Expired Date | Days Overdue | Action |
|---|-----------|----------|--------------|--------------|--------|
| 1 | ... | ... | 2024-03-31 | 425 days | Fix or renew |

## Orphaned Suppressions (Dead Code)

| # | Original File | Check ID | Reason |
|---|---------------|----------|--------|
| 1 | `removed-module/main.tf:15` | CKV_AWS_18 | File no longer exists |

## Recommendations
1. Remove {N} expired skips and apply fixes
2. Clean up {N} orphaned skip comments
3. Re-evaluate {N} skips with stale justifications
4. Verify {N} ticket references with team
```

---

## Integration với Existing Workflow

### Khi nào tự động trigger review

1. **Sau mỗi scan** (analyze phase): Đếm skipped checks từ results.json → nếu >0 hiển thị summary
2. **Khi user yêu cầu suppress** (`suppress` command): Validate justification trước khi apply
3. **Session start** (resume): Check nếu có expired skips trong project-memory

### Update Project Memory

Sau review, append kết quả vào `state/project-memory.md`:

```markdown
## Skip Review History
| Date | Total Skips | Valid | Invalid | Outdated | Action Taken |
|------|-------------|-------|---------|----------|--------------|
| 2026-05-28 | 15 | 10 | 2 | 3 | Fixed 2 invalid, cleaned 3 orphaned |
```

### Update Tech Debt

Nếu review tìm invalid/outdated skips → update `scans/{NNN}/tech-debt.md`:
- Move từ "Accepted Debt" → "Needs Review" nếu justification yếu
- Move từ "Suppression Candidates" → "Accepted Debt" nếu verified valid

---

## Suppress Command Enhancement

Khi user dùng `suppress {CHECK_ID}` command, PHẢI enforce:

### Mandatory Fields
```hcl
resource "aws_example" "this" {
  # checkov:skip={CHECK_ID}:{JUSTIFICATION - minimum 10 chars}
  ...
}
```

### Recommended Fields (prompt user)
```hcl
resource "aws_example" "this" {
  # checkov:skip={CHECK_ID}:{JUSTIFICATION}
  # Ticket: {TICKET-ID}
  # Approved by: {approver}
  # Expires: {YYYY-MM-DD} (nếu temporary)
  # Compensating controls:
  # - {control 1}
  # - {control 2}
  ...
}
```

### Validation Before Apply

| Check Severity | Requirements |
|----------------|-------------|
| CRITICAL | ❌ KHÔNG suppress — phải fix. Ngoại lệ: user explicitly override với "force suppress" |
| HIGH | Justification ≥ STRONG + prompt for ticket + compensating controls |
| MEDIUM | Justification ≥ ACCEPTABLE |
| LOW | Any non-empty justification |

Nếu user cố suppress CRITICAL check:
```
⚠️ CKV_AWS_274 (AdministratorAccess policy) là CRITICAL finding.
Suppress CRITICAL checks KHÔNG được khuyến nghị — nên fix thay vì skip.

Nếu THỰC SỰ cần suppress, cung cấp:
1. Business justification (tại sao không thể fix?)
2. Compensating controls (giảm thiểu risk thế nào?)
3. Ticket reference (ai approve?)
4. Expiration date (khi nào sẽ fix?)

Tiếp tục force suppress? [y/N]
```

---

## Quarterly Review Reminder

Khi session start, check `state/project-memory.md` → nếu last skip review > 90 days:

```
📋 Reminder: Last skip review was {N} days ago.
Recommended: chạy `review-skip` để audit suppressions.
Potential issues: expired dates, stale justifications, deprecated checks.
```

---

## Anti-Patterns (KHÔNG BAO GIỜ accept)

| Pattern | Why Bad | Action |
|---------|---------|--------|
| `# checkov:skip=*` | Blanket suppress ALL checks | ❌ Reject — never valid |
| Skip without colon text | No justification | ❌ Flag as MISSING |
| "Too expensive" as justification for prod | Cost ≠ security justification | ❌ Flag as WEAK |
| "Not needed" without explanation | Vague, no business context | ❌ Flag as WEAK |
| Skip CRITICAL in production path | Highest risk | ❌ Flag — require force + full documentation |
| Same skip copy-pasted 10+ times | Probably should be in .checkov.yaml skip-check | ⚠️ Suggest centralized suppression |
| Skip with expired date still active | Maintenance debt | 🔴 Flag as OUTDATED |
