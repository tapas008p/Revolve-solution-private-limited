import pytest
from analysis import *

def test1():
    result = total_number_of_days_flight_data_cover()
    assert result == 365

def test2():
    result = number_of_departure_cities()
    assert result == 2

def test3():
    result = manufacturer_with_most_delays()
    assert result == 'EMBRAER'

def test4():
    result = two_most_connected_cities()
    assert result == 'New York-Chicago'