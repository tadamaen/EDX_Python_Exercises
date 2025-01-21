# Singapore MRT Line Travelling Plan (Simplified)

# Import the necessary packages
import sys
import random

# Step 1: Create a list of all the MRT stations from their respective lines

# 1st MRT Line: North-South Line (NSL)
mrt_stations_NSL = ["Jurong East", "Bukit Batok", "Bukit Gombak", "Choa Chu Kang", "Yew Tee", "Kranji", "Marsiling",
                    "Woodlands", "Admiralty", "Sembawang", "Canberra", "Yishun", "Khatib", "Yio Chu Kang",
                    "Ang Mo Kio", "Bishan", "Braddell", "Toa Payoh", "Novena", "Newton", "Orchard", "Somerset",
                    "Dhoby Ghaut", "City Hall", "Raffles Place", "Marina Bay", "Marina South Pier"]

# 2nd MRT Line: East-West Line (EWL)
mrt_stations_EWL = ["Pasir Ris", "Tampines", "Simei", "Tanah Merah", "Bedok", "Kembangan", "Eunos", "Paya Lebar",
                    "Aljunied", "Kallang", "Lavender", "Bugis", "City Hall", "Raffles Place", "Tanjong Pagar",
                    "Outram Park", "Tiong Bahru", "Redhill", "Queenstown", "Commonwealth", "Buona Vista", "Dover",
                    "Clementi", "Jurong East", "Chinese Garden", "Lakeside", "Boon Lay", "Pioneer", "Joo Koon",
                    "Gul Circle", "Tuas Crescent", "Tuas West Road", "Tuas Link"]

# 3rd MRT Line: North-East Line (NEL)
mrt_stations_NEL = ["HarbourFront", "Outram Park", "Chinatown", "Clarke Quay", "Dhoby Ghaut", "Little India",
                    "Farrer Park", "Boon Keng", "Potong Pasir", "Woodleigh", "Serangoon", "Kovan", "Hougang",
                    "Buangkok", "Sengkang", "Punggol", "Punggol Coast"]

# 4th MRT Line: Downtown Line (DTL)
mrt_stations_DTL = ["Bukit Panjang", "Cashew", "Hillview", "Hume", "Beauty World", "King Albert Park", "Sixth Avenue",
                    "Tan Kah Kee", "Botanic Gardens", "Stevens", "Newton", "Little India", "Rochor", "Bugis",
                    "Promenade", "Bayfront", "Downtown", "Telok Ayer", "Chinatown", "Fort Canning", "Bencoolen",
                    "Jalan Besar", "Bendemeer", "Geylang Bahru", "Mattar", "MacPherson", "Ubi", "Kaki Bukit",
                    "Bedok North", "Bedok Reservoir", "Tampines West", "Tampines", "Tampines East", "Upper Changi",
                    "Expo"]

# 5th MRT Line: Circle Line (CCL)
mrt_stations_CCL = ["Dhoby Ghaut", "Bras Basah", "Esplanade", "Promenade", "Nicoll Highway", "Stadium", "Mountbatten",
                    "Dakota", "Paya Lebar", "MacPherson", "Tai Seng", "Bartley", "Serangoon", "Lorong Chuan",
                    "Bishan", "Marymount", "Caldecott", "Botanic Gardens", "Farrer Road", "Holland Village",
                    "Buona Vista", "one-north", "Kent Ridge", "Haw Par Villa", "Pasir Panjang", "Labrador Park",
                    "Telok Blangah", "HarbourFront"]

# 6th MRT Line, Thomson East-Coast Line (TEL) is excluded for simplicity
# The EWL extension has also been excluded for simplicity

# Step 2: Lists to store the distances between the two train stations

# Distances for East-West Line (NSL)
distances_NSL = [1.2, 1.1, 1.4, 1.6, 1.3, 1.5, 1.2, 1.0, 1.8, 1.4, 1.3, 1.6, 1.4, 1.3, 1.5, 1.2, 1.1, 1.3, 1.4, 1.2,
                 1.3, 1.0, 1.1, 0.9, 1.0, 0.8]

