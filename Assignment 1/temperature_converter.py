# CMPR.X416 Python For Programmers
# Module 2: Temperature Conversion Programming Assignment

print('This is a temperature converter.')
print('It converts from/to Fahrenheit, Celsius, and Kelvin units.\n')

while True:
    # White space is removed from user's input.
    ans = input('Enter a temperature(number), or E to exit: ').strip()
    # Exit the loop if input is "E"
    if ans == 'E':
        print('Exiting the temperature converter.')
        break
    # Convert user input from string to float.
    # Python thows ValueError if user input is not a number or a float
    temp = float(ans)
    # Get temperature_FROM value from user
    while True:
        # Remove white space from user input
        temp_from = input('Enter FROM temperature unit:[Cc/Ff/Kk] ').strip()
        # Only allow 'C', 'c' , 'F', 'f', 'K' , 'k' as user input.
        # Throw error otherwise and repeat loop until correct user input
        if temp_from not in 'CcFfKk' or len(temp_from) != 1:
            print(f"  [ERROR] Invalid temperature unit: '{temp_from}'")
            print('  Valid choices are:[Cc/Ff/Kk]\n')
            continue
        break
    # Get temperature_TO value from user
    while True:
        # Remove white space from user input
        temp_to = input('Enter TO temperature unit:[Cc/Ff/Kk] ').strip()
        # Only allow 'C', 'c' , 'F', 'f', 'K' , 'k' as user input.
        # Throw error otherwise and repeat loop until correct user input
        if temp_to not in 'CcFfKk' or len(temp_to) != 1:
            print(f"  [ERROR] Invalid temperature unit: '{temp_to}'")
            print('  Valid choices are:[Cc/Ff/Kk]\n')
            continue
        break
    # Temperature Conversion Logic
    # All answers printed with 2 decimal places and formated to float
    if temp_from in 'Cc':
        if temp_to in 'Cc':
            print(f"{temp:.2f}C = {temp:.2f}C\n")
        elif temp_to in 'Ff':
            print(f"{temp:.2f}C = {temp * (9 / 5) + 32:.2f}F\n")
        else:
            print(f"{temp:.2f}C = {temp + 273.15:.2f}K\n")
    elif temp_from in 'Kk':
        if temp_to in 'Kk':
            print(f"{temp:.2f}K = {temp:.2f}K\n")
        elif temp_to in 'Ff':
            print(f"{temp:.2f}K = {temp * (9 / 5) - 459.67:.2f}F\n")
        else:
            print(f"{temp:.2f}K = {temp - 273.15:.2f}C\n")
    else:
        if temp_to in 'Ff':
            print(f"{temp:.2f}F = {temp:.2f}F\n")
        elif temp_to in 'Cc':
            print(f"{temp:.2f}F = {(temp - 32) * (5 / 9):.2f}C\n")
        else:
            print(f"{temp:.2f}F = {(temp + 459.67) * (5 / 9):.2f}K\n")
