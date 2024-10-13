from flights import Flights

filename = "flight_schedule.json"
flights = Flights(filename)
    
while True:
    print("\n*** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU")
    print("1. Add flight")
    print("2. Print flight schedule")
    print("3. Set flight schedule filename")
    print("4. Exit the program")

    choice = input("\nEnter menu choice: ")
        
    if choice == "1":
        origin = input("\nEnter origin: ")
        destination = input("Enter destination: ")
        flight_number = input("Enter flight number: ")
        departure = input("Enter departure time (HHMM): ")
        arrival = input("Enter arrival time (HHMM): ")
        next_day = input("Is arrival next day (Y/N): ")
            
        if flights.add_flight(origin, destination, flight_number, departure, next_day, arrival):
            pass
        else:
            print("Invalid Input")
        
    elif choice == "2":
        print()
        print("================== FLIGHT SCHEDULE ==================")
        print("Origin Destination Number Departure Arrival  Duration")
        print("====== =========== ====== ========= ======== ========")
        for flight in flights.get_flights():
            print("{origin:<6} {destination:<11} {flight_number:>6} {departure:>9} {arrival:>8} {duration:>8}".format(**flight))
        
    elif choice == "3":
        filename = input("Enter new flight schedule filename: ")
        flights = Flights(filename)

    elif choice == "4":
        break
        
    else:
        print("Invalid choice")
