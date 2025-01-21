# Import pytest
import pytest

# Import the relevant three functions from the project page
from project import train_station_stops, generate_random_stations, computing_distance

# Testing for the first function train_station_stops
def test_train_station_stops():
    assert train_station_stops("NSL", "Novena", 1) == ["Newton", "Toa Payoh"]
    assert train_station_stops("EWL", "Lakeside", 4) == ["Dover", "Gul Circle"]
    assert train_station_stops("CCL", "Mountbatten", 5) == ["Bartley", "Bras Basah"]
    assert train_station_stops("EWL", "Clementi", 15) == ["Paya Lebar"]
    assert train_station_stops("DTL", "Bukit Panjang", 10) == ["Newton"]
    assert train_station_stops("DTL", "Bukit Panjang", 1000) == []
    assert train_station_stops("NEL", "Punggol Coast", 3) == ["Buangkok"]

    # Catch for the relevant errors:
    # 1. Invalid train line
    # 2. Invalid origin train station/wrong train station

    with pytest.raises(SystemExit):
        train_station_stops("LLL", "Woodlands", 8)
    with pytest.raises(SystemExit):
        train_station_stops("EWL", "Mickey Mouse", 5)
    with pytest.raises(SystemExit):
        train_station_stops("NSL", "Simei", 2)

# Testing for the second function generate_random_stations
def test_generate_random_stations():
    assert len(generate_random_stations("NSL", 5)) == 5
    assert len(generate_random_stations("EWL", 1)) == 1
    assert len(generate_random_stations("DTL", 20)) == 20

    # Catch for the relevant errors:
    # 1. Invalid train line
    # 2. Bad input of number of stations (eg. 0 or a number more than the length of the list of stations)

    with pytest.raises(SystemExit):
        generate_random_stations("COL", 2)
    with pytest.raises(SystemExit):
        generate_random_stations("EWL", 50)
    with pytest.raises(SystemExit):
        generate_random_stations("NEL", 0)

# Testing for the third function computing_distance
def test_computing_distance():
    assert computing_distance("CCL", "Dhoby Ghaut", "Bras Basah") == 1.0
    assert computing_distance("CCL", "Bras Basah", "Dhoby Ghaut") == 1.0
    assert computing_distance("NSL", "Jurong East", "Yew Tee") == 5.3
    assert computing_distance("NSL", "Raffles Place", "Orchard") == 4.3
    assert computing_distance("DTL", "Tampines West", "Tampines East") == 2.4

    # Catch for the relevant errors:
    # 1. Invalid train line
    # 2. Invalid train station one
    # 3. Invalid train station two
    # 4. Identical names of train station one and two

    with pytest.raises(SystemExit):
        computing_distance("PPL", "Bishan", "Somerset")
    with pytest.raises(SystemExit):
        computing_distance("NEL", "Whampoa", "Punggol")
    with pytest.raises(SystemExit):
        computing_distance("EWL", "Commonwealth", "Kranji")
    with pytest.raises(SystemExit):
        computing_distance("CCL", "Stadium", "Stadium")
