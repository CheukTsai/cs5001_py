def main():

    # following code has passed the test
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    # TODO: Fill in the rest of the necessary code here

    # Basic information and formula
    maxHR = 208-0.7*age
    reserve = maxHR - restHR
    
    # print out the heading
    print("=======================================")
    print("Your heart rate reserve is: ", reserve, " bpm")
    print("Here is a breakdown of your training zones: ") 
    
    # zone 1 to 5 all print out similar information, with only numbers changed
    for num in range(1,6):
        
        # in zone 1, 2 and 3, the factors can be calculated in certain formula
        if(num <= 3):
            zoneMinFactor = 0.5+0.1*(num-1)
            zoneMin = round(restHR+zoneMinFactor*reserve, 2)
            zoneMaxFactor = 0.5+0.1*num
            zoneMax = round(restHR+zoneMaxFactor*reserve-0.01, 2)
        
        # in zone 4 and 5, however, would be easier to just directly write out (with the wierd 93%)
        elif(num == 4):
            zoneMinFactor = 0.8
            zoneMin = round(restHR+zoneMinFactor*reserve, 2)
            zoneMaxFactor = 0.93
            zoneMax = round(restHR+zoneMaxFactor*reserve-0.01, 2)
        else:
            zoneMinFactor = 0.93
            zoneMin = round(restHR+zoneMinFactor*reserve, 2)
            zoneMaxFactor = 1.0
            zoneMax = round(restHR+zoneMaxFactor*reserve, 2)

        # print out information each time in the loop                        
        print("Zone ", num, ": ", zoneMin, " to ", zoneMax, " bpm")
main()