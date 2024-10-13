import json
from datetime import datetime

class Flights:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        try:
            with open(filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            pass

    def add_flight(self, origin, destination, flight_number, departure, next_day, arrival):
        try:
            datetime.strptime(departure, '%H%M')
            datetime.strptime(arrival, '%H%M')
        except ValueError:
            return False

        self.data.append({
            "origin": origin,
            "destination": destination,
            "flight_number": flight_number,
            "departure": departure,
            "next_day": next_day,
            "arrival": arrival
        })

        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

        return True

    def get_flights(self):
        formatted_flights = []
        for flight in self.data:
            dep_time_obj = datetime.strptime(flight["departure"], '%H%M')
            arr_time_obj = datetime.strptime(flight["arrival"], '%H%M')
            duration = (arr_time_obj - dep_time_obj).seconds // 60

            hours = duration // 60
            minutes = duration % 60
            formatted_arrival = arr_time_obj.strftime('%I:%M%p').lstrip('0').lower()

            if flight["next_day"] == 'Y':
                formatted_arrival = f"+{formatted_arrival}"

            formatted_flights.append({
                "origin": flight["origin"],
                "destination": flight["destination"],
                "flight_number": flight["flight_number"],
                "departure": dep_time_obj.strftime('%I:%M%p').lstrip('0').lower(),
                "arrival": formatted_arrival,
                "duration": f"{hours}:{minutes:02d}"
            })

        return formatted_flights

#Small error - If a flight for example leaves at 10 and arrives at 11 the next
#day, it shows 1 hour instead of 25 hours. 
#Hint: add another if statement with import timedelta