# Distances for East-West Line (EWL)
distances_EWL = [1.4, 1.2, 1.5, 1.3, 1.0, 1.1, 1.4, 1.2, 1.1, 1.0, 1.5, 1.0, 1.1, 1.3, 1.2, 1.4, 1.0, 1.1, 1.2, 1.3,
                 1.2, 1.1, 1.5, 1.3, 1.0, 1.0, 1.4, 1.2, 1.1, 1.4, 1.3, 1.2]

# Distances for North-East Line (NEL)
distances_NEL = [1.0, 0.8, 1.1, 1.0, 1.3, 1.2, 1.4, 1.3, 1.2, 1.4, 1.1, 1.2, 1.3, 1.1, 1.5, 1.6]

# Distances for Downtown Line (DTL)
distances_DTL = [1.2, 1.1, 1.4, 1.0, 1.5, 1.0, 1.2, 1.3, 1.2, 1.0, 1.4, 1.1, 1.3, 1.2, 1.1, 1.3, 1.0, 1.0, 1.5, 1.2,
                 1.4, 1.3, 1.1, 1.2, 1.4, 1.3, 1.1, 1.5, 1.2, 1.3, 1.0, 1.4, 1.2, 1.5]

# Distances for Circle Line (CCL)
distances_CCL = [1.0, 1.1, 1.2, 1.0, 1.3, 1.2, 1.4, 1.1, 1.0, 1.2, 1.1, 1.3, 1.4, 1.2, 1.3, 1.0, 1.1, 1.2, 1.3, 1.4,
                 1.2, 1.3, 1.1, 1.2, 1.0, 1.3, 1.0]

# The main function to test all the three functions
def main():

    # Give the user an introduction: Select Options
    print(
        "Choose an option:\n"
        "1. Find your train station stops\n"
        "2. Generate random train stations\n"
        "3. Calculate the distance between two stations\n"
        "4. Exit"
    )
    try:
        # Prompt the user for the option number he/she wants
        function_number = int(input("Type 1, 2, 3, or 4: "))

        # Simply exit the program if the user chooses option 4
        if function_number == 4:
            print("Exiting program. Goodbye!")
            sys.exit()

        # Handle the three functions respectively depending on the input the user gives

        # Tests for the train_station_stops function
        elif function_number == 1:
            user_input_line = input("Train Line? ").strip()
            user_input_origin_station = input("Which Station Are You At? ").strip()
            try:
                user_input_num_stops = int(input("How Many Stops Do You Want To Go? "))
                possible_stations = train_station_stops(user_input_line, user_input_origin_station, user_input_num_stops)
                print(f"Possible stations: {possible_stations}")
            except ValueError:
                print("Please enter a valid number of stops.")

        # Tests for the generate_random_stations function
        elif function_number == 2:
            user_input_line = input("Train Line? ").strip()
            try:
                number_of_stations = int(input("How Many Stations Do You Want? "))
                train_choice = generate_random_stations(user_input_line, number_of_stations)
                print(f"Random train stations: {train_choice}")
            except ValueError:
                print("Please enter a valid number of stations.")

        # Tests for the computing_distance function
        elif function_number == 3:
            user_input_line = input("Train Line? ").strip()
            first_train_station = input("First Train Station? ").strip()
            second_train_station = input("Second Train Station? ").strip()
            total_distance = computing_distance(user_input_line, first_train_station, second_train_station)
            print(f"Total distance: {total_distance} km")

        # If the user keys in an invalid option (not 1, 2, 3 or 4)
        else:
            print("Invalid option. Please select a valid number.")

    # Similar to the case above - bad inputs like strings
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")

# First function - Obtaining the station names from X number of stops away from the original train station

# Example 1:  Initial train line: EWL
#             Initial train station: City Hall
#             User wants to determine the train station 7 stops away from City Hall
#             Expected Result: ['Commonwealth', 'Kembangan'] -> sorted list in alphabetical order

# Example 2:  Initial train line: NSL
#             Initial train station: Bukit Batok
#             User wants to determine the train station 5 stops away from Bukit Batok
#             Expected Result: ['Marsling'] (only 1 train station)

# If train station input not in list/no such line, sys.exit immediately
# Example 3:  Initial train line: NEL
#             Initial train station: Whampoa
#             User wants to determine the train station 3 stops away from Whampoa
#             Expected Result: Train station does not exist

