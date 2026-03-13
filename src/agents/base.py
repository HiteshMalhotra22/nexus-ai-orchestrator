from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    async def act(self, task_description: str, context: Dict[str, Any]) -> Any:
        pass

class ResearcherAgent(BaseAgent):
    async def act(self, task_description: str, context: Dict[str, Any]) -> str:
        # Simulate web search or DB query
        return f"Research data for {task_description}"

class AnalystAgent(BaseAgent):
    async def act(self, task_description: str, context: Dict[str, Any]) -> str:
        # Simulate data processing
        return f"Analysis of {context.get('research_data')}"

class FinalizerAgent(BaseAgent):
    async def act(self, task_description: str, context: Dict[str, Any]) -> str:
        # Simulate report generation
        return f"Final synthesized report based on {context.get('analysis_data')}"