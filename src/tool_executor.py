from langchain_tavily import TavilySearch
from langchain_core.tools import StructuredTool
from langgraph.prebuilt import ToolNode

from lang_classes import AnswerQuestion, ReviseAnswer

search = TavilySearch()
tavily_tool = search  # TavilySearch now acts as the tool

def run_queries(search_queries: list[str], **kwargs):
    """Run the generated queries."""
    results = tavily_tool.batch([{"query": query} for query in search_queries])
    # Ensure the result is serializable (e.g., list of dicts or strings)
    return [r if isinstance(r, dict) else str(r) for r in results]

tool_node = ToolNode(
    [
        StructuredTool.from_function(run_queries, name=AnswerQuestion.__name__),
        StructuredTool.from_function(run_queries, name=ReviseAnswer.__name__),
    ]
)