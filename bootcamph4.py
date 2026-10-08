Web_Development = ["rahul","glen","sajith"]
Data_Science = ["abhid","yasir","yaseen"]
UI_UX_Design = ["ferdin","anzif","vishu"]
print("1",Web_Development)
print("2",Data_Science)
print("3",UI_UX_Design)
all_participants = [Web_Development,Data_Science,UI_UX_Design]
print("4",all_participants)
Web_Development.append("neha")
print("5",Web_Development)
Data_Science.insert(1 ,"akshy")
print("6",Data_Science)
UI_UX_Design.pop
print("7",UI_UX_Design)
new_data_science = Data_Science.copy()
Data_Science.clear()
print("8",new_data_science)
print("9",Web_Development[:2])
lengths = [len(x) for x in new_data_science]
print("10",lengths)
if "asha" in Web_Development or "asha" in new_data_science or "asha" in UI_UX_Design:
    print("true")
else:
    print("false")
first_participants = (Web_Development[0], Data_Science[0], UI_UX_Design[0])
print(first_participants)