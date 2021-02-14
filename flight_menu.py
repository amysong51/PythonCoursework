# Flight program menu thingy
# Amy Jones: 30/1/21

# UK airports
airports = []
UK_BOH = 0
UK_LPL = 1

# Airport details
airport_details = []
APORT_CODE = 0
APORT_NAME = 1
APORT_LPL_KM = 2
APORT_BOH_KM = 3

# Aircraft details
aircraft_details = []
ACRFT_TYPE = 0
ACRFT_COST = 1
ACRFT_RANGE = 2
ACRFT_CAPACITY = 3
ACRFT_SEATS = 4

# User data
user_data = [-1, -1, -1, -1, -1]
USR_UK_APORT = 0
USR_OSEAS_APORT = 1
USR_ACRFT_TYPE = 2
USR_NUM_STD_CLASS = 3
USR_NUM_FIRST_CLASS = 4


def print_flight_details(airport):
    print("Thank you, here are your flight details.")
    print(airport_details[airport][APORT_NAME])
    
def print_aircraft_details(aircraft):
    print("Your type of flight craft is",(aircraft_details[aircraft][ACRFT_TYPE]))
    print("The running cost per 100km is £",(aircraft_details[aircraft][ACRFT_COST]))
    print("The maximum flight range(km) is",(aircraft_details[aircraft][ACRFT_RANGE]))
    print("If all seats are full in standard-class the capacity is",(aircraft_details[aircraft][ACRFT_CAPACITY]))
    print("The minimum number of first-class seats, if any, is",(aircraft_details[aircraft][ACRFT_SEATS]),"\n")

def flight_cost_per_seat(distance):
    return int(aircraft_details[user_data[USR_ACRFT_TYPE]][ACRFT_COST]) * distance / 100
    
def flight_cost(cost_per_seat):
    return cost_per_seat * (user_data[USR_NUM_STD_CLASS] + user_data[USR_NUM_FIRST_CLASS])
    
def flight_income(price_first_class_seat, price_std_class_seat):
    return user_data[USR_NUM_FIRST_CLASS] * price_first_class_seat + user_data[USR_NUM_STD_CLASS] * price_std_class_seat
    
def flight_profit(income, cost):
    return income - cost
    

