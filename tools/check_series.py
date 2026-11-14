#!/usr/bin/env python3
"""Run the actual source, freshness and local-link checks for all ten episodes."""
from pathlib import Path
import argparse
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.episode_package import validate_links


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--written-only', action='store_true',
                        help='Check continuation scripts and derived handoffs; skip their artwork and whole-tree links')
    args = parser.parse_args()
    for number in range(1, 11):
        episode = f'Episode_{number:02}'
        commands = [[sys.executable, f'{episode}/check.py']]
        if args.written_only and number >= 4:
            commands[0].append('--written-only')
        if number >= 2:
            commands.append([sys.executable, f'{episode}/sync.py', '--check'])
        for command in commands:
            result = subprocess.run(command, cwd=ROOT)
            if result.returncode:
                return result.returncode
    if args.written_only:
        print('PASS: all ten written episode packages; continuation artwork, graphics and whole-tree links were NOT checked')
    else:
        print(f'PASS: all ten episode packages; {validate_links(ROOT)} local Markdown/HTML path references across the repository')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
