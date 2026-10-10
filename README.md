# Team and Guide Allocation

A planned web application for comparing a simple greedy team-to-guide allocator with an optimal maximum-cardinality allocator based on Dinic's maximum-flow algorithm.

## Planned features

- Manage teams and guides, including codes, domains, team sizes, and guide capacities.
- Define team-guide eligibility using rules to be confirmed before implementation.
- Compare greedy and maximum-flow assignments using the same input data.
- Review assignments, unassigned teams and reasons, guide loads, and unused capacity.
- Export results to CSV.
- Validate correctness and benchmark representative workloads up to 10,000 teams.

**Capacity rule:** Guide capacity counts teams, not students. Each assigned team uses one capacity slot; team size is informational.

## Technology

Python 3.12 or a compatible stable Python version, FastAPI, SQLite with Python's built-in `sqlite3`, Jinja2, HTML/CSS/Bootstrap, lightweight JavaScript, and pytest. Authentication, external databases, frontend frameworks, and paid/AI services are outside the initial MVP.

## Project documentation

- [Product requirements](./docs/PRD.md)
- [Architecture](./docs/ARCHITECTURE.md)
- [Interface design](./docs/DESIGN.md)
- [Test plan](./docs/TEST_PLAN.md)
- [Security and data integrity](./docs/SECURITY.md)
- [Decisions and open questions](./docs/DECISIONS.md)
- [Project memory](./docs/MEMORY.md)
- [Coding rules](./RULES.md)
- [Implementation tasks](./TASKS.md)

## Setup and run

### Windows (PowerShell)

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

If the Python launcher is unavailable, install Python 3.12 and use `python` in place of `py -3.12` when creating the virtual environment.

### macOS / Linux

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000/> for the home page. The health endpoint is <http://127.0.0.1:8000/health>.

The page loads Bootstrap CSS from jsDelivr, so the browser needs an internet connection to display Bootstrap styling. The application itself does not call an external API.

### Run tests

With the virtual environment activated:

```text
python -m pytest
```

## Current status

Runnable development skeleton with a health endpoint and Jinja2 home page. Allocation and database schema features are not implemented. The SQLite connection factory is available for later data-access work; it creates independent connections and does not create tables.
