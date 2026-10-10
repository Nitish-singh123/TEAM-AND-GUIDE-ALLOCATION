# Security and Data Integrity

## Scope

The MVP is a local, single-user application without authentication. Lack of authentication is not suitable protection for a publicly exposed deployment. Do not expose the application to untrusted networks without a separately approved security design.

## Input validation

- Validate all form and request data on the server, even if browser controls also validate it.
- Enforce required codes/domains, the approved code uniqueness and normalization rules, positive team sizes, and non-negative capacities.
- Bound input lengths and reject malformed or unsupported values with clear field-level errors.
- Validate explicit eligibility references against existing team and guide records.
- Never trust submitted allocation results; calculate results on the server.

## Database access and integrity

- Use parameterized SQL for all values; never build SQL by concatenating user input.
- Enforce uniqueness and foreign-key integrity in SQLite where appropriate, and enable foreign-key checks for connections.
- Use transactions for multi-step changes so partial writes are not reported as success.
- Keep database access centralized in the data layer and avoid exposing raw SQL errors to users.
- Backups and migrations should be documented when persistence features are implemented.

## Error handling

- Return understandable validation and operation errors to the user.
- Log actionable diagnostic details server-side without logging secrets or unnecessarily sensitive input.
- Do not display stack traces, SQL statements, local file paths, or database contents in web responses.
- Fail explicitly when allocation or export fails; do not return an empty or success-shaped result on error.

## CSV export safety

- Use a standard CSV writer so delimiters, quotes, and newlines are escaped correctly.
- Include only fields needed to explain the allocation.
- Consider spreadsheet formula injection: untrusted text beginning with formula-triggering characters (for example `=`, `+`, `-`, or `@`) should be neutralized for spreadsheet consumers without corrupting ordinary CSV data.
- Test CSV encoding, quoting, formula-sensitive cells, and download headers.

## Secrets and configuration

- The documented MVP currently requires no secret keys, API credentials, or external services.
- Do not commit `.env` files or credentials. `.env.example` should only list configuration that the application actually introduces.
- If a later feature requires a secret, load it from the environment, document it, and add only a placeholder to `.env.example`.

## Web protections

- Keep Jinja2 autoescaping enabled for HTML templates; do not mark user data as safe HTML.
- Use POST for state-changing operations and avoid destructive actions through plain GET links.
- Use a CSRF defense if the app is deployed in a browser-accessible environment where cross-site requests are a concern; deployment assumptions and framework configuration must be reviewed before public exposure.
- Do not enable debug error pages in a production deployment.

## Database integrity and operational limits

- Define sensible input-size limits to prevent accidental resource exhaustion.
- Keep algorithm limits and expected workload documented; 10,000 teams is a performance test target, not a claim that every graph density is inexpensive.
- Treat database files and generated exports as local data, exclude them from version control, and restrict access through the operating system.
