# 🌤️ Multi-Purpose Weather Agent

An intelligent, extensible weather and utility assistant powered by **Microsoft AutoGen** and **Ollama**. This agent provides real-time weather information, time operations, calculations, and various utilities through an intuitive chat interface.

##  Features

### 🌍 Weather Services
- **Real-time weather data** for any global location
- **Temperature conversion** (Celsius/Fahrenheit)
- **Weather conditions** and wind speed information
- Powered by OpenStreetMap geocoding and Open-Meteo API

### ⏰ Time Operations
- **Current time** in any timezone worldwide
- **Timezone conversion** between different regions
- Support for common timezone abbreviations (EST, PST, JST, etc.)

### 🧮 Utility Functions
- **Mathematical calculations** with safe expression evaluation
- **Website accessibility checks** with status information
- **Random facts** for entertainment and learning
- **System information** about the agent and its creator

### 🔧 Extensible Architecture
- **Dynamic tool discovery** with `@tool` decorator
- **Category-based organization** (weather, time, utility)
- **Easy expansion** - just add new Python files in `tools/` directory

## 📦 Technology Stack

| Package | Purpose | Version |
|---------|---------|---------|
| **autogen-agentchat** | Core agent framework for intelligent conversations | Latest |
| **autogen-ext[openai]** | OpenAI-compatible model integration | Latest |
| **httpx** | Modern HTTP client for API requests | Latest |
| **pytz** | Timezone handling and conversion | Latest |

### 🤖 AI Model
- **Qwen3 0.6B** - Lightweight yet capable language model
- **Ollama** - Local inference server
- **Function calling** enabled for tool execution

## 🛠️ Installation & Setup

### Prerequisites
- **Python 3.8+**
- **Ollama** installed and running locally

### 1️⃣ Install Ollama
```bash
curl -fsSL https://ollama.ai/install.sh | sh

ollama pull qwen3:0.6b

ollama serve
```

### 2️⃣ Clone & Setup Python Environment
```bash
git clone https://github.com/developersharif/weather-agent.git
cd weather-agent

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate 

pip install -r requirements.txt
```

### 3️⃣ Run the Agent
```bash
python main.py
```

## 💬 Usage Examples

### Weather Queries
```
You: What's the weather in Tokyo?
Agent: [Calls get_weather("Tokyo")] The weather in Tokyo is 22°C, Partly cloudy. Wind speed: 8 km/h.

You: Weather in New York in Fahrenheit
Agent: [Calls get_weather("New York", "fahrenheit")] The weather in New York is 75°F, Clear sky. Wind speed: 12 km/h.
```

### Time Operations
```
You: What time is it in London?
Agent: [Calls get_current_time("Europe/London")] Current time in London: 2025-06-10 14:30:25 BST

You: Convert 3:00 PM from EST to PST
Agent: [Calls convert_timezone("15:00", "EST", "PST")] Time conversion: 2025-06-10 15:00 EST → 2025-06-10 12:00:00 PST
```

### Utility Functions
```
You: Calculate 25 * 4 + 10
Agent: [Calls calculate("25 * 4 + 10")] Calculation: 25 * 4 + 10 = 110

You: Check if google.com is working
Agent: [Calls check_website("google.com")] ✅ Website is accessible
URL: https://google.com
Status Code: 200
```

### Agent Information
```
You: Who created you?
Agent: [Calls about_me()] 👨‍💻 About the Agent Creator
Name: MD Shariful Islam
GitHub: @developersharif
Profession: Software Engineer
...

You: Tell me about your capabilities
Agent: [Calls agent_about()] 🤖 About Your AI Assistant
8 tools available across 3 categories
Real-time data integration
Extensible architecture
...
```

## 📁 Project Structure

```
weather-agent/
├── main.py                 # Entry point and chat interface
├── agent.py                # Agent configuration and setup
├── requirements.txt        # Python dependencies
├── list_tools.py          # Tool discovery utility
├── README.md              # This file
└── tools/                 # Extensible tool system
    ├── __init__.py        # Package initialization
    ├── tool_manager.py    # Dynamic tool discovery
    ├── weather_api.py     # Weather data tools
    ├── time_tools.py      # Time and timezone tools
    └── utility_tools.py   # Mathematical and utility tools
```

## 🔧 Adding New Tools

Creating new tools is simple with the extensible architecture:

1. **Create a new Python file** in the `tools/` directory
2. **Use the `@tool` decorator** on your async functions
3. **Tools are auto-discovered** on startup

Example:
```python
# tools/my_custom_tools.py
from tools.tool_manager import tool

@tool(category="custom", description="My awesome new feature")
async def my_awesome_tool(parameter: str) -> str:
    """
    Description of what this tool does.
    
    Args:
        parameter: Description of the parameter
    
    Returns:
        Result description
    """
    # Your implementation here
    return f"Result: {parameter}"
```

## 🎯 Design Philosophy

- **Real Data Only**: Never provides fake information - always uses API calls
- **Professional Interface**: Clean, emoji-enhanced responses
- **Extensible by Design**: Easy to add new capabilities
- **Local Privacy**: Runs entirely on your machine with Ollama
- **Lightweight**: Efficient 0.6B parameter model

## 👨‍💻 Creator

**MD Shariful Islam**
- GitHub: [@developersharif](https://github.com/developersharif)
- Role: Software Engineer
- Focus: AI/ML Applications & Backend Development

## 📄 License

This project is open source. Feel free to use, modify, and distribute according to your needs.

---

**Built with ❤️ using Microsoft AutoGen and Ollama**
