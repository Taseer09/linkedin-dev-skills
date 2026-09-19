# Phase 4: approved writing preferences

## What changed and why

Adds /li-feedback to compare a draft with user edits and propose reusable style
preferences. A user must approve the concrete wording and scope before saving.
The default destination is ~/.claude/linkedin/voice.md, already read by the
existing post skill and li-project. No additional database or model training
is required. A named section holds active rules and a minimal change log.

Show, selective save, revision, and removal are supported by instructions to
the host assistant. There is no separate persistence program: read/write and
approval behavior depends on the host following the skill. These behaviors
must be tested; a valid Markdown file does not prove safe persistence.

The original skills, license, and attribution remain unchanged. No user's
actual voice profile is included in this repository. Samples are fictional.

## Review and validation

feature/feedback-memory builds on feature/claim-review. Its draft PR targets
that branch so the Phase 4 additions can be reviewed separately. Nothing is
merged or released by creating this branch.

Skill-format validation and static review are the local checks. Live Claude
proposal behavior, selective persistence, preservation of unrelated content,
readback in a new session, and removal are pending. Start with the read-only
fixture in examples.md, then use an isolated profile for the write trial.

## Windows installation

From the repository root, check for local changes before switching:

```powershell
git status --short
git fetch origin
git switch feature/feedback-memory
New-Item -ItemType Directory -Force .claude/skills | Out-Null
Copy-Item -Recurse -Force skills/li-feedback .claude/skills/
Add-Content -Path .git/info/exclude -Value '/.claude/skills/li-feedback/'
```

Stop if Git reports conflicting edits; preserve them. Preserve deliberate
edits to an installed skill before copying over it. Restart Claude and invoke
/li-feedback with the proposal-only fixture from examples.md. Do not approve
any saves to your real profile for this first trial. Send the output for review.

Later write tests should name an isolated absolute test path. Default global
profile changes affect other projects; this must be visible in any save preview.
