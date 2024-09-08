import json
from typing import Any, List, Optional

import requests
from langchain_core.pydantic_v1 import BaseModel

from cleaning import clean_about_data
from ..config import portfolio_api


class PortfolioAPIWrapper(BaseModel):
    """Wrapper for the Portfolio API."""

    def __init__(self, **data: Any):
        super().__init__(**data)

    def get_about_data(self) -> Optional[dict]:
        """
        Get the general information about Faisal.
        :return: a dict containing the general information about Faisal
        """
        response = requests.get(f"{portfolio_api}data/aboutData.json")
        data = response.json()
        return clean_about_data(data)

    def run(self, mode: str, ticker: str, **kwargs: Any) -> str:
        if mode == "get_about_data":
            return json.dumps(self.get_about_data())
        else:
            raise ValueError(f"Invalid mode {mode} for Portfolio API Wrapper")
