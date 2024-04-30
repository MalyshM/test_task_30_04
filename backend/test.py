import re

response = [
    {
        "time": "2024-04-30T11:00:00Z",
        "data": {
            "instant": {
                "details": {
                    "air_pressure_at_sea_level": 1028,
                    "air_temperature": 8.3,
                    "cloud_area_fraction": 100,
                    "relative_humidity": 74.4,
                    "wind_from_direction": 190.7,
                    "wind_speed": 1.4
                }
            },
            "next_12_hours": {
                "summary": {
                    "symbol_code": "cloudy"
                },
                "details": {}
            },
            "next_1_hours": {
                "summary": {
                    "symbol_code": "cloudy"
                },
                "details": {
                    "precipitation_amount": 0
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
    {
        "time": "2024-04-30T12:00:00Z",
        "data": {
            "instant": {
                "details": {
                    "air_pressure_at_sea_level": 1028.1,
                    "air_temperature": 9.2,
                    "cloud_area_fraction": 100,
                    "relative_humidity": 73.9,
                    "wind_from_direction": 231,
                    "wind_speed": 1.3
                }
            },
            "next_12_hours": {
                "summary": {
                    "symbol_code": "cloudy"
                },
                "details": {}
            },
            "next_1_hours": {
                "summary": {
                    "symbol_code": "cloudy"
                },
                "details": {
                    "precipitation_amount": 0
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
    {
        "time": "2024-04-30T13:00:00Z",
        "data": {
            "instant": {
                "details": {
                    "air_pressure_at_sea_level": 1027.8,
                    "air_temperature": 9.9,
                    "cloud_area_fraction": 98.8,
                    "relative_humidity": 73.2,
                    "wind_from_direction": 257.5,
                    "wind_speed": 1
                }
            }
        }
    }
]

# Regex pattern to match the desired timestamp
pattern = r"12:00:00Z"

# Filter the response using regex
filtered_data = [item for item in response if re.search(pattern, item["time"])]

# Print the filtered data
print(filtered_data)