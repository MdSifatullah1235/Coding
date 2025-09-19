import re, random
from colorama import Fore, init

# Intiliaze colorama(autoset = True means it ensures each print resets after use)
init(autoreset=True)

#Destination and Joke data
destinations = {
    "beaches": ["Bali","Maldives","Phuket"],
    "mountains": ["Swiss Alps","Rocky Mountains","Himalayas"],
    "cities": ["Tokyo","Paris","New York","Washington D.C","California"]
}

jokes = [
    "Why don't programmers like nature ? too many bugs",
    "Why did the computer go to a doctor ? because it had a virus",
    "Why do travelers always feel warm ? becauseof of all their hot spots"
]

#Helper funtion used for removing spaces,lowercasing the input from user
def normalize_text(text):
    return re.sub(r"\s+"," ",text.strip().lower())

# Provide travel Recommendation (recursive if user rejects suggestions)
def recommend():
    print(Fore.CYAN + "Beaches, mountains or cities ?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_text(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(f"{Fore.GREEN} How about {suggestion} ?")
        print(f"{Fore.CYAN} Do you like it ? (yes/no)")
        ans = input(Fore.YELLOW + "You: ").lower()

        if ans == "yes":
            print(Fore.GREEN + f"Awesome! enjoy your trip to {suggestion}")
        elif ans == "no":
            print(Fore.RED + "No, it's ok let's try another one")
            recommend()
        
        else:
            print(Fore.RED + "Let's try again!")
            recommend()
    else:
        print(Fore.RED + "Sorry I don't have that destination")
    show_help()


#Offering packing tips based on users destination and duration
def packing_tips():
    print(Fore.CYAN + "Where to ?")
    location = input(Fore.YELLOW + "You : ")
    print(Fore.CYAN + "How many days ?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN+ f"Packing tips for {days} in {location} ")
    print(Fore.GREEN + "- Pack versatile clothes")
    print(Fore.GREEN + "- Bring charger/adapters")
    print(Fore.GREEN + "- Check the weather forecast")


# tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"{random.choice(jokes)}")

#Dispaly help menu
def show_help():
    print(Fore.MAGENTA+ "\n I can:")
    print(Fore.GREEN + "Suggest Travel Spots (say 'recommendation')")
    print(Fore.GREEN + "Offer packing tips (say 'packing')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end conversation \n")

#Main chat loop
def chat():
    print(Fore.CYAN + "Hello! Im travelbot")
    print(Fore.CYAN+"Your Name ?")
    name = input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"Nice to meet you! {name}")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_text(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "Safe Travels bye!")
            break
        else:
            print(Fore.RED + "Could you rephrase ?")



#Run the chatbot
if __name__ == "__main__":
    chat()