#!/usr/bin/env python3
"""Validate all written episodes and the fully illustrated episode packages."""
from pathlib import Path
import argparse
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.episode_package import validate_links

# The remaining folders contain 80-shot written drafts, but not 20 storyboard PNGs yet.
FULLY_ILLUSTRATED = frozenset({1, 2, 3, 4, 6})
PENDING_ARTWORK = frozenset(range(1, 11)) - FULLY_ILLUSTRATED


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--written-only', action='store_true',
                        help='Skip artwork for continuation episodes')
    args = parser.parse_args()
    for number in range(1, 11):
        episode = f'Episode_{number:02}'
        command = [sys.executable, f'{episode}/check.py']
        if number >= 4 and (args.written_only or number in PENDING_ARTWORK):
            command.append('--written-only')
        commands = [command]
        if number >= 2:
            commands.append([sys.executable, f'{episode}/sync.py', '--check'])
        for item in commands:
            result = subprocess.run(item, cwd=ROOT)
            if result.returncode:
                return result.returncode
    if args.written_only:
        print('PASS: all ten written episode packages; continuation visuals not checked')
    else:
        links = sum(validate_links(ROOT / f'Episode_{n:02}') for n in sorted(FULLY_ILLUSTRATED))
        complete = ', '.join(f'{n:02}' for n in sorted(FULLY_ILLUSTRATED))
        partial = ', '.join(f'{n:02}' for n in sorted(PENDING_ARTWORK))
        print(f'PASS: scripts and handoffs for all ten; full artwork for {complete} '
              f'({links} verified local links); episodes {partial} have partial '
              'storyboards and have NOT passed complete artwork checks')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
