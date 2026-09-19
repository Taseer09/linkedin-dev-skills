#!/usr/bin/env python3
"""Dependency-free package and CLI smoke checks; not an LLM evaluation."""
import ast
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {'li-post', 'li-comment', 'li-reply', 'li-profile', 'li-plan',
            'li-human', 'li-carousel', 'li-repurpose', 'li-dm', 'li-inbox',
            'li-audit', 'li-project', 'li-proof', 'li-feedback'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    entries = list((ROOT / 'skills').glob('*/SKILL.md'))
    require({p.parent.name for p in entries} == EXPECTED, 'Unexpected skill inventory')
    for path in entries:
        text = path.read_text(encoding='utf-8')
        parts = text.split('---', 2)
        require(len(parts) == 3 and not parts[0].strip(), f'Missing frontmatter: {path}')
        name = re.search(r'^name:\s*(\S+)\s*$', parts[1], re.M)
        require(name is not None and name[1] == path.parent.name, f'Skill name mismatch: {path}')
        require(re.search(r'^description:\s*\S', parts[1], re.M), f'Missing description: {path}')

    for path in ROOT.glob('.claude-plugin/*.json'):
        json.loads(path.read_text(encoding='utf-8'))
    for path in (ROOT / 'skills').rglob('*.json'):
        json.loads(path.read_text(encoding='utf-8'))
    plugin = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    require(plugin['name'] == 'linkedin-dev-skills', 'Wrong fork package identity')
    require(market['plugins'][0]['name'] == plugin['name'], 'Marketplace name mismatch')
    require(market['plugins'][0]['source'] == './', 'Invalid local plugin source')
    require(plugin['repository'] == 'https://github.com/Taseer09/linkedin-dev-skills', 'Wrong repository')
    require('Copyright (c) 2026 Jake Schincariol' in (ROOT / 'LICENSE').read_text(), 'Missing upstream notice')

    docs = list(ROOT.glob('*.md')) + list((ROOT / 'skills').rglob('*.md'))
    for path in docs:
        for target in re.findall(r'\]\(([^\s)]+)\)', path.read_text(encoding='utf-8')):
            if '://' in target or target.startswith(('#', 'mailto:')):
                continue
            require((path.parent / target.split('#')[0]).exists(), f'Broken local link: {path}: {target}')
    for path in list((ROOT / 'skills').rglob('*.py')) + list((ROOT / 'scripts').glob('*.py')):
        ast.parse(path.read_text(encoding='utf-8'), filename=str(path))

    def run(script, args, text):
        result = subprocess.run([sys.executable, str(ROOT / 'skills/li-human' / script), *args],
                                input=text, text=True, encoding='utf-8', capture_output=True, timeout=15)
        require(result.returncode == 0, f'{script} failed: {result.stderr}')
        return result.stdout

    url = 'https://example.com/robust?q=leverage'
    sample = 'I built a Python tool. See ' + url
    clean = json.loads(run('humanize.py', ['-', '--json'], sample))
    require(url in clean['text'], 'Cleanup damaged a URL')
    require(clean['text'] == sample + '\n', 'Cleanup altered plain sample unexpectedly')
    score = json.loads(run('detect.py', ['-', '--json'], sample))
    require(score['verdict'] in {'PASS', 'REVIEW', 'FLAGGED'}, 'Invalid scorer verdict')
    require(0 <= score['human_score'] <= 100, 'Invalid score range')
    print('PASS: 14 skills, package metadata, local links, Python syntax, credit, and CLI smoke checks.')
    print('Not tested: Claude behavior, Windows execution, or plugin discovery.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, json.JSONDecodeError, subprocess.TimeoutExpired) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
