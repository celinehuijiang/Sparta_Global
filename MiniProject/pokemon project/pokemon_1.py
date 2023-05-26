import random
import requests
import json

def get_random_pokemon():
# generate a random Pokémon ID between 1 and 898 (total number of Pokémon in the API)
# getting the data from the pokemon 
    pokemon_id = random.randint(1, 898)
    url = f"https://pokeapi.co/api/v2/pokemon/ditto" # getting the url
    response = requests.get(url)
    # ceating a statement when the connection be made, convert into json 
    if response.status_code == 200:
        pokemon_data = response.json() # converting into json file 
        return pokemon_data
    else:
        print("Error occurred while retrieving Pokémon data.") # show error message if the data not retrieved propeerly 
        return None

def pokemon_game():
    pokemon_data = get_random_pokemon()
    if not pokemon_data:
        return
    # extracting names and types from the json file
    name = pokemon_data['name']
    # list comphrension to get names and types 
    types = [t['type']['name'] for t in pokemon_data['types']]
    
    print("Welcome to the Pokémon Guessing Game!")
    print("I'm thinking of a Pokémon with the following types:", ", ".join(types))
    print("Can you guess the Pokémon?")
    # iterating how many attempts the user has inputed - has inputed 
    attempts = 0
    while True:
        # user input 
        guess = input("Enter your guess (or 'quit' to exit): ")
        attempts += 1
        # have user to leave the game when they ddin't get guess close to the number 
        if guess.lower() == 'quit':
            print("Thanks for playing! The Pokémon was", name)
            break
        # when user makes the corrects guess then print out the message that the user has guessed correctly 
        if guess.lower() == name.lower():
            print("Congratulations! You guessed the Pokémon correctly!")
            print("Number of attempts:", attempts)
            break
        else:
            # if not getting right, offer user hint to guess pokemon 
            print("That's not the right Pokémon. Try again!")
            print("Hint: The Pokémon has the following types:", ", ".join(types))
            break

# call the pokemon_game function to start the game
pokemon_game()



