from __future__ import annotations

from typing import List

from langchain_core.pydantic_v1 import Field
from langchain_core.tools import BaseTool
from langchain_core.tools.base import BaseToolkit

from app.portfolio_agent.api_wrapper import PortfolioAPIWrapper
from app.portfolio_agent.tools import SkillsData


class PortfolioToolkit(BaseToolkit):
    """Toolkit for interacting with the Faisal's Portfolio API.

    Parameters:
        api_wrapper: The Portfolio API Wrapper.
    """

    api_wrapper: PortfolioAPIWrapper = Field(default_factory=PortfolioAPIWrapper)

    def __init__(self, api_wrapper: PortfolioAPIWrapper):
        super().__init__()
        self.api_wrapper = api_wrapper

    class Config:
        arbitrary_types_allowed = True

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        print("Getting tools", SkillsData(api_wrapper=self.api_wrapper))
        return [
            SkillsData(api_wrapper=self.api_wrapper),
        ]
