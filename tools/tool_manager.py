import importlib
import importlib.util
import inspect
from typing import List, Callable, Dict, Any
import os
from pathlib import Path

class ToolManager:
    """
    A dynamic tool manager that can discover, register, and manage tools for the agent.
    This allows for easy extension of agent capabilities by adding new tool modules.
    """
    
    def __init__(self):
        self.tools: Dict[str, Callable] = {}
        self.tool_metadata: Dict[str, Dict[str, Any]] = {}
        
    def register_tool(self, name: str, func: Callable, description: str = "", category: str = "general"):
        """Register a tool function with metadata"""
        self.tools[name] = func
        self.tool_metadata[name] = {
            "description": description,
            "category": category,
            "signature": inspect.signature(func),
            "docstring": func.__doc__
        }
        
    def discover_tools(self, tools_dir: str = None):
        """
        Automatically discover and register tools from the tools directory.
        Looks for functions that are decorated with @tool or have specific naming patterns.
        """
        if tools_dir is None:
            tools_dir = Path(__file__).parent
        
        tools_path = Path(tools_dir)
        
        for py_file in tools_path.glob("*.py"):
            if py_file.name.startswith("__") or py_file.name == "tool_manager.py":
                continue
                
            module_name = py_file.stem
            try:
                spec = importlib.util.spec_from_file_location(module_name, py_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                for name, obj in inspect.getmembers(module, inspect.iscoroutinefunction):
                    if not name.startswith("_"):
                        self.register_tool(
                            name=name,
                            func=obj,
                            description=obj.__doc__ or f"Tool from {module_name}",
                            category=getattr(obj, "category", module_name)
                        )
                        
            except Exception as e:
                print(f"Warning: Could not load tools from {py_file}: {e}")
                
    def get_tools_list(self) -> List[Callable]:
        """Get list of all registered tool functions"""
        return list(self.tools.values())
        
    def get_tool_by_name(self, name: str) -> Callable:
        """Get a specific tool by name"""
        return self.tools.get(name)
        
    def list_tools(self) -> Dict[str, Dict[str, Any]]:
        """List all available tools with their metadata"""
        return self.tool_metadata.copy()
        
    def get_tools_by_category(self, category: str) -> Dict[str, Callable]:
        """Get all tools in a specific category"""
        return {
            name: func for name, func in self.tools.items()
            if self.tool_metadata[name]["category"] == category
        }

tool_manager = ToolManager()

def tool(category: str = "general", description: str = ""):
    """
    Decorator to mark functions as tools and automatically register them.
    
    Usage:
    @tool(category="weather", description="Get current weather information")
    async def get_weather(city: str) -> str:
        # implementation
    """
    def decorator(func):
        func.category = category
        func.description = description
        # Auto-register when the module is imported
        tool_manager.register_tool(
            name=func.__name__,
            func=func,
            description=description,
            category=category
        )
        return func
    return decorator
