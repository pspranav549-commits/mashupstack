# main.py

import json
from datetime import datetime
from tracker import create_record

# Create travel records
records = [
    create_record("London", "Visited museums", "05-06-2022"),
    create_record("Dubai", "Amazing skyscrapers", "18-12-2023"),
    create_record("Sydney", "Loved the beaches", "09-01-2024")
]

# Convert date format
for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(records, indent=4)
print("JSON Output:")
print(json_data)

parsed_records = json.loads(json_data)

print("\nParsed Records (One per line):")
for rec in parsed_records:
    print(f"{rec['city']} | {rec['date']} | {rec['comment']}")