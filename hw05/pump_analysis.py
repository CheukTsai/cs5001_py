""" Credited by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" The program is to record some important information from a water pump,
utilizing mostly some timer to record some important timing."""

# Basic constants:
GALLON_PER_MINUTE = 2
MINUTES_PER_HOUR = 60.0
HOURS_PER_DAY = 24.0
WATT_TO_KW = 1/1000
CHECKPOINT_5_GALLON = 5
CHECKPOINT_100_GALLON = 100


def main():

    # Needed Variables:
    timer_unstop_minutes = 0  # A timer to record all used time.

    live_minutes = 0  # Timer to collect pump running time.
    minutes_to_reach_5_gallons = 0  # Total time to reach 5 gallons
    minutes_to_reach_100_gallons = 0  # Total time to reach 100 gallons
    watt_minute_total = 0  # Total power used in the unit of watt minute

    softener_recharge_list = []  # List to collect softener recharging data
    softener_recharge_start_point = 0  # A flag to record when softener recharge
    softener_recharge_timer = 0  # Record the duration

    # Make sure file can be found.
    while True:
        try:
            input_file = input("Please enter the file name: ")
            raw_file = open(input_file)
            break
        except FileNotFoundError:
            print("Unable to open", input_file)

    # Read information from raw data txt.
    for line in raw_file:
        watt_that_minute = int(line.rstrip())
        watt_minute_total += watt_that_minute
        timer_unstop_minutes += 1

        # If the energy used that minute is more "near" 0 than 1000, we record that minute as "stop minute",
        # Otherwise, we record that minute as "running/live minute".
        # Here are those which we call "stop minutes"
        if(min(abs(watt_that_minute), abs(1000-watt_that_minute)) == abs(watt_that_minute)):

            if(softener_recharge_timer >= 120):  # Only record constantly running time that is over 120

                # Put the running time into data.
                softener_recharge_list.append(softener_recharge_timer)

                # Put the softener start point into data.
                softener_recharge_list.append(softener_recharge_start_point)

            # Every time it comes to "stop minute", the timer should be reset.
            softener_recharge_timer = 0

        else:
            live_minutes += 1  # Record running time.
            softener_recharge_timer += 1  # Record constantly running time.

        # If recorded water pump data haven't reached the target,
        # The time of timer increments by 1.
        if((live_minutes-1)*GALLON_PER_MINUTE < CHECKPOINT_5_GALLON):
            minutes_to_reach_5_gallons += 1
        if((live_minutes-1)*GALLON_PER_MINUTE < CHECKPOINT_100_GALLON):
            minutes_to_reach_100_gallons += 1

        if(softener_recharge_timer == 1):
            # Every the first minute of the period of "live minutes" may possibly be the start point. Record it.
            softener_recharge_start_point = timer_unstop_minutes

    # Calculate total covering time in hours
    hours = timer_unstop_minutes/MINUTES_PER_HOUR
    # Calculate total covering time in days
    days = round(hours/HOURS_PER_DAY, 3)
    # Calculate total producing water in gallons
    gallons = live_minutes * GALLON_PER_MINUTE
    # Calculate producing water per day in gallons
    gallons_per_day = round(gallons/hours*HOURS_PER_DAY, 3)
    # Calculate total requiring power in kwh
    kwh = round(watt_minute_total * WATT_TO_KW / MINUTES_PER_HOUR, 3)

    # If the target gallon is never reached, record it as -1.
    if(minutes_to_reach_5_gallons == timer_unstop_minutes and gallons < CHECKPOINT_5_GALLON):
        minutes_to_reach_5_gallons = -1
    if(minutes_to_reach_100_gallons == timer_unstop_minutes and gallons < CHECKPOINT_100_GALLON):
        minutes_to_reach_100_gallons = -1

    print("Data covers a total of", hours, "hours")
    print("(That's", days, "days)")
    print("")
    print("Pump was running for", live_minutes,
          "minutes, producing", gallons, "gallons")
    print("(That's", gallons_per_day, "gallons per day)")
    print("")
    print("Pump required a total of", watt_minute_total, "watt minutes of power")
    print("(That's", kwh, "kwh)")
    print("")
    print("It took", minutes_to_reach_5_gallons,
          "minutes of data to reach 5 gallons.")
    print("It took", minutes_to_reach_100_gallons,
          "minutes of data to reach 100 gallons.")
    print("")

    # Only print out the following information when a least a set of data is recorded.
    if(len(softener_recharge_list) != 0):
        print("Information on water softener recharges:")
        index = 0
        while (index < len(softener_recharge_list)):
            # List[index] recording the time,
            # List[index+1] recording the start point.
            recharge_time = softener_recharge_list[index]
            recharge_watt = softener_recharge_list[index+1]
            print(recharge_time, "minute run started at", recharge_watt)
            # Since the data is collected in a 1-dimension list, the index should increment by 2 every time.
            index += 2


main()
