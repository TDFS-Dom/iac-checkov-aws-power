# IaC Checkov AWS — Token Budget

Guardrail cho context window. Kiểm soát steering file loading.

## Nguyên tắc

- Chỉ load steering files cần thiết cho command hiện tại
- Never load all steering files cùng lúc
- Always-loaded files phải nhỏ (<4KB mỗi file)
- On-demand files load 1-2 tại 1 thời điểm

## Always-Loaded (mỗi interaction)

| File | Est. size | Mục đích |
|---|---|---|
| `secops-contract.md` | ~4KB | Paths, prerequisites, behavior rules |
| `secops-routing.md` | ~3KB | NLP intent → command dispatch |

**Total always-loaded: ~7KB**

## On-Demand Load Bundles

| Command | Load files | Est. size |
|---|---|---|
| plan / scan | secops-contract + checkov-aws-scan | ~12KB |
| analyze | secops-contract (sufficient) | ~4KB |
| fix | secops-contract + checkov-aws-scan (Phase 5) | ~12KB |
| compliance | secops-contract + checkov-aws-compliance | ~10KB |
| report | secops-contract + checkov-aws-compliance | ~10KB |
| baseline | secops-contract + checkov-aws-scan | ~12KB |
| next / status | secops-contract (sufficient) | ~4KB |
| custom-policy | secops-contract + checkov-aws-compliance | ~10KB |
| suppress | secops-contract (sufficient) | ~4KB |
| export-docx | secops-contract + docx-export | ~10KB |

## Khi budget tight

1. Không load checkov-aws-compliance nếu command là plan/scan/fix
2. Không load checkov-aws-scan nếu command là compliance/report
3. Dùng secops-contract summary cho next/status (không cần file khác)
4. Compliance mapping chỉ load khi user hỏi CIS/PCI/HIPAA/SOC2 cụ thể
