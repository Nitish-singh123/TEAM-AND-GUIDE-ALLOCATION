# Decisions and Open Questions

This document records approved project direction and decisions that must be settled before the dependent implementation work begins.

## Approved project direction

| Topic | Decision |
|---|---|
| Language | Python 3.12 or a compatible stable Python version |
| Web framework | FastAPI |
| Database | SQLite accessed through Python's built-in `sqlite3` |
| HTML rendering | Jinja2 server-rendered templates |
| Frontend | HTML, CSS, Bootstrap, and lightweight JavaScript; no React or similar framework |
| Testing | pytest |
| Allocation methods | A greedy allocator and an optimal maximum-cardinality allocator using Dinic's algorithm |
| Authentication | Outside the initial MVP unless explicitly approved later |
| External services | No AI APIs, paid services, or external database |
| Team size | Informational; it does not consume multiple guide-capacity slots |

## Core capacity decision

**Guide capacity counts teams, not students.** Every assigned team consumes exactly one guide-capacity slot, regardless of the number of students in the team. A guide with capacity 2 can supervise two teams whether their sizes are 1 or 10.

## Allocator semantics

- Maximum flow optimizes the number of assigned teams subject to eligibility and capacity. It does not inherently optimize preference ranking.
- The maximum-flow graph is expected to use unit capacity from source to each team, edges only for eligible team-guide pairs, and guide-to-sink capacity equal to the guide's team capacity.
- Both algorithms must use the same input snapshot and eligibility relation for a fair comparison.

## Decisions requiring approval

| ID | Question | Why it matters | Proposed resolution |
|---|---|---|---|
| D1 | Is domain equality the default eligibility rule, and do explicit rules only restrict it or may they allow cross-domain pairings? | Defines the eligible edges and the data model. | Use domain equality by default; require an explicit allow-list/override to support cross-domain eligibility. Confirm before coding. |
| D2 | Are preference rankings required in the MVP? | Preferences need storage and UI; ordinary maximum flow ignores ranking. | Defer ranked preferences from the MVP unless explicitly requested. |
| D3 | If preferences are included, should they affect only greedy ordering or should a separate preference-aware optimization be designed? | Preference optimization is not ordinary maximum-cardinality flow and changes scope. | Keep maximum flow cardinality-only; treat preference optimization as a later, separately approved feature. |
| D4 | What exact greedy ordering and guide-selection rule should be used? | Results can vary based on team order and guide choice. | Choose and document a deterministic rule before implementing the greedy allocator. |
| D5 | What unassigned explanation detail is expected? | The reason can range from a basic capacity category to allocator-specific explanation. | MVP baseline: distinguish no eligible guide from eligible guides all at capacity; explain greedy-specific causes if practical and agreed. |
| D6 | What scale-test guide count, edge density, hardware, and numeric runtime target define success for 10,000 teams? | Runtime depends heavily on eligible edges and environment. | Agree a representative sparse workload and measurable target before setting a performance pass/fail threshold. |
| D7 | Should team/guide codes and domains be case-sensitive? | Affects uniqueness constraints, matching, and duplicate validation. | Prefer case-insensitive codes and domain matching; confirm before schema creation. |
| D8 | Should allocations be saved as history or generated on demand only? | Affects schema, UI, and auditability. | Generate on demand from current data; defer persistent run history. |

## Change control

When an open decision is resolved, record the chosen behavior and rationale here and update the PRD, architecture, test plan, and task checklist where relevant. Do not silently implement a proposal as if it were already approved.
