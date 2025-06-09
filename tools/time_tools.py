import asyncio
from datetime import datetime, timezone
import pytz
from tools.tool_manager import tool

@tool(category="time", description="Get current time in a specific timezone")
async def get_current_time(timezone_name: str = "UTC") -> str:
    """
    Get the current time in a specified timezone.
    
    Args:
        timezone_name: The timezone name (e.g., 'UTC', 'US/Eastern', 'Asia/Tokyo', 'Europe/London')
    
    Returns:
        A formatted string with the current time in the specified timezone
    """
    try:
        # Handle common timezone abbreviations
        timezone_mapping = {
            'EST': 'US/Eastern',
            'PST': 'US/Pacific',
            'GMT': 'GMT',
            'JST': 'Asia/Tokyo',
            'CET': 'Europe/Paris',
            'IST': 'Asia/Kolkata',
            'CST': 'US/Central',
            'MST': 'US/Mountain'
        }
        
        tz_name = timezone_mapping.get(timezone_name.upper(), timezone_name)
        
        tz = pytz.timezone(tz_name)
        
        # Get current time in the specified timezone
        current_time = datetime.now(tz)
        
        # Format the time
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        
        return f"Current time in {timezone_name}: {formatted_time}"
        
    except pytz.exceptions.UnknownTimeZoneError:
        return f"Error: Unknown timezone '{timezone_name}'. Please use a valid timezone like 'UTC', 'US/Eastern', 'Asia/Tokyo', etc."
    except Exception as e:
        return f"Error getting time: {str(e)}"

@tool(category="time", description="Convert time between different timezones")
async def convert_timezone(time_str: str, from_tz: str, to_tz: str) -> str:
    """
    Convert time from one timezone to another.
    
    Args:
        time_str: Time in format "YYYY-MM-DD HH:MM" or "HH:MM"
        from_tz: Source timezone
        to_tz: Target timezone
    
    Returns:
        Converted time with timezone information
    """
    try:
        timezone_mapping = {
            'EST': 'US/Eastern',
            'PST': 'US/Pacific',
            'GMT': 'GMT',
            'JST': 'Asia/Tokyo',
            'CET': 'Europe/Paris',
            'IST': 'Asia/Kolkata',
            'CST': 'US/Central',
            'MST': 'US/Mountain',
            'UTC': 'UTC',
            'dhaka': 'Asia/Dhaka',
            'bangladesh': 'Asia/Dhaka',
        }
        
        from_tz = timezone_mapping.get(from_tz.upper(), from_tz)
        to_tz = timezone_mapping.get(to_tz.upper(), to_tz)
        
        if len(time_str.split()) == 1: 
            today = datetime.now().strftime("%Y-%m-%d")
            time_str = f"{today} {time_str}"
        
        from_timezone = pytz.timezone(from_tz)
        to_timezone = pytz.timezone(to_tz)
        
        dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        

        dt_localized = from_timezone.localize(dt)
        
        dt_converted = dt_localized.astimezone(to_timezone)
        
        result = dt_converted.strftime("%Y-%m-%d %H:%M:%S %Z")
        
        return f"Time conversion: {time_str} {from_tz} → {result}"
        
    except Exception as e:
        return f"Error converting time: {str(e)}. Please use format 'YYYY-MM-DD HH:MM' or 'HH:MM'"
