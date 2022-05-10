from booking_details import BookingDetails

def test_flight_or_city():
    assert BookingDetails(or_city='Paris').or_city == "Paris"

def test_flight_dst_city():
    assert BookingDetails(dst_city='London').dst_city == "London"

def test_flight_budget():
    assert BookingDetails(or_city=1000).or_city == 1000
