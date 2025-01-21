# YOUR PROJECT TITLE
#### Video Demo: https://youtu.be/r0tZqfJ4OgE
#### Description:

This code implements a comprehensive journey planning system for Singapore's MRT (Mass Rapid Transit) rail network. The program focuses on five major lines: North-South Line (NSL), East-West Line (EWL), North-East Line (NEL), Downtown Line (DTL), and Circle Line (CCL). For simplicity, it excludes the newer Thomson East-Coast Line and some EWL extensions.

The program begins by initializing extensive data structures that represent the MRT network. Each line is represented by two parallel arrays: one containing the station names in sequential order, and another containing the distances (in kilometers) between adjacent stations. This data organization allows for accurate distance calculations and station identification along each line.

The main interface is implemented through a command-line menu system that presents users with four options: finding train station stops, generating random stations, calculating distances between stations, or exiting the program. The interface includes robust error handling for invalid inputs, ensuring users can only enter valid numeric choices between 1 and 4.

The first major function, train_station_stops, helps users identify stations that are a specific number of stops away from their current location. Given a train line, origin station, and number of stops, it calculates possible destinations in both directions along the line. For example, if a user is at City Hall on the EWL and wants to know stations 7 stops away, it will return stations in both directions, sorted alphabetically. The function includes validation to ensure both the train line and origin station exist.

The generate_random_stations function provides a way for users to get a random selection of stations from a specified line. This could be useful for exploration or planning various journey scenarios. The function takes a train line name and the desired number of stations as input. It uses Python's random.sample() function to ensure stations are selected without replacement, meaning no station will be repeated in the output. The function includes checks to prevent users from requesting more stations than exist on the line.

The third major function, computing_distance, calculates the total distance between any two stations on the same line. It works by summing up the individual distances between adjacent stations along the route. The function can calculate distances regardless of whether the journey is in the "forward" or "reverse" direction along the line. This is particularly useful for journey planning and estimating travel times.

Each function includes comprehensive error handling. For instance, if a user enters a non-existent train line or station, the program will exit with an appropriate error message rather than attempting to process invalid data. Similarly, if a user tries to calculate the distance between the same station twice, the program will prompt them to enter two different stations.

The program uses a modular design where the main data structures (station lists and distances) are separated from the logic functions. This makes it easier to maintain and update the system, particularly if new stations are added to existing lines or if distance data needs to be modified.

The code demonstrates good programming practices by including clear comments and examples throughout. For instance, the train_station_stops function includes example cases showing expected inputs and outputs, making it easier for other developers to understand how the function should behave.

The system is designed to be user-friendly while maintaining accuracy in its calculations. All user inputs are stripped of leading and trailing whitespace to prevent matching errors, and the program provides clear feedback for all operations. While it focuses on individual lines rather than interchanges between lines, it provides a solid foundation for understanding and navigating Singapore's MRT system.
