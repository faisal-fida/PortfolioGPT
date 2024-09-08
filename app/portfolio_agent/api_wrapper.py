import json
from typing import Any, Optional

import requests
from langchain_core.pydantic_v1 import BaseModel

from app.portfolio_agent.cleaning import clean_skills_data
from app.config import portfolio_api


class PortfolioAPIWrapper(BaseModel):
    """Wrapper for the Portfolio API."""

    def __init__(self, **data: Any):
        super().__init__(**data)

    def get_skills_data(self) -> Optional[dict]:
        """
        Get the information about the skills, types of works, and resume URL of Faisal.
        :return: a dict containing the data about the skills, types of works, and resume URL.
        """
        response = requests.get(f"{portfolio_api}data/aboutData.json")
        data = response.json()
        return clean_skills_data(data)

    def run(self, mode: str, **kwargs: Any) -> str:
        if mode == "get_skills_data":
            return json.dumps(self.get_skills_data())
        else:
            raise ValueError(f"Invalid mode {mode} for Portfolio API Wrapper")
