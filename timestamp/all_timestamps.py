from datetime import datetime

# Define a list of common timestamp formats
timestamp_formats = [
    "%Y-%m-%d",           # 2024-08-01
    "%Y/%m/%d",           # 2024/08/01
    "%Y.%m.%d",           # 2024.08.01
    "%d-%m-%Y",           # 01-08-2024
    "%d/%m/%Y",           # 01/08/2024
    "%d.%m.%Y",           # 01.08.2024
    "%B %d, %Y",          # August 01, 2024
    "%b %d, %Y",          # Aug 01, 2024
    "%d %B %Y",           # 01 August 2024
    "%d %b %Y",           # 01 Aug 2024
    "%A, %B %d, %Y",      # Thursday, August 01, 2024
    "%a, %b %d, %Y",      # Thu, Aug 01, 2024
    "%Y-%m-%d %H:%M:%S",  # 2024-08-01 14:30:59
    "%d/%m/%Y %H:%M:%S",  # 01/08/2024 14:30:59
    "%I:%M %p",           # 02:30 PM
    "%H:%M:%S",           # 14:30:59
    "%Y-%m-%dT%H:%M:%SZ", # 2024-08-01T14:30:59Z (ISO 8601)
    "%Y-%m-%d %H:%M:%S.%f", # 2024-08-01 14:30:59.123456 (Microseconds)
]

# Get the current datetime
current_datetime = datetime.now()

# Display the current time in various formats
print("Current date and time in various formats:\n")
for fmt in timestamp_formats:
    formatted_date = current_datetime.strftime(fmt)
    print(f"Format: {fmt} => {formatted_date}")

# Example: Parse a date string using a specific format
date_string = "2024-08-01 14:30:59"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("\nParsed Date from string:", parsed_date)
