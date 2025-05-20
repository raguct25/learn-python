from datetime import datetime
import pytz

# Original log string
log_time_str = "Thu May 15 2025 11:35:09 UTC+0000"

# Parse the string to datetime
dt_utc = datetime.strptime(log_time_str, "%a %b %d %Y %H:%M:%S %Z%z")

# Convert to IST
india_tz = pytz.timezone("Asia/Kolkata")
dt_ist = dt_utc.astimezone(india_tz)

print("UTC :", dt_utc.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
print("IST :", dt_ist.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
