from pages.home_page import HomePage
from faker import Faker
import random

fake = Faker()

def purchaseEndToEnd(deptCity=None, desCity=None, flightSeq=None):
    cities = ["Boston", "Berlin", "Paris", "Dubai", "Mumbai", "Buenos Aires"]

    # Randomize inputs if not provided
    deptCity = deptCity if deptCity else random.choice(cities)
    desCity = desCity if desCity else random.choice(cities)
    flightSeq = flightSeq if flightSeq is not None else random.randint(1, 5)

    # Validate inputs
    if deptCity not in cities or desCity not in cities or flightSeq < 1:
        raise ValueError("Invalid input provided!")

    print(f"Booking flight from {deptCity} to {desCity}, flight number {flightSeq}")

    # Initialize page object
    home = HomePage()
    home.enter_from(deptCity)
    home.enter_to(desCity)
    home.select_flight(flightSeq)

    # Generate dummy user data
    user_data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number()
    }
    print(f"Using user data: {user_data}")

    home.enter_passenger_details(user_data)
    home.make_payment()

    # Validation
    status = home.get_status()
    price = home.get_price()

    assert status == "PendingCapture", f"Status validation failed! Got: {status}"
    assert price > 100.0, f"Price validation failed! Got: {price}"

    print("Purchase successful ✅")
