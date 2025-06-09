import asyncio
import httpx
import json
from tools.tool_manager import tool

@tool(category="utility", description="Calculate basic mathematical expressions")
async def calculate(expression: str) -> str:
    """
    Calculate basic mathematical expressions safely.
    
    Args:
        expression: Mathematical expression to evaluate (e.g., "2 + 3 * 4")
    
    Returns:
        The result of the calculation
    """
    try:
        # Only allow safe mathematical operations
        allowed_chars = set("0123456789+-*/().% ")
        if not all(c in allowed_chars for c in expression):
            return "Error: Only basic mathematical operations are allowed (+, -, *, /, %, parentheses)"
        
        # Evaluate the expression safely
        result = eval(expression)
        return f"Calculation: {expression} = {result}"
        
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error in calculation: {str(e)}"

@tool(category="utility", description="Get random facts or quotes")
async def get_random_fact() -> str:
    """
    Get a random interesting fact.
    
    Returns:
        A random fact
    """
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get("https://uselessfacts.jsph.pl/random.json?language=en")
            response.raise_for_status()
            
            data = response.json()
            fact = data.get('text', 'No fact available')
            
            return f"🧠 Random Fact: {fact}"
            
    except Exception as e:
        # Fallback facts if API is unavailable
        fallback_facts = [
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "A group of flamingos is called a 'flamboyance'.",
            "The shortest war in history lasted only 38-45 minutes between Britain and Zanzibar in 1896.",
            "Octopuses have three hearts and blue blood.",
            "A day on Venus is longer than its year."
        ]
        import random
        return f"🧠 Random Fact: {random.choice(fallback_facts)}"

@tool(category="utility", description="Check if a website is accessible")
async def check_website(url: str) -> str:
    """
    Check if a website is accessible and get basic information.
    
    Args:
        url: The website URL to check
    
    Returns:
        Website status and basic information
    """
    try:
        # Add protocol if missing
        if not url.startswith(('http://', 'https://')):
            url = f"https://{url}"
        
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.head(url)
            
            status = "✅ Website is accessible"
            info = f"Status Code: {response.status_code}"
            
            # Get some headers
            content_type = response.headers.get('content-type', 'Unknown')
            server = response.headers.get('server', 'Unknown')
            
            return f"{status}\n🌐 URL: {url}\n📊 {info}\n📄 Content Type: {content_type}\n🖥️ Server: {server}"
            
    except httpx.ConnectTimeout:
        return f"❌ Connection timeout for {url}"
    except httpx.HTTPStatusError as e:
        return f"⚠️ HTTP Error {e.response.status_code} for {url}"
    except Exception as e:
        return f"❌ Error checking {url}: {str(e)}"

@tool(category="utility", description="Get information about the agent creator")
async def about_me() -> str:
    """
    Get information about the creator of this AI agent.
    
    Returns:
        Information about MD Shariful Islam, the agent creator
    """
    try:
        creator_info = f"""👨‍💻 **About the Agent Creator**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👋 **Personal Information:**
• Full Name: MD Shariful Islam
• Profession: Software Engineer
• Specialization: AI/ML Applications & Web Development

🌐 **Social Media & Professional Profiles:**
• GitHub: @developersharif
• Facebook: @developersharif  
• X (Twitter): @developersharif
• LinkedIn: @developersharif

💼 **Professional Background:**
• Role: Software Engineer
• Focus Areas: Artificial Intelligence, Machine Learning, Backend Development
• Current Project: Weather Agent with Extensible Tool System

🚀 **This Project:**
• Created: Multi-Purpose Weather & Utility Assistant
• Technology Stack: Python, AutoGen, Ollama, Qwen3
• Architecture: Extensible tool system with dynamic discovery
• Features: Weather data, time operations, calculations, web utilities

🎯 **Vision:**
• Building intelligent, practical AI applications
• Creating extensible and maintainable software architectures
• Combining real-world utility with cutting-edge AI technology

📫 **Connect:**
• Open to collaboration and networking
• Passionate about AI/ML development
• Available across all major platforms as @developersharif
"""
        
        return creator_info
        
    except Exception as e:
        return f"❌ Error getting creator information: {str(e)}"

@tool(category="utility", description="Get information about the AI agent and its capabilities")
async def agent_about() -> str:
    """
    Get detailed information about the AI agent and its capabilities.
    
    Returns:
        Comprehensive information about the agent
    """
    try:
        agent_info = f"""🤖 **About Your AI Assistant**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 **Identity & Purpose:**
• Name: Multi-Purpose Weather & Utility Assistant
• Version: 1.0 (Enhanced with Extensible Tools)
• Primary Role: Weather information, time operations, and general utilities
• Model: Qwen3:0.6b (via Ollama)

🛠️ **Available Capabilities:**
• 🌤️ **Weather Services**: Real-time weather data for any global location
• ⏰ **Time Operations**: Current time, timezone conversions
• 🧮 **Mathematical Calculations**: Safe expression evaluation
• 🌐 **Web Utilities**: Website accessibility checks
• 🧠 **Knowledge Base**: Random facts and information
• 👤 **System Information**: User and system details

🔧 **Technical Architecture:**
• Framework: Microsoft AutoGen AgentChat
• Tool System: Dynamic discovery with @tool decorators
• API Integration: OpenStreetMap (geocoding), Open-Meteo (weather)
• Language Model: Qwen3 0.6B parameters
• Interface: Command-line interactive chat

📊 **Current Session Stats:**
• Tools Available: 8 functions across 3 categories
• Categories: Weather, Time, Utility
• Response Mode: Professional with emoji enhancement
• Function Calling: Enabled for real-time data

🎯 **Design Philosophy:**
• Always use real data via tool calls
• Never provide fake or made-up information
• Professional, helpful, and accurate responses
• Extensible architecture for easy capability expansion

💡 **How to Extend:**
• Add new tools in the tools/ directory
• Use @tool decorator for auto-discovery
• Follow async function patterns
• Categories: weather, time, utility, or custom

🚀 **Created for:** Sharif's Weather Agent Project
📅 **Last Updated:** June 2025
"""
        
        return agent_info
        
    except Exception as e:
        return f"❌ Error getting agent information: {str(e)}"
