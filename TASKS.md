# Implementation Task Checklist

Tasks are ordered. Do not begin feature implementation until the decision gates in Task 1 are resolved. Check off a task only after its acceptance criteria and tests pass.

## 1. Resolve implementation decisions

- [ ] Record approved eligibility semantics, preference scope, greedy ordering/tie-breaking, unassigned explanations, code/domain normalization, result-history behavior, and scale-test workload/target in [docs/DECISIONS.md](./docs/DECISIONS.md).
- **Acceptance criteria:** Every decision needed by the data model or first allocator has an explicit answer; remaining questions are marked as deferred and do not block the first implementation slice.
- **Tests:** No automated tests required; review that [docs/PRD.md](./docs/PRD.md), [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md), and [docs/TEST_PLAN.md](./docs/TEST_PLAN.md) agree with the decisions.

## 2. Create the Python application skeleton

- [x] Add the minimal FastAPI entry point, package layout, dependency manifest, health route, and Jinja2 home page.
- **Acceptance criteria:** The app can be imported and launched locally; `/health` returns `{"status":"ok"}`; `/` renders the starter template; an independent SQLite connection factory uses only `sqlite3` and creates no tables; no authentication, external database, or frontend framework is introduced.
- **Tests:** `python -m pytest` passes the health, home-page, static-JavaScript, and independent SQLite-connection tests; verify Uvicorn starts and serves `/`, `/health`, and `/static/app.js`.

## 3. Add SQLite schema and data access

- [ ] Create database initialization and parameterized CRUD access for teams, guides, and approved eligibility records.
- **Acceptance criteria:** Approved constraints are represented in schema and enforced; foreign keys are enabled; transactions avoid partial writes.
- **Tests:** Temporary-database tests cover persistence, uniqueness, references, rollback, and CRUD behavior.

## 4. Implement input validation and management services

- [ ] Validate and manage team/guide records through service functions before wiring all pages.
- **Acceptance criteria:** Invalid codes, domains, sizes, capacities, duplicates, and missing references produce explicit, understandable errors according to the approved rules.
- **Tests:** Unit tests cover valid and invalid boundaries; integration tests verify service/database behavior.

## 5. Implement approved eligibility construction

- [ ] Convert stored domain and explicit-rule data into a consistent set of eligible team-guide pairs.
- **Acceptance criteria:** The output exactly follows the approved eligibility policy and contains no missing or unknown references.
- **Tests:** Unit tests cover same-domain, cross-domain, allow, deny, and precedence cases applicable to the approved policy.

## 6. Implement greedy allocation

- [ ] Implement the approved deterministic greedy policy using the shared eligibility input.
- **Acceptance criteria:** No team is assigned more than once, no ineligible edge is used, capacities are respected, and repeated runs with identical inputs return identical results.
- **Tests:** Unit tests cover empty input, exhausted capacity, multiple choices, tie-breaking, and a case where greedy is not optimal.

## 7. Implement Dinic maximum-flow allocation

- [ ] Implement Dinic's algorithm for the team-to-guide capacity network and return normalized assignments.
- **Acceptance criteria:** Results obey all assignment invariants and maximize assignment cardinality on known test graphs.
- **Tests:** Unit tests cover known maximum-flow graphs, zero capacities, no edges, multiple optimal solutions, and cases where reassignment improves the total.

## 8. Implement shared reporting and explanations

- [ ] Normalize both results and calculate assignment counts, unassigned teams/reasons, guide loads, and unused capacity.
- **Acceptance criteria:** Both allocators use the same report shape; all totals reconcile with assignments and capacities; no false success result is produced on failure.
- **Tests:** Unit tests check all counts and reason categories, including no eligible guide and all eligible guides full.

## 9. Add server-rendered management and comparison pages

- [ ] Add FastAPI routes and Jinja2 pages for team/guide management, eligibility, and allocation comparison.
- **Acceptance criteria:** A coordinator can complete the approved core journey using accessible, responsive forms and clearly labeled results; empty, loading, validation, and error states are handled.
- **Tests:** API tests cover route behavior and errors; UI tests cover the core journey, keyboard-accessible fields, and responsive layouts.

## 10. Add CSV export

- [ ] Export the normalized allocation results as a downloadable CSV.
- **Acceptance criteria:** CSV includes clearly identified allocation method, team, guide/status, and relevant reason fields; quoting and spreadsheet safety follow [docs/SECURITY.md](./docs/SECURITY.md).
- **Tests:** API/export tests cover headers, assigned and unassigned records, commas, quotes, newlines, Unicode, and formula-sensitive values.

## 11. Verify scale and complete user documentation

- [ ] Run correctness and performance checks on the approved workload of up to 10,000 teams; finish local setup and usage instructions.
- **Acceptance criteria:** Correctness invariants pass at scale; measured performance meets the approved target on the documented machine/workload; README setup steps are reproducible.
- **Tests:** Run the full pytest suite and the separately selectable performance benchmark; record team count, guide count, edge count/density, and elapsed time.
