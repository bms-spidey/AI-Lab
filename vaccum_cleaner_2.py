def vacuum_cleaner(position, room_a, room_b):
    if position == "A":
        if room_a == "DIRTY":
            print("SUCK")
            room_a = "CLEAN"

        print("MOVE RIGHT")
        position = "B"

        if room_b == "DIRTY":
            print("SUCK")
            room_b = "CLEAN"
    else:
        if room_b == "DIRTY":
            print("SUCK")
            room_b = "CLEAN"

        print("MOVE LEFT")
        position = "A"

        if room_a == "DIRTY":
            print("SUCK")
            room_a = "CLEAN"

    print("STOP")
    print("\nFinal State:")
    print("Room A:", room_a)
    print("Room B:", room_b)
    print("Final Vacuum Position:", position)  # Added to show final position


# --- Get User Inputs ---

# Get and validate initial position
start_position = input("Enter initial vacuum position (A or B): ").strip().upper()
while start_position not in ["A", "B"]:
    start_position = input("Invalid input. Enter 'A' or 'B': ").strip().upper()

# Get and validate Room A status
status_a = input("Enter status of Room A (DIRTY or CLEAN): ").strip().upper()
while status_a not in ["DIRTY", "CLEAN"]:
    status_a = input("Invalid status. Enter 'DIRTY' or 'CLEAN': ").strip().upper()

# Get and validate Room B status
status_b = input("Enter status of Room B (DIRTY or CLEAN): ").strip().upper()
while status_b not in ["DIRTY", "CLEAN"]:
    status_b = input("Invalid status. Enter 'DIRTY' or 'CLEAN': ").strip().upper()

print("\n--- Running Vacuum Simulation ---")
# Run the simulation with user inputs
vacuum_cleaner(start_position, status_a, status_b)
