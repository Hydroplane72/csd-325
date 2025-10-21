# Matthew Rozendaal
# Module 1, Exercise 3
# This program takes user input for number of beers on the wall
# and prints out the lyrics to the "99 Bottles of Beer" song.

def sing_beer_song(num_beers: int):
    """
    This function prints the lyrics of the "99 Bottles of Beer" song
    starting from the number of beers specified by the user.
    """
    try:
        for i in range(num_beers, 0, -1):
            print(f"{i} bottle{'s' if i != 1 else ''} of beer on the wall, {i} bottle{'s' if i != 1 else ''} of beer.")
            print(f"Take one down and pass it around, {i - 1 if i - 1 > 0 else 'no more'} bottle{'s' if i - 1 != 1 else ''} of beer on the wall.\n")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def main():
    """
    Ask the user for input and call the function to sing the song
    At the end of the program, remind the user to buy more beer
    """
    num_Beers = get_user_input("Enter the number of beers on the wall: ", 1)
    sing_beer_song(num_Beers)
    print("Time to buy more bottles of beer!")

def get_user_input(prompt: str, minAmt: int) -> int:
    """
    This function gets user input and validates that it is an integer greater than 0.
    """
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value >= minAmt:
                return value
            else:
                print(f"Input must be greater than or equal to {minAmt}.")
        except ValueError:
            print("Invalid input. Please enter an integer value.")

main()