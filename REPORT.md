\# TP2 Report — Group 3: DevOps \& NetOps



\## Part 1 — Python Environment and uv



\- Inspected the global Python environment using `scripts/inspect\_env.py`.

\- Inspected the project virtual environment using `uv run python scripts/inspect\_env.py`.

\- Global Python: 3.12.4.

\- Project virtual environment Python: 3.14.8.

\- Confirmed that `uv run` executes Python inside the project virtual environment.

\- Added `.gitignore` to exclude `.venv`, `.env`, build output, Python caches, and test caches.

\- Initial Git commit: `d051ef9`.



\## Part 2 — GitHub REST API



\- Installed `requests` and `python-dotenv` using `uv add`.

\- Configured environment variables through `.env`.

\- Implemented configuration validation in `config.py`.

\- Implemented a GitHub API client in `client.py`.

\- Endpoint: `GET https://api.github.com/user`.

\- Authentication: Bearer token supplied through `GITHUB\_TOKEN`.

\- User-Agent: `Epita-Student-CLI`.

\- Verified a successful live API response.

\- Returned status: `LIVE\_SUCCESS`.

\- Authenticated username: `sheshank1212`.

\- Public repositories: 16.

\- Followers: 0.

\- Verified that `.env` is ignored by Git and that the real token is not included in the report.



\## Part 3 — Dependency Management and Testing



Pending completion.



