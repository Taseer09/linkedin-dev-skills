# Phase 3: claim review

## Scope and design

The new /li-proof skill reviews an existing draft against supplied sources.
It separates how well a claim is supported from the type of evidence behind
it. This avoids treating a README assertion as independently established truth.
It explains corrections and offers replacement copy; the user retains control.

Added files: skills/li-proof/SKILL.md and skills/li-proof/examples.md.
No web retrieval, automated posting, model training, or saved memory is added.
The original eleven skills are unchanged. License and attribution are retained.
The Phase 2 skill remains usable independently; invoking li-proof explicitly
reviews any draft, including one produced by li-project.

## GitHub review

feature/claim-review builds on feature/project-to-post. Its draft pull request
targets that branch to show Phase 3 changes separately. It is not a merge or
release. Phase 2 still has its own draft pull request against main.

## Validation

Run the skill-format validator and inspect source links. The examples define
manual behavior checks; they do not prove model compliance. A live Claude
trial is pending. No accuracy percentage or verified badge is warranted.

## Windows trial

From the repository root, inspect local work before switching branches:

```powershell
git status --short
git fetch origin
git switch feature/claim-review
```

If Git reports conflicting local edits, stop and preserve them. Otherwise,
install the new skill locally (preserve deliberate edits if already installed):

```powershell
New-Item -ItemType Directory -Force .claude/skills | Out-Null
Copy-Item -Recurse -Force skills/li-proof .claude/skills/
Add-Content -Path .git/info/exclude -Value '/.claude/skills/li-proof/'
```

Restart Claude in this folder. Invoke /li-proof with the draft and evidence in
skills/li-proof/examples.md. Ask it not to edit files. Check that it flags the
five unsupported or conflicting claims, produces grounded replacement copy,
and does not call its review independent verification. Share the response for
review; it does not post to LinkedIn.
