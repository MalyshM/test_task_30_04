import math
import re

from fastapi import APIRouter
from starlette import status
from geopy.geocoders import Nominatim
from starlette.exceptions import HTTPException

from util import get_request

yr_no_API_router = APIRouter(tags=["yr.no API"])


@yr_no_API_router.get('/api/temperature_by_location', name='yr.no API:temperature_by_location',
                      status_code=status.HTTP_200_OK,
                      description=
                      """
                              Получает name_str: str = None, long: float = None, lat: float = None,
                              Returns:
                                  json, list of dicts
                              \n
                              [
                                  {
                                    "time": "2024-04-30T12:00:00Z", - время
                                    "data": {
                                      "instant": {
                                        "details": {
                                          "air_pressure_at_sea_level": 1028.5, - давление воздуха на уровне моря
                                          "air_temperature": 20.7, - температура воздуха
                                          "cloud_area_fraction": 76.6, - облачность
                                          "relative_humidity": 37.9, - Относительная влажность
                                          "wind_from_direction": 269.4, - направление воздуха
                                          "wind_speed": 7.5 - скорость ветра
                                        }
                                      },
                                      "next_12_hours": {
                                        "summary": {
                                          "symbol_code": "partlycloudy_day" - статус дня
                                        },
                                        "details": {}
                                      },
                                      "next_1_hours": {
                                        "summary": {
                                          "symbol_code": "partlycloudy_day"
                                        },
                                        "details": {
                                          "precipitation_amount": 0 - количество_осадков
                                        }
                                      },
                                      "next_6_hours": {
                                        "summary": {
                                          "symbol_code": "partlycloudy_day"
                                        },
                                        "details": {
                                          "precipitation_amount": 0
                                        }
                                      }
                                    }
                                  },
                      """)
async def get_temperature_by_location(name_str: str = None, long: float = None, lat: float = None):
    try:
        if name_str is not None:
            geolocator = Nominatim(user_agent="Tester")
            location = geolocator.geocode(name_str)
            long = location.longitude
            lat = location.latitude
        if long is None or lat is None or math.isnan(long) or math.isnan(lat):
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail="Широта или долгота не указаны")
        resp = await get_request(
            f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={round(lat, 2)}&lon={round(long, 2)}")
        filtered_data = [item for item in resp['properties']['timeseries'] if re.search(r"12:00:00Z", item["time"])]
        return filtered_data
    except Exception as e:
        raise e
