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

Skill-format validation passed and static review was performed. The following
observations come from user-supplied Claude Code transcripts reviewed on
2026-09-19, not direct inspection of the user's disk or loaded skill revision.

| Trial | Observed result | Limit |
| --- | --- | --- |
| Proposal only | Tentative P1/P2/P3 suggestions and Not saved; speed-claim removal distinguished from style. | P2 mixed factual discipline with style; it was not approved. No independent no-write check. |
| Selective save | Only P1 written as LF-001 to a new isolated profile and read back. | New-file creation does not test preserving existing content. |
| Subsequent read | LF-001 returned from a file read after a fresh-session test was requested. | Session boundary not independently observed; initial empty page-range error recovered by retry. |
| Removal | LF-001 removed, action log retained without deleted rule wording; unrelated paragraph added outside the managed section and present on readback. | Paragraph was added in the same edit as removal; this is narrower than preservation of an independently pre-existing profile. |

The host reported leaving the default voice profile unchanged; this was not
independently checked. No private profile or original user draft is committed.
These observations support the core selective save/read/remove workflow in
this fixture, not all persistence behavior.

Remaining release checks include applying a saved preference in a later draft,
preserving pre-existing unrelated content, conflict/stale-preview handling,
revision, duplicate and missing-ID no-ops. Avoid repeating successful fixtures
unless a change creates a concrete regression risk.

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
