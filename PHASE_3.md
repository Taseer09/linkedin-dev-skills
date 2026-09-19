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

Skill-format validation passed. The first user-supplied Claude screenshot
was reviewed on 2026-09-19. It flagged all five questionable claims, removed
unsupported statements from replacement copy, kept semantic search planned,
and explicitly disclaimed independent verification and publication.

Two classification errors remain in that trial: prototype status was treated
as contradicting production readiness, and absent benchmarks as contradicting
actual speed. Both claims lack support, but the supplied facts alone do not
disprove them. The evidence-basis column also omitted explicit basis labels.

The instructions now contain concrete Unsupported-versus-Conflicting examples
and explicitly require basis labels. Format validation passed after the edit;
a live rerun of these corrections is pending. Fenced-block rendering is
unconfirmed from the screenshot. Other cases remain untested; no accuracy
percentage or verified badge is warranted.

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
