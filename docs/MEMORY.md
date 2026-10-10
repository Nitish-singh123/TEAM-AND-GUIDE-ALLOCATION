# Project Memory

## Current status

- Initial documentation baseline and a runnable development skeleton have been created.
- FastAPI serves `/health` and a Jinja2 home page; allocation features are not implemented.
- The SQLite connection factory uses independent built-in `sqlite3` connections and does not create tables.
- The workspace is not currently a Git repository.

## Completed work

- Captured product goals and MVP scope from the approved project requirements.
- Recorded the proposed FastAPI, Jinja2, SQLite, service, allocator, reporting, and pytest architecture.
- Recorded the capacity rule: one assigned team consumes one guide slot; team size is informational.
- Identified decisions that need approval before dependent implementation.
- Created the PRD, architecture, interface design, test plan, security notes, decisions log, task checklist, coding rules, README, and local ignore/configuration templates.
- Added the FastAPI app package, SQLite connection factory, health route, Jinja2 home page, Bootstrap styling, lightweight navigation JavaScript, requirements, and initial tests.
- Verified all four tests in the project virtual environment and confirmed Uvicorn returned successful health, home-page, and static-file responses.
- The test run reports a non-failing Starlette deprecation warning about using `httpx` with `TestClient`; tests currently pass with the declared dependencies.

## Current task

- Review the open decisions in [DECISIONS.md](./DECISIONS.md) before starting schema or allocation implementation.

## Known issues and open decisions

- Eligibility semantics for domain matching and explicit allow/deny rules need approval.
- Preference ranking scope is undecided; maximum flow as specified optimizes assignment count only.
- Greedy ordering and tie-breaking need definition.
- Unassigned-reason detail needs agreement.
- The 10,000-team performance workload and numeric runtime target need agreement.
- Code/domain case normalization and allocation-history expectations need confirmation.
- There is no Git repository metadata in the inspected workspace.

## Next step

- Confirm the eligibility policy, preference scope, greedy ordering, and performance benchmark before proceeding to the SQLite schema task.
