#!/usr/bin/env python3
# filepath: /home/sharif/Documents/Codes/python/weather-agent/list_tools.py
"""
Utility script to list all available tools and their capabilities.
"""

from tools import tool_manager

def main():
    print("🔧 Available Tools for Weather Agent\n")
    print("=" * 50)
    
    tools = tool_manager.list_tools()
    
    if not tools:
        print("No tools found. Make sure tools are properly registered.")
        return
    
    # Group tools by category
    categories = {}
    for name, metadata in tools.items():
        category = metadata["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append((name, metadata))
    
    # Display tools by category
    for category, tool_list in categories.items():
        print(f"\n📂 {category.upper()} TOOLS:")
        print("-" * 30)
        
        for name, metadata in tool_list:
            print(f"🔨 {name}")
            print(f"   📝 {metadata['description']}")
            
            # Show function signature
            sig = metadata['signature']
            print(f"   📋 Usage: {name}{sig}")
            
            if metadata['docstring']:
                # Show first line of docstring
                first_line = metadata['docstring'].split('\n')[0].strip()
                if first_line:
                    print(f"   💡 {first_line}")
            print()
    
    print(f"\n✅ Total tools available: {len(tools)}")
    print("\nTo add new tools, create a new .py file in the tools/ directory")
    print("and use the @tool decorator on your async functions.")

if __name__ == "__main__":
    main()
