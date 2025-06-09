import httpx
import asyncio
import time
from tools.tool_manager import tool

@tool(category="weather", description="Get current weather information for any city worldwide")
async def get_weather(city: str, format: str = "celsius") -> str:
    nominatim_headers = {
        'User-Agent': 'WeatherAgent/1.0 (weather-agent-project-python; contact@realbrain.cc)',
        'Accept-Language': 'en,en-US;q=0.9',
    }
    
    regular_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }
    
    timeout = httpx.Timeout(10.0, connect=5.0) 
    
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            try:
                location_response = await client.get(
                    "https://nominatim.openstreetmap.org/search",
                    params={"q": city, "format": "json"},
                    headers=nominatim_headers 
                )
                location_response.raise_for_status() 
                
                location_data = location_response.json()
                if not location_data:
                    return f"Error: Could not find location '{city}'"
                
                lat = location_data[0]["lat"]
                lon = location_data[0]["lon"]
                location_name = location_data[0]["display_name"]
              
                await asyncio.sleep(1)
                
                weather_response = await client.get(
                    "https://api.open-meteo.com/v1/forecast",
                    params={
                        "latitude": lat,
                        "longitude": lon,
                        "current_weather": "true"
                    },
                    headers=regular_headers
                )
                weather_response.raise_for_status() 
                
                weather_data = weather_response.json()
                
                temperature = weather_data["current_weather"]["temperature"]
                windspeed = weather_data["current_weather"]["windspeed"]
                weathercode = weather_data["current_weather"]["weathercode"]
                
                weather_descriptions = {
                    0: "Clear sky",
                    1: "Mainly clear",
                    2: "Partly cloudy",
                    3: "Overcast",
                    45: "Fog",
                    48: "Depositing rime fog",
                    51: "Light drizzle",
                    53: "Moderate drizzle",
                    55: "Dense drizzle",
                    56: "Light freezing drizzle",
                    57: "Dense freezing drizzle",
                    61: "Slight rain",
                    63: "Moderate rain",
                    65: "Heavy rain",
                    71: "Slight snow fall",
                    73: "Moderate snow fall",
                    75: "Heavy snow fall",
                    95: "Thunderstorm"
                }
                
                weather_desc = weather_descriptions.get(weathercode, f"Unknown ({weathercode})")
                
            
                if format.lower() == "fahrenheit":
                    temperature = (temperature * 9/5) + 32
                    temp_unit = "°F"
                else:
                    temp_unit = "°C"
                    
                return f"The weather in {city} ({location_name}) is {temperature}{temp_unit}, {weather_desc}. Wind speed: {windspeed} km/h."
                
            except httpx.HTTPStatusError as e:
                return f"API Error: {e.response.status_code} - {e.response.text}"
                
    except httpx.ConnectTimeout:
        return f"Error: Connection timeout while trying to get weather data. Please check your internet connection or try again later."
    except httpx.ReadTimeout:
        return f"Error: Read timeout while waiting for API response. Please try again later."
    except Exception as e:
        return f"Error: {str(e)}"

# # Create an async main function
# async def main():
#     city = input("Enter city name: ") or "London"
#     unit = input("Enter unit (celsius/fahrenheit): ").lower() or "celsius"
#     if unit not in ["celsius", "fahrenheit"]:
#         unit = "celsius"
    
#     print(f"Getting weather for {city}...")
#     result = await get_weather(city, unit)
#     print(result)

# # Run the async function properly
# if __name__ == "__main__":
#     asyncio.run(main())