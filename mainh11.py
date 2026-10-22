import json
from datetime import datetime
from trackerh11sub import get_record

records = [
    get_record("Paris", "Visited the Eiffel Tower", "05-06-2022"),
    get_record("London", "Visited Big Ben", "15-07-2023"),
    get_record("Tokyo", "Enjoyed Japanese food", "20-08-2024")
]

for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(records, indent=4)
print("JSON Data:")
print(json_data)

parsed_records = json.loads(json_data)

print("\nTravel Records:")
for record in parsed_records:
    print(record)

