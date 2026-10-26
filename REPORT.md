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



\## Part 4 — CLI Packaging and TestPyPI Deployment



\### Package Build

Built the source distribution and wheel using `uv build`.



\- Source distribution: `epita\_sheshank\_boddu\_devopsnetops-0.1.0.tar.gz`

\- Wheel: `epita\_sheshank\_boddu\_devopsnetops-0.1.0-py3-none-any.whl`



\### TestPyPI Publication

Successfully uploaded both distribution files to TestPyPI using Twine.



Package URL: https://test.pypi.org/project/epita-sheshank-boddu-devopsnetops/0.1.0/



\### Installation Verification

Created a separate virtual environment named `.venv\_test` and installed version `0.1.0` from TestPyPI.



\### CLI Verification

Ran `epita-group3-cli.exe` from the isolated environment. The CLI displayed the GitHub profile information, including API status, username, public repository count, and follower count.



\*\*Result:\*\* Package build, publication, installation, and CLI execution were successful.





