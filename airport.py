class Passenger:
    def __init__(self, passenger_id, name, passport):
        self.passenger_id = passenger_id
        self.name = name
        self.passport = passport

    def display(self):
        print(f"Passenger ID: {self.passenger_id}")
        print(f"Name: {self.name}")
        print(f"Passport: {self.passport}")


class Flight:
    def __init__(self, flight_no, source, destination, seats):
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.seats = seats
        self.booked_passengers = []

    def book_seat(self, passenger):
        if len(self.booked_passengers) < self.seats:
            self.booked_passengers.append(passenger)
            print(f"Seat booked for {passenger.name} on Flight {self.flight_no}")
        else:
            print("No seats available!")

    def display_flight(self):
        print(f"\nFlight No: {self.flight_no}")
        print(f"Route: {self.source} -> {self.destination}")
        print(f"Available Seats: {self.seats - len(self.booked_passengers)}")


class Baggage:
    def __init__(self, baggage_id, weight):
        self.baggage_id = baggage_id
        self.weight = weight

    def check_weight(self):
        if self.weight <= 25:
            print("Baggage accepted")
        else:
            print("Excess baggage charges apply")


class AirportManagementSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
        print(f"Flight {flight.flight_no} added successfully")

    def display_all_flights(self):
        print("\nAvailable Flights:")
        for flight in self.flights:
            flight.display_flight()


# Driver Code
if __name__ == "__main__":
    # Airport system
    airport = AirportManagementSystem()

    # Add flights
    f1 = Flight("AI202", "Chennai", "Delhi", 2)
    f2 = Flight("IN305", "Mumbai", "Dubai", 3)

    airport.add_flight(f1)
    airport.add_flight(f2)

    airport.display_all_flights()

    # Passenger booking
    p1 = Passenger(101, "Rahul", "P12345")
    p2 = Passenger(102, "Divya", "P67890")

    f1.book_seat(p1)
    f1.book_seat(p2)

    # Baggage check
    b1 = Baggage("BG101", 20)
    b1.check_weight()

    airport.display_all_flights()