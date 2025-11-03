#Matthew Rozendaal
#10/27/2025
# Module 4: Sitka Highs and Lows with User Input

import csv
from datetime import datetime
from pathlib import Path
import os

def clear_console():
    """
    Clears the console screen based on the operating system.
    """
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

from matplotlib import pyplot as plt

clear_console()
while True:
    # Output to the user the options highs, lows, or exit
    
    print("Please enter a value below to see the corresponding graph:")
    output = input("Enter highs, lows, or exit: ")
    if output.lower() == 'exit':
        print("Exiting the program.")
        exit()
    elif output.lower() != 'highs' and output.lower() != 'lows':
        print("Invalid input. Please try again.")
        clear_console()
        continue;


    # Get the path of the current script
    script_dir = Path(__file__).parent

    # Construct the path to the file in the same directory
    filename = script_dir / 'sitka_weather_2018_simple.csv'
    with open(filename, "r") as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and high temperatures from this file.
        dates, highs, lows = [], [],[]
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)

    # Plot the high temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    if output.lower() == 'lows':
        ax.plot(dates, lows, c='blue')
        plt.title("Daily low temperatures - 2018", fontsize=24)
    else:
        ax.plot(dates, highs, c='red')
        plt.title("Daily high temperatures - 2018", fontsize=24)

    # Format plot.
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
    clear_console()