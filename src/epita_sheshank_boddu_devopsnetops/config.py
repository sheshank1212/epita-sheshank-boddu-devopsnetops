import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv("APP_ENV", "development")
    api_key: str = os.getenv("GITHUB_TOKEN", "")
    debug: bool = os.getenv("DEBUG", "False").lower() in (
        "true", "1", "yes"
    )

    def validate(self):
        """Fail immediately if the GitHub token is missing."""
        if not self.api_key or self.api_key.startswith("your_"):
            raise ValueError(
                "GITHUB_TOKEN is missing or still uses the placeholder. "
                "Check your .env file."
            )


config = Settings()