def train_station_stops(train_line, origin, num_stops):

    # For invalid train lines
    if train_line not in ["NSL", "EWL", "NEL", "DTL", "CCL"]:
        sys.exit("Train Line Does Not Exist")

    # For valid train lines (obtain the list of the train line respectively)
    elif train_line == "NSL":
       interested_ls = mrt_stations_NSL
    elif train_line == "EWL":
       interested_ls = mrt_stations_EWL
    elif train_line == "NEL":
       interested_ls = mrt_stations_NEL
    elif train_line == "DTL":
       interested_ls = mrt_stations_DTL
    else:
       interested_ls = mrt_stations_CCL

    # Check for the validness of the origin station the user has given
    if origin not in interested_ls:
        sys.exit("Train Station does not exist")

    # For valid origin train station
    else:
        # Obtain the index of the origin train station
        index_origin = interested_ls.index(origin)

        # To store all the possible train stations in the list
        stations_ls = []

        # Get the left and right indexes of the selected train stations
        index_left = index_origin - num_stops
        if index_left < 0:
            stations_ls.append("")
        else:
            stations_ls.append(interested_ls[index_left])

        index_right = index_origin + num_stops
        if index_right > len(interested_ls) - 1:
            stations_ls.append("")
        else:
            stations_ls.append(interested_ls[index_right])

        # Remove all the empty strings "" in the list (for index overshooting cases)
        filtered_list = [station for station in stations_ls if station != ""]

        # Sort the list alphabetically by train station name
        filtered_list.sort()
        return filtered_list

# Second Function - Generating random train stations from user input of train line and number of stations to generate
def generate_random_stations(train_line, number_stations):

    # For invalid train lines
    if train_line not in ["NSL", "EWL", "NEL", "DTL", "CCL"]:
        sys.exit("Train Line Does Not Exist")

    # For bad inputs of number_stations (eg: 0)
    if number_stations == 0:
        sys.exit("Please choose 1 or more stations")

    # For valid train lines (obtain the list of the train line respectively)
    elif train_line == "NSL":
       interested_ls = mrt_stations_NSL
    elif train_line == "EWL":
       interested_ls = mrt_stations_EWL
    elif train_line == "NEL":
       interested_ls = mrt_stations_NEL
    elif train_line == "DTL":
       interested_ls = mrt_stations_DTL
    else:
       interested_ls = mrt_stations_CCL

    # Prompt the user for the input of the number_stations
    # Sample the list without replacement
    try:
        stations_selected = random.sample(interested_ls, number_stations)

    # If the number of stations user inputted exceeds the length of the list
    except ValueError:
        sys.exit("You have chosen too many stations")

    return stations_selected

# Third Function - Compute the total distance between two stations from a train line
def computing_distance(train_line, train_station_one, train_station_two):

    # For invalid train lines
    if train_line not in ["NSL", "EWL", "NEL", "DTL", "CCL"]:
        sys.exit("Train Line Does Not Exist")

    # For valid train lines (obtain the lists of the train line and distance respectively)
    elif train_line == "NSL":
       interested_ls = mrt_stations_NSL
       interested_dist = distances_NSL
    elif train_line == "EWL":
       interested_ls = mrt_stations_EWL
       interested_dist = distances_EWL
    elif train_line == "NEL":
       interested_ls = mrt_stations_NEL
       interested_dist = distances_NEL
    elif train_line == "DTL":
       interested_ls = mrt_stations_DTL
       interested_dist = distances_DTL
    else:
       interested_ls = mrt_stations_CCL
       interested_dist = distances_CCL

    # If the user inputs wrong train stations (can be non-existent or station from the wrong line)
    if train_station_one not in interested_ls or train_station_two not in interested_ls:
        sys.exit("Train Station Does Not Exist")

    # For valid train station inputs
    else:
        # Set the initial distance to 0
        distance = 0

        # Obtain the indexes of the two train stations selected
        index_first = interested_ls.index(train_station_one)
        index_second = interested_ls.index(train_station_two)

        # Two possible cases: index_first < index_second or vice versa
        # Can be travelling in both directions
        if index_first < index_second:
            for i in range(index_first, index_second):
                distance = distance + interested_dist[i]
            return distance
        elif index_first > index_second:
            for j in range(index_second, index_first):
                distance = distance + interested_dist[j]
            return distance

        # This case targets the user inputting the same train station twice, which is invalid
        else:
            sys.exit("Please Enter Two Different Train Stations")


if __name__ == "__main__":
    main()
