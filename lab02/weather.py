import statistics
# data was collected from Feb.2nd to Feb.11th, from the website.

# for the 1st question, 
# I chose to pick out the highest and lowest temperature in the 10 days.
# Naming rule: highest temperature of day x will tempFebxh
# lowest temperature of day x will tempFebxl

tempFeb2l = 39.0
tempFeb3l = 47.0
tempFeb3h = 40.0
tempFeb4l = 46.0
tempFeb4h = 42.0
tempFeb5l = 49.0
tempFeb5h = 40.0
tempFeb6l = 48.0
tempFeb6h = 39.0
tempFeb7l = 47.0
tempFeb7h = 38.0
tempFeb8l = 46.0
tempFeb8h = 36.0
tempFeb9l = 46.0
tempFeb9h = 37.0
tempFeb10l = 47.0
tempFeb10h = 38.0
tempFeb11l = 46.0
tempFeb11h = 38.0

tempHighiest = max(tempFeb3h, tempFeb4h, tempFeb5h, tempFeb6h, tempFeb7h, tempFeb8h, tempFeb9h, tempFeb10h, tempFeb11h)
tempLowest = max(tempFeb2l, tempFeb3l, tempFeb4l, tempFeb5l, tempFeb6l, tempFeb7l, tempFeb8l, tempFeb9l, tempFeb10l, tempFeb11l)
print("1. the difference between the highest and the lowest temperature values predicted for the 10 day forecast is", tempHighiest - tempLowest, "degree fahrenheit")

# for the 2nd question, 
# all the temperatures below are picked at noon.
#Naming rule: highest temperature of day x at noon will tempFebxn

tempFeb2n = 38.0
tempFeb3n = 42.0
tempFeb4n = 40.0
tempFeb5n = 45.0
tempFeb6n = 41.0
tempFeb7n = 43.0
tempFeb8n = 41.0
tempFeb9n = 40.0
tempFeb10n = 40.0
tempFeb11n = 41.0
print("2. the average temperature at noon predicted for the 10 day forecast will be", statistics.mean([tempFeb2n, tempFeb3n, tempFeb4n, tempFeb5n, tempFeb6n, tempFeb7n, tempFeb8n, tempFeb9n, tempFeb10n, tempFeb11n]), "degree fahrenheit")

# for the 3rd question, 
# from Fahrenheit to Celsius, we need to use a specific formula
base = 9.0/5.0
numberAdded = 32.0
print("3. the highest temperature predicted for the 10 day forecast, converted from Fahrenheit to Celsius is ", (tempHighiest-32)/base)

