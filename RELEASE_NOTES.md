# LinkedIn Dev Skills v0.1.0

Published September 20, 2026: [GitHub Release v0.1.0](https://github.com/Taseer09/linkedin-dev-skills/releases/tag/v0.1.0).
The tag points to reviewed merge commit `8f35c6c77acd3cb2f61dbf86e17a66d62575d8c4`.

## What this first developer edition adds

- `/li-project`: turn supplied README text or project notes into grounded
  announcement, technical, and personal-lesson drafts. Missing experience stays
  pending rather than becoming a fabricated story.
- `/li-proof`: review factual claims against supplied evidence, distinguish
  absent support from contradiction, and produce corrected copy.
- `/li-feedback`: propose scoped style preferences, save only approved changes,
  and show, revise, or remove them from an editable voice profile.

The package contains fourteen skills: these three additions plus eleven inherited
from Jake Schincariol's linkedin-agent-skill. Original attribution and the MIT
notice are preserved. This fork uses its own version sequence.

## Installation

Use the project-local instructions in [README.md](README.md). Clone `main`
for the current version, or tag `v0.1.0` for the exact published snapshot.
Claude Code is the tested host. No LinkedIn connection, model training, or
separate API key is needed by the three new skills; normal Claude usage applies.
They use pasted source material and manual publishing. The package checker and
inherited Python utilities require Python; the new Markdown skills do not.

## Validation and limits

- Local package checks and format validation passed for all 14 skills.
- A supplied Windows screenshot shows the package checker passing.
- User-supplied Claude transcripts demonstrate project drafting, claim review,
  selective preference persistence, later-draft application, conflict detection,
  and removal. These are observed trials, not a statistical accuracy evaluation.
- Inherited skill instructions and text cleanup have not been fully audited.
  Cleanup can alter technical terms and meaningful Unicode; li-project avoids
  automatic use of it.
- Plugin-mode installation is included but not exercised. The documented
  project-local installation was exercised in user trials.
- Some copied outputs have uncertain fenced-block formatting; source sentence
  numbering was occasionally imprecise. Review copy and citations before use.
- Preference edits rely on the host following instructions, not a dedicated
  transactional persistence program. Keep important profile files backed up
  through your normal workflow.

Full observations and limitations are in [TESTING.md](TESTING.md).

## Publication status

- Combined PR #4 was merged after owner approval; the merged tree was verified
  and package checks passed. Superseded staged PRs are closed or merged.
- The owner published GitHub Release v0.1.0 on September 20, 2026.
- Community sharing remains pending approval of the text and destination.
  The announcement below is a draft and has not been posted to a community.

The isolated LF-003 test preference is user-local and not included in this
repository. Its cleanup was requested but not confirmed; it is not a source
release blocker and must not be represented as already removed.

## Draft community announcement — not posted

I've extended Jake Schincariol's LinkedIn agent skill pack with three skills
for developers:

- Turn project notes into LinkedIn drafts.
- Check draft claims against the evidence you supply.
- Save writing preferences only after you approve them.

The workflow keeps you in charge of the final text and publishing. It works
with supplied notes; it does not automatically verify every claim or publish
to LinkedIn. The original author is credited and the MIT license is retained.

Repository: https://github.com/Taseer09/linkedin-dev-skills

I'd welcome examples where the drafts miss context or the review misses a claim.
