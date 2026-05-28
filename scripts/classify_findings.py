#!/usr/bin/env python3
"""
Classify Checkov findings by severity using severity-map.md as source of truth.

Usage:
    python3 scripts/classify_findings.py <results.json>

Output:
    Prints JSON to stdout with findings grouped by severity (CRITICAL/HIGH/MEDIUM/LOW).
    Agent uses this output directly — does NOT self-classify.

Example:
    python3 scripts/classify_findings.py .checkov-reports/scans/001/results.json
"""

import json
import sys
import os
import re

def load_severity_map(script_dir):
    """Load severity-map.md and build Check ID → Severity dict."""
    map_path = os.path.join(script_dir, '..', 'references', 'severity-map.md')
    if not os.path.exists(map_path):
        print(f"ERROR: severity-map.md not found at {map_path}", file=sys.stderr)
        sys.exit(1)

    severity_map = {}
    current_severity = None

    with open(map_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('## CRITICAL'):
                current_severity = 'CRITICAL'
            elif line.startswith('## HIGH'):
                current_severity = 'HIGH'
            elif line.startswith('## MEDIUM'):
                current_severity = 'MEDIUM'
            elif line.startswith('## LOW'):
                current_severity = 'LOW'
            elif current_severity and 'CKV' in line:
                check_ids = re.findall(r'CKV2?_AWS_\d+', line)
                for cid in check_ids:
                    severity_map[cid] = current_severity

    return severity_map


def classify_findings(results_path, severity_map):
    """Parse results.json and classify each finding."""
    with open(results_path, 'r') as f:
        data = json.load(f)

    failed_checks = data.get('results', {}).get('failed_checks', [])
    skipped_checks = data.get('results', {}).get('skipped_checks', [])
    summary = data.get('summary', {})

    classified = {
        'CRITICAL': [],
        'HIGH': [],
        'MEDIUM': [],
        'LOW': [],
    }

    for finding in failed_checks:
        check_id = finding.get('check_id', '')
        severity = severity_map.get(check_id, 'MEDIUM')  # default MEDIUM if unknown

        classified[severity].append({
            'check_id': check_id,
            'check_name': finding.get('check_name', ''),
            'resource': finding.get('resource', ''),
            'file_path': finding.get('file_path', ''),
            'file_line_range': finding.get('file_line_range', []),
            'severity': severity,
            'guideline': finding.get('guideline', ''),
        })

    output = {
        'scan_summary': {
            'passed': summary.get('passed', 0),
            'failed': summary.get('failed', 0),
            'skipped': summary.get('skipped', 0),
            'resource_count': summary.get('resource_count', 0),
        },
        'severity_counts': {
            'CRITICAL': len(classified['CRITICAL']),
            'HIGH': len(classified['HIGH']),
            'MEDIUM': len(classified['MEDIUM']),
            'LOW': len(classified['LOW']),
        },
        'findings_by_severity': classified,
        'skipped_checks': [{
            'check_id': s.get('check_id', ''),
            'resource': s.get('resource', ''),
            'file_path': s.get('file_path', ''),
            'suppress_comment': s.get('suppress_comment', ''),
        } for s in skipped_checks],
    }

    return output


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/classify_findings.py <results.json>", file=sys.stderr)
        sys.exit(1)

    results_path = sys.argv[1]
    if not os.path.exists(results_path):
        print(f"ERROR: {results_path} not found", file=sys.stderr)
        sys.exit(1)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    severity_map = load_severity_map(script_dir)
    output = classify_findings(results_path, severity_map)

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
