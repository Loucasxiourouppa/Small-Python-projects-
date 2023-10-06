def validate_time(time):
    parts = time.split(":")
    if len(parts) != 2:
        raise ValueError("Invalid time format. Use 'hh:mm'.")

    hours = int(parts[0])
    minutes = int(parts[1])

    if hours < 0 or hours >= 24:
        raise ValueError("Invalid hours. Hours should be between 0 and 23.")
    if minutes < 0 or minutes >= 60:
        raise ValueError("Invalid minutes. Minutes should be between 0 and 59.")

    return hours, minutes

num = int(input("Number of participants? "))
participants = []

for i in range(num):
    name = input("Name: ")
    time = input("Time (hh:mm): ")

    try:
        hours, minutes = validate_time(time)
        participants.append({"Name": name, "Hours": hours, "Minutes": minutes})
    except ValueError as e:
        print("Invalid input:", e)

# Print the participants and their times
print("\nParticipants:")
for participant in participants:
    print(f"Name: {participant['Name']}, Time: {participant['Hours']:02}:{participant['Minutes']:02}")
