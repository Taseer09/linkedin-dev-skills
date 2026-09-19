# Testing and release gates

## Automated package check

Requires Python 3.10+; no third-party Python dependencies.

```text
python scripts/check_package.py
```

Checks 14 skill entry points, JSON package consistency, local Markdown links,
Python syntax, license credit, and executable smoke tests for the two inherited
Python utilities. This is not a Claude behavioral evaluation or full JSON/YAML
schema validation. A user-supplied Windows PowerShell screenshot shows a PASS
on the phase-5-packaging checkout. The screenshot does not show the exact Python
version or commit hash. The three local skill copies refreshed without errors.

## Observed manual trials

User-supplied Claude Code transcripts support project drafting, no invented
personal role when missing, correct claim labels after clarification, selective
preference save, file readback, and removal. See PHASE_2.md, PHASE_3.md, and
PHASE_4.md for exact limitations. Never turn those observations into an accuracy
percentage or claim that every edge case passes.

## Combined trial — partial result

User-supplied transcripts show LF-002 saved to the isolated profile, followed
by li-project reading that profile, ignoring removed LF-001, and opening with
a question. This supports preference propagation on the observed trial.

The generated question and body added unsupported privacy guarantees:
'without sending them anywhere' and 'Everything stays on your machine'.
Local prototype/SQLite notes do not establish network behavior. Source notes
also omitted these claims. This is a factual-grounding failure, so the combined
trial has not passed overall. The save diff shows only an active preference
addition, with no matching LF-002 action-log addition visible.

The instructions now explicitly check factual implications in hooks/privacy
claims and require active-state plus dated-log verification in the same edit.
The drafting and action-log fixes need a targeted live check. A subsequent
user-supplied li-proof transcript correctly marked both privacy guarantees
Unsupported and the documented functionality/status Supported. It retained the
no-benchmark meaning and made no independent-verification claim. It omitted
the corrected draft normally requested by the skill; this output-completeness
issue remains. Its additional criticism of 'your own notes' was overly strict:
ordinary audience framing is not itself a product guarantee. LF-002 still
needs test cleanup. This trial supports detecting the privacy error, not full
combined-workflow completion.

## Combined trial procedure

Install the three current developer skills. Use this isolated profile:
`D:\linkedin-agent\li-feedback-test\voice.md`. If the path already has an
unrelated rule, preserve it and resolve conflicts rather than overwriting it.

1. Invoke li-feedback: approve saving this exact preference to that test path:
   'Scope: technical project announcements. Begin the draft with a short
   question about the project's documented purpose.' This is a synthetic rule
   for an observable integration test, not a permanent personal preference.
2. Start a fresh Claude session. Invoke li-project with only an announcement
   requested, explicitly selecting that profile, and supply:
   'NotesIndex is a local prototype. It imports Markdown into SQLite and
   provides keyword search through a Python CLI. Semantic search is planned.
   No benchmark has been run. No authorship information is supplied.'
3. Confirm the selected profile was read, the draft opens with a relevant
   question, ownership is not invented, and future features stay planned.
4. Invoke li-proof on that actual output plus the same evidence. Check that
   style is not mistaken for a factual claim and unsupported facts are absent.
5. Remove only the test rule's assigned LF ID with li-feedback. Read back the
   file and confirm unrelated content is intact. Do not delete the whole file.

Record the actual output and revision tested. One successful run supports the
workflow; it does not prove perfect preference adherence across all outputs.

## Before release

- [ ] Combined trial above passes against the packaged revision.
- [ ] Check preference conflict handling with an isolated existing profile.
- [x] Run package check on Windows and record the result (user-supplied screenshot).
- [ ] Confirm installation/discovery from the selected distribution method.
- [ ] Review changed skills and known limitations; approve merge order.
- [ ] Replace development version with the agreed release version and tag the
      reviewed commit only after owner approval.

Draft PRs are stacked: Phase 2 targets main, Phase 3 targets Phase 2, Phase 4
targets Phase 3, and Phase 5 targets Phase 4. Review them together before choosing
the merge strategy; do not assume merging one publishes all later branches.

## Known inherited limitations

li-human can change technical wording (robust scaling becomes solid scaling)
and remove meaningful Unicode joiners. Its scores are heuristics, not authorship
or truth tests. li-project avoids automatic use of it. The inherited li-post
still calls it and has examples with unsupported details; use the new developer
workflow for source-grounded project content. Original skill examples and
platform-performance assumptions have not received a full audit in this phase.
Plugin-mode discovery and commands have not been exercised here. Individual
project-local skills have been exercised through user-supplied transcripts.
