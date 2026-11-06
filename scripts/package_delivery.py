#!/usr/bin/env python3
"""I package my tracked repository, history and checksums for an offline handoff."""

import hashlib
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / 'outputs'


def main():
    if subprocess.run(['git', 'status', '--porcelain'], cwd=ROOT, capture_output=True, check=True).stdout:
        raise SystemExit('I require a clean committed repository before packaging.')
    subprocess.run([str(ROOT / 'scripts/verify_repo.sh')], cwd=ROOT, check=True)
    OUTPUTS.mkdir(exist_ok=True)
    bundle = OUTPUTS / 'ADA-08-history.bundle'
    if bundle.exists():
        bundle.unlink()
    subprocess.run(['git', 'bundle', 'create', str(bundle), '--all'], cwd=ROOT, check=True)
    subprocess.run(['git', 'bundle', 'verify', str(bundle)], cwd=ROOT, check=True)
    listing = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT, capture_output=True, check=True).stdout
    paths = [Path(p.decode()) for p in listing.split(b'\0') if p]
    archive = OUTPUTS / 'ADA-08-AgentReady-Repository.zip'
    hashes = []
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as target:
        for rel in sorted(paths):
            path = ROOT / rel
            if path.is_symlink() or not path.is_file():
                raise SystemExit(f'I reject non-regular tracked delivery path: {rel}')
            info = zipfile.ZipInfo('ada-08-agent-ready-repository/' + rel.as_posix(), (2026, 11, 5, 0, 0, 0))
            info.external_attr = (0o100755 if path.stat().st_mode & 0o111 else 0o100644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            data = path.read_bytes()
            target.writestr(info, data)
            hashes.append(f'{hashlib.sha256(data).hexdigest()}  {rel.as_posix()}')
    with zipfile.ZipFile(archive) as check:
        if check.testzip() is not None:
            raise SystemExit('I detected a corrupt ZIP member.')
    (OUTPUTS / 'ADA-08-FILES-SHA256.txt').write_text('\n'.join(hashes) + '\n')
    summary = [archive, bundle, OUTPUTS / 'ADA-08-FILES-SHA256.txt']
    (OUTPUTS / 'ADA-08-SHA256SUMS.txt').write_text('\n'.join(
        f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}' for p in summary
    ) + '\n')
    print(f'I packaged {len(paths)} source files and all Git refs.')


if __name__ == '__main__':
    main()
