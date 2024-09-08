from typing import Optional

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.pydantic_v1 import Field
from langchain_core.tools import BaseTool

from app.portfolio_agent.api_wrapper import PortfolioAPIWrapper


class SkillsData(BaseTool):
    """
    Tool that gets the skills data from the Portfolio API.
    """

    mode: str = "get_skills_data"
    name: str = "skills_data"
    description: str = (
        "A wrapper around the Faisal's Portfolio API. "
        "This tool is useful for fetching the information about the skills, types of works, and resume URL of Faisal."
        "The skills include the Languages, Frameworks, and Tools."
        "The types of works include the categories of the skills."
        "The resume URL is the URL of the resume of Faisal to view."
    )

    api_wrapper: PortfolioAPIWrapper = Field(..., exclude=True)

    def __init__(self, api_wrapper: PortfolioAPIWrapper):
        super().__init__(api_wrapper=api_wrapper)

    def _run(self, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Use the Portfolio API Wrapper to get the skills data."""
        return self.api_wrapper.run(mode=self.mode)
