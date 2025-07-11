from typing import Any
import requests_cache
import openmeteo_requests
from retry_requests import retry
import pandas as pd
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def get_weather_data(latitude: float, longitude: float) -> Any:
    """
    Fetch hourly temperature data for a given location using Open-Meteo API.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.

    Returns:
        dict or list: Weather data or error message.
    """
    try:
        session = retry(requests_cache.CachedSession('.cache', expire_after=3600), retries=5, backoff_factor=0.2)
        client = openmeteo_requests.Client(session=session)

        responses = client.weather_api(
            url="https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "hourly": "temperature_2m",
                "temperature_unit": "celsius",
                "forecast_days": 1
            }
        )

        response = responses[0]
        # Process hourly data. The order of variables needs to be the same as requested.
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {"date": pd.date_range(
            start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
            end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        )}

        hourly_data["temperature_2m"] = hourly_temperature_2m

        hourly_dataframe = pd.DataFrame(data = hourly_data)

        return hourly_dataframe.to_dict(orient="records")

    except Exception as e:
        return {"error": str(e)}




if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')