# Main menu loop function definition
def run():

    ans = ""
    
    # Textfile 1-reads,splits and prints. Also a list.
    f = open("flightdetails.txt", "r")
    file = (f.read())
    details = file.split('\n')

    for x in details:
        aircraft_details.append(x.split(','))
    
    # Second textfile-""
    f = open("Airports.txt","r")
    file = (f.read())
    airports = file.split('\n')

    for x in airports:
        airport_details.append(x.split(','))
    
    # Menu-press 5 to quit
    while ans != "5":
    
        print("\nWelcome to the menu!")
        print("Press 1 to Enter Airport Details")
        print("Press 2 to Enter Flight Details")
        print("Press 3 to Enter Price Plan and Calculate Profit")
        print("Press 4 to Clear Data")
        print("Press 5 to Quit\n")
        
        ans = input()
        
        # 1:ENTER AIRPORT DETAILS-asks user to enter their three letter airport code and checks it against the textfile1.
        if ans == "1":
        
            code = str(input("Please enter your three letter UK airport code: "))
            
            # Check for Bournemouth or Liverpool UK airport
            if code == "BOH":
                user_data[USR_UK_APORT] = UK_BOH
            
            elif code == "LPL":
                user_data[USR_UK_APORT] = UK_LPL
                
            else:
                print("Unknown UK Airport.")
                continue

            # Ask the user for the destination airport
            destination = str(input("Please enter the three letter code for the overseas airport: "))
                      
            # Iterate through the list and search for the input string.
            for x in range(len(airport_details)):
                if destination == airport_details[x][APORT_CODE]:
                    print_flight_details(x)
                    user_data[USR_OSEAS_APORT] = x
                    break
                        
            if user_data[USR_OSEAS_APORT] == -1:
                print("Unknown Overseas Airport.")
           
                
        # 2:ENTER FLIGHT DETAILS-Asks for the type of aircraft for your flight e.g.Medium Narrow body AND checks aginst textfile1.
        # If data inputed checks correctly, all details for the flight will be diplayed.
        elif ans == "2":
        
            aircraft_type = str(input("Please enter the type of aircraft for your flight: " ))
            
            # Iterate through the list and search for the input string.
            for x in range(len(aircraft_details)):
                if aircraft_type == aircraft_details[x][ACRFT_TYPE]:
                    print_aircraft_details(x)
                    user_data[USR_ACRFT_TYPE] = x
                                   
                    # Calculation for number of standard class seats
                    min_first_class_seats = int(aircraft_details[x][ACRFT_SEATS])
                    capacity = int(aircraft_details[x][ACRFT_CAPACITY])
            
                    # Check valid input
                    while True:
                        try:
                            num_first_class_seats = int(input("Please input the number of first class seats on the aircraft: "))
                        except ValueError:
                            print("Not an integer! Try again.")
                            continue
                        else:
                            break
                                       
                    num_standard_seats = capacity - num_first_class_seats * 2
            
                    if num_first_class_seats > 0:
                
                        if num_first_class_seats < min_first_class_seats:
                            print("Too few first class seats entered, minimum is...", min_first_class_seats)
                    
                        elif num_first_class_seats > capacity / 2:
                            print("Too many first class seats entered, maximum is...", capacity / 2)

                        else:
                            print("The number of std-class seats on your aircraft is...", num_standard_seats)
                            user_data[USR_NUM_STD_CLASS] = num_standard_seats
                            user_data[USR_NUM_FIRST_CLASS] = num_first_class_seats
               
                    break
             
            if user_data[USR_ACRFT_TYPE] == -1:
                print ("Unknown aircraft type")
                    
            
        # Check user data
        elif ans == "3":
            
            # Checks that a UK airport code has been corectly entered.
            if user_data[USR_UK_APORT] == -1:
                print("Please input a UK airport code before selecting this option.")
            
            # Checks that a Overseas airport code has been corectly entered.
            if user_data[USR_OSEAS_APORT] == -1:
                print("Please input an Overseas airport code before selecting this option.")
                
            # Checks that an aircraft type has been correctly entered.
            if user_data[USR_ACRFT_TYPE] == -1:
                print("Please input an Aircraft Type before selecting this option.")

            # Checks the number of standard class seats has been entered correctly.
            if user_data[USR_NUM_STD_CLASS] == -1:
                print("Please enter the number of standard class seats before selecting this option.")

            result = True
            
            # Check all options are valid before we continue
            for x in range(len(user_data)):
                if user_data[x] == -1:
                    result = False
            
            if result == True:
                
                # Find the max flight range for the selected aircraft.
                max_flight_range = int(aircraft_details[user_data[USR_ACRFT_TYPE]][ACRFT_RANGE])
                
                # Find the source UK airport
                if user_data[USR_UK_APORT] == UK_BOH:
                    source_airport = APORT_BOH_KM
                    
                elif user_data[USR_UK_APORT] == UK_LPL:
                    source_airport = APORT_LPL_KM
                
                # Calculate the total distance
                distance = int(airport_details[user_data[USR_OSEAS_APORT]][source_airport])
               
                # Asks for price of a first class and standard class seat then calculates flight cost per seat, flight cost, flight income and flight profit.
                if max_flight_range >= distance:
                
                    # Enter num std class seats
                    while True:
                        try:
                            price_std_class_seat = int(input("Please enter the price of a standard-class seat: £"))
                        except ValueError:
                            print("Not an integer! Try again.")
                            continue
                        else:
                            break
                            
                    # Enter num first class seats
                    while True:
                        try:
                            price_first_class_seat = int(input("Please enter the price of a first-class seat: £"))
                        except ValueError:
                            print("Not an integer! Try again.")
                            continue
                        else:
                            break
                               
                    # Flight cost per seat CALCULATION
                    cost_per_seat = flight_cost_per_seat(distance)
                    print ("Flight cost per seat: £{:.2f}".format(cost_per_seat))
                
                    # Flight cost CALCULATION
                    cost = flight_cost(cost_per_seat)
                    print("Flight cost: £{:.2f}".format(cost))
                    
                    # Flight income CALCULATION
                    income = flight_income(price_first_class_seat, price_std_class_seat)
                    print ("Flight income: £{:.2f}".format(income))
                    
                    # Flight profit CALCULATION
                    print ("Flight profit: £{:.2f}".format(flight_profit(income, cost)))
                    
                    
                else:
                    print("Error. Your aircraft cannot fly that distance")
                    
        
        # Clear data
        elif ans == "4":
                       
            for x in range(len(user_data)):
                user_data[x] = -1

        # Exit
        elif ans == "5":
            print("Thank you.")
            exit()

        else:
            print("Sorry we didn't quite get that, sending you back to the menu...")

    # End of while loop



run()
