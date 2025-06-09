"""
Tools package for the weather agent.
This package contains all available tools and the tool management system.
"""

from .tool_manager import tool_manager, tool
from .weather_api import get_weather

# Import all tool modules to register them
from . import time_tools
from . import utility_tools


tool_manager.discover_tools()


__all__ = ['tool_manager', 'tool', 'get_weather']
