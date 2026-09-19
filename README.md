# LinkedIn Dev Skills

Turn project notes into LinkedIn drafts, review their claims against supplied
evidence, and save writing preferences you explicitly approve.

**Version 0.1.0 — prepared for release; publication pending.** Fourteen Claude skills: three additions to
Jake Schincariol's original eleven. Not yet a tagged release. The host assistant
generates text and handles approved local preference edits. No model training
or LinkedIn connection is required; Claude's normal usage limits still apply.
You review and manually publish posts.

## The developer workflow

| Skill | Input | Result |
| --- | --- | --- |
| [li-project](skills/li-project/SKILL.md) | Pasted README or notes | Three post angles; missing personal experience stays pending |
| [li-proof](skills/li-proof/SKILL.md) | Draft and supplied evidence | Claim review, explanations, and corrected copy |
| [li-feedback](skills/li-feedback/SKILL.md) | Original and edited drafts | Tentative style proposals; only approved preferences are saved |

Reading a README does not independently verify its claims. These skills use
supplied text rather than automatic GitHub imports or web evidence retrieval.

The default voice profile is `~/.claude/linkedin/voice.md`, shared across
projects. li-feedback previews changes and supports selective approval and
removal. li-project can read an explicitly selected test profile instead.
Preferences guide style, not personal achievements. Keep profiles out of Git.

## Install the three additions in Claude Code

After the release changes are merged, clone `main` with the commands below.
Before merge, reviewers should use `--branch phase-5-packaging` instead.

```powershell
git clone --branch main https://github.com/Taseer09/linkedin-dev-skills.git
cd linkedin-dev-skills
New-Item -ItemType Directory -Force .claude/skills | Out-Null
foreach ($skillName in 'li-project','li-proof','li-feedback') {
    Copy-Item -Recurse -Force "skills/$skillName" .claude/skills/
}
```

If already cloned, inspect `git status --short`, fetch origin, and switch to
`main` after merge (or `phase-5-packaging` for pre-merge review) before copying. Preserve deliberate edits in installed
copies before replacing them. Generated local copies are ignored by Git.
Restart Claude in this folder and invoke `/li-project`, `/li-proof`, or
`/li-feedback`. If a command is missing, confirm its file exists at
`.claude/skills/<name>/SKILL.md` and report the discovery error.

macOS/Linux equivalent after cloning:

```bash
mkdir -p .claude/skills
cp -R skills/li-project skills/li-proof skills/li-feedback .claude/skills/
```

To update an unchanged checkout on this branch, run `git pull --ff-only` and
repeat the copy block. To uninstall, remove only the named installed skill
folder under `.claude/skills/`; keep your voice profile unless you want it removed.

This follows the documented [project skill location](https://code.claude.com/docs/en/skills).
Plugin packaging is also included: `claude --plugin-dir .` loads a local plugin
for testing, with commands such as `/linkedin-dev-skills:li-project`.
Use one installation method per test. Plugin discovery remains untested here;
see the [plugin reference](https://code.claude.com/docs/en/plugins-reference).

## First try

```text
/li-project
Create drafts from these fictional notes:
NotesIndex is a local prototype. It imports Markdown into SQLite and supports
keyword search through a Python CLI. Semantic search is planned.
No benchmark has been run. No contribution or personal lessons are supplied.
Do not edit files.
```

Expect neutral drafts, a pending personal lesson, and source notes. See the
[claim-review examples](skills/li-proof/examples.md),
[feedback examples](skills/li-feedback/examples.md), and [TESTING.md](TESTING.md).

## Inherited skills

| Command | Purpose |
| --- | --- |
| /li-post | General post drafts and hooks |
| /li-comment | Comment drafts |
| /li-reply | Reply drafts |
| /li-profile | Profile review |
| /li-plan | Weekly planning |
| /li-human | Text cleanup and heuristic scoring |
| /li-carousel | Carousel drafting instructions |
| /li-repurpose | Adapt supplied content |
| /li-dm | Message drafts |
| /li-inbox | Triage supplied inbox content |
| /li-audit | Review supplied performance data |

Their source folders remain available for optional installation. The inherited
Python utilities need Python; the new three skills do not. li-human can alter
technical terms and meaningful Unicode; its score is not an authorship or truth
test. li-project avoids automatic use of it. See [known limitations](TESTING.md).

## Development and credit

Run `python scripts/check_package.py` for package and utility smoke checks.
Behavioral validation still requires a host assistant. See
[CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md).

Original project: [linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill)
by **Jake Schincariol**. Developer-edition additions are maintained in
**Taseer09/linkedin-dev-skills**. The original [MIT license](LICENSE) and copyright
notice are preserved. This fork is not an official LinkedIn product.
