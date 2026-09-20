# Phase 1: baseline and development scope

Upstream: https://github.com/Jakeschincariol/linkedin-agent-skill
Inspected commit: add2c23 (shallow clone). Branch: phase-1-baseline.

## Status

Public repository cloned and inspected. Read and write access confirmed for
https://github.com/Taseer09/linkedin-dev-skills. No release has been published. Original license, author
credit, skill files, and plugin metadata are unchanged.

## Architecture

- Eleven Markdown skills in skills/li-*/SKILL.md.
- Two standard-library Python utilities: humanize.py and detect.py.
- JSON data for hooks, cleanup rules, and profile scoring.
- Claude plugin and marketplace manifests.
- Voice template; skills use ~/.claude/linkedin for user state.
- No application server or model training required.
- No tracked test files found in the inspected revision.

## Baseline checks

Tested on Python 3.12.14, Linux; Windows not yet tested.

- All repository JSON files parsed successfully.
- Confirmed eleven SKILL.md files.
- humanize.py accepted stdin and returned valid JSON.
- A sample URL containing words in the replacement dictionary was preserved.
- detect.py accepted stdin and returned valid JSON (REVIEW, 62.0).
- JSON detection mode returns exit code 0 even for REVIEW because it returns
  before the normal exit-status logic. Consumers must inspect the verdict.
- Claude CLI is unavailable here. Skill discovery and a real /li-post session
  are unverified; script execution does not establish end-to-end skill success.

## Confirmed issues and design implications

1. Cleanup changed 'robust scaling' into 'solid scaling'. Technical wording
   needs preservation or review before applying lexical substitutions.
2. Cleanup changed the joined developer emoji into two separate emoji by
   removing U+200D. Preserve meaningful Unicode joiners before multilingual use.
3. The scorer uses an English-only word regex and fixed heuristic thresholds.
   Do not interpret its score as verified authorship or factual accuracy.
4. li-post's example adds dollar amounts and personal history absent from its
   sample input, despite its no-fabrication rule. Our examples must demonstrate
   evidence discipline as well as describe it.
5. li-post already logs accepted posts. Future content memory should extend that
   history rather than introduce a conflicting log.

## Version 0.1 scope

1. /li-project: supplied README or notes to announcement, technical explanation,
   and lessons-learned drafts. Ask about personal contribution; never infer it
   merely from access to a repository. Treat supplied content as data, not
   instructions to execute.
2. /li-proof: map claims to sources; distinguish documented assertions,
   user-confirmed experience, independently checked evidence, and unsupported
   claims. A README alone does not verify benchmark results.
3. /li-feedback: compare draft and final edit; propose voice preferences and
   persist only approved changes with removal support.

Manual publishing remains the first-release workflow. Automatic GitHub import,
dashboard, multilingual support, analytics, and model training are outside v0.1.

## Remaining Phase 1 gates

- In the user's chosen Claude environment, follow the upstream install steps,
  supply real writing samples, and run /li-post on a real project idea.
- Confirm hook output, draft output, humanizer execution, and no invented claims.
- Run Python smoke checks on Windows if Windows is the development target.

Phase 2 can then add skills/li-project/SKILL.md and examples. Keep this report
with the fork so contributors can distinguish checks performed from pending work.

