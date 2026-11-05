"""Validate report format, not engineering correctness. Standard library only.
Usage: python validate_review_report.py REPORT
Exit codes: 0 valid, 1 invalid/unreadable, 2 incorrect invocation.
"""
import re
import sys
from pathlib import Path

SECTIONS = ('Review Context', 'Requirements / Acceptance Criteria Reviewed', 'Test Evidence',
            'MUST FIX', 'SHOULD FIX', 'OPTIONAL', 'Open Questions', 'Final Review Summary')
FIELDS = ('Requirement / AC', 'File', 'Evidence', 'Problem', 'Recommended next step')


def visible_markdown(text):
    """Ignore comments and fenced examples, including unclosed fences."""
    text = re.sub(r'<!--.*?(?:-->|\Z)', '', text, flags=re.S)
    lines, fence, width = [], None, 0
    for line in text.splitlines():
        match = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if fence is None:
            if match:
                fence, width = match[1][0], len(match[1])
            else:
                lines.append(line)
        elif match and match[1][0] == fence and len(match[1]) >= width and not match[2].strip():
            fence = None
    return '\n'.join(lines)


def validate(text):
    text = visible_markdown(text)
    errors = []
    headings = list(re.finditer(r'^## ([^\n]+)[^\S\n]*$', text, re.M))
    names = [m[1].strip() for m in headings]
    if names != list(SECTIONS):
        return ['Required level-2 sections must appear exactly once and in template order.']
    bodies = {name: text[headings[i].end():headings[i + 1].start() if i + 1 < len(headings) else len(text)].strip()
              for i, name in enumerate(names)}
    for name, body in bodies.items():
        if not body:
            errors.append(f'Empty section: {name}')
    if re.search(r'\{[^{}\n]+\}', text):
        errors.append('Unresolved template placeholders.')
    context = bodies['Review Context']
    for field in ('PR / Branch', 'Reviewer Agent', 'Date', 'Base / Head', 'Authority'):
        if not re.search(r'^' + re.escape(field) + r':[^\S\n]*\S[^\n]*$', context, re.M):
            errors.append(f'Missing context field: {field}')
    summary = bodies['Final Review Summary']
    if len(re.findall(r'^Human decision required:[^\S\n]*YES[^\S\n]*$', summary, re.M)) != 1:
        errors.append('Human decision required must be YES in Final Review Summary.')
    ids = []
    for severity in ('MUST FIX', 'SHOULD FIX', 'OPTIONAL'):
        body = bodies[severity]
        findings = list(re.finditer(r'^### (RF-\d{2,})[^\S\n]*$', body, re.M))
        count = re.findall(r'^' + re.escape(severity) + r' count: (\d+)[^\S\n]*$', summary, re.M)
        if len(count) != 1 or int(count[0]) != len(findings):
            errors.append(f'Incorrect or missing count for {severity}.')
        if not findings and body != 'None.':
            errors.append(f'Empty finding category {severity} must say None.')
        if findings and body[:findings[0].start()].strip():
            errors.append(f'Unstructured findings in {severity}.')
        for i, finding in enumerate(findings):
            ids.append(finding[1])
            block = body[finding.end():findings[i + 1].start() if i + 1 < len(findings) else len(body)]
            for field in FIELDS:
                values = re.findall(r'^' + re.escape(field) + r':[^\S\n]*(\S[^\n]*)$', block, re.M)
                if len(values) != 1 or values[0].strip() in ('...', 'TBD', 'TODO'):
                    errors.append(f'{finding[1]}: missing/invalid {field}.')
    if len(ids) != len(set(ids)):
        errors.append('Finding IDs must be unique across all categories.')
    return errors


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print('Usage: validate_review_report.py REPORT', file=sys.stderr)
        return 2
    try:
        text = Path(argv[0]).read_text(encoding='utf-8')
    except (OSError, UnicodeError) as exc:
        print(f'INVALID: cannot read report: {exc}', file=sys.stderr)
        return 1
    errors = validate(text)
    if errors:
        print('INVALID: ' + '\nINVALID: '.join(errors), file=sys.stderr)
        return 1
    print('VALID: PR readiness review structure is complete.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
