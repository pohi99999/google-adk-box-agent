"""
Basic tests for the Box Agent
"""

from box_agent import root_agent
from box_agent.agent import BoxAgent


def test_root_agent_exists():
    """Test that the root agent is properly instantiated"""
    assert root_agent is not None
    assert isinstance(root_agent, BoxAgent)
    assert root_agent.name == "BoxFlowAgent"


def test_agent_has_box_agent():
    """Test that the BoxAgent has a box_full_agent"""
    assert hasattr(root_agent, "box_full_agent")
    assert root_agent.box_full_agent is not None


def test_box_agent_tools_import():
    """Test that all required tools can be imported"""
    from box_agent.tools.box_agent_tools import (
        box_who_am_i_tool,
        box_search_tool,
        box_read_tool,
        box_search_folder_by_name,
        box_list_folder_content_by_folder_id,
        box_ask_ai_tool,
        box_ai_extract_data,
    )

    # Verify all tools are callable
    assert callable(box_who_am_i_tool)
    assert callable(box_search_tool)
    assert callable(box_read_tool)
    assert callable(box_search_folder_by_name)
    assert callable(box_list_folder_content_by_folder_id)
    assert callable(box_ask_ai_tool)
    assert callable(box_ai_extract_data)


if __name__ == "__main__":
    test_root_agent_exists()
    test_agent_has_box_agent()
    test_box_agent_tools_import()
    print("All basic tests passed!")
