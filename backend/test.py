from datetime import datetime, timedelta

# Sample data
data = [
  {
    "time": "2024-05-15T10:00:00",
    "data": 12.4
  },
  {
    "time": "2024-05-15T11:00:00",
    "data": 12.4
  },
  {
    "time": "2024-05-15T12:00:00",
    "data": 12.6
  },
  {
    "time": "2024-05-16T10:00:00",
    "data": 13.5
  },
  {
    "time": "2024-05-16T11:00:00",
    "data": 13.9
  },
  {
    "time": "2024-05-16T12:00:00",
    "data": 13.7
  },
  {
    "time": "2024-05-17T12:00:00",
    "data": 17.4
  },
  {
    "time": "2024-05-18T12:00:00",
    "data": 13.7
  },
  {
    "time": "2024-05-19T12:00:00",
    "data": 15.7
  },
  {
    "time": "2024-05-20T12:00:00",
    "data": 17.5
  },
  {
    "time": "2024-05-21T12:00:00",
    "data": 21.6
  },
  {
    "time": "2024-05-22T12:00:00",
    "data": 21.5
  },
  {
    "time": "2024-05-23T12:00:00",
    "data": 23
  }
]

interpolated_data = []

# Interpolate time and data
for entry in data:
    current_time = datetime.fromisoformat(entry["time"])
    previous_time = current_time - timedelta(hours=1)
    interpolated_entry = {
        "time": previous_time.isoformat()[:-6] + "",
        "data": (entry["data"] + entry["data"] - interpolated_data[-1]["data"]) / 2 if interpolated_data else entry["data"]
    }
    interpolated_data.append(interpolated_entry)

# Print interpolated data
for entry in interpolated_data:
    print(entry)