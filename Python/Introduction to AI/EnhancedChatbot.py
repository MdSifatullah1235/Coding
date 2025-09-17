print("Hello I'm the AI bot. Whats your name ? ")
#Asking the user for his name

name = input() #Takes the name as a input from the user

print(f"Nice to meet you {name}") #Responding to the user

#Asks a question
print("How are you feeling today ? (good/bad) : ")

mood = input().lower() #Takes the mood of the user as a input from the user

#if the input is good
if mood == "good":
    print("Im glad to hear that!") #Responds to the input

#if the input is bad
elif mood == "bad":
    print("Oh sorry to hear that! ") #Responds to the input

#If the input is something else
else:
    print("Sometimes it's hard to put feelings into words. It will be alright") #Responds to the input

print("Anyways, do you like any sports? (yes/no) : ")

sport = input().lower() #Takes the sport of the user as a input from the user

#if the input is yes
if sport == "yes":
    print("What sport? :") #Responds to the input

    sport = input() #Takes the sport of the user as a input from the user

    print(f"Great! I like {sport} too!") #Responds to the input

#if the input is no
elif sport == "no":
    print("That's too bad") #Responds to the input

print("Anyways, do you like any movies? (yes/no) : ")

movie = input().lower() #Takes the movie of the user as a input from the user

#if the input is yes
if movie == "yes":
    print("What movie? :") #Responds to the input

    movie = input() #Takes the movie of the user as a input from the user

    print(f"Great! I like {movie} too!") #Responds to the input

#if the input is no
elif movie == "no":
    print("That's too bad") #Responds to the input

print(f"I't was nice chatting with you {name} bye")

print("Wanna create a new chat (yes/no) ? : ")

loopans = input().lower() #Takes the answer as a input from the user

if loopans == "yes":
    print("Hello I'm the AI bot. Whats your name ? ")
#Asking the user for his name

    name = input() #Takes the name as a input from the user

    print(f"Nice to meet you {name}") #Responding to the user

    #Asks a question
    print("How are you feeling today ? (good/bad) : ")

    mood = input().lower() #Takes the mood of the user as a input from the user

    #if the input is good
    if mood == "good":
        print("Im glad to hear that!") #Responds to the input

    #if the input is bad
    elif mood == "bad":
        print("Oh sorry to hear that! ") #Responds to the input

    #If the input is something else
    else:
        print("Sometimes it's hard to put feelings into words. It will be alright") #Responds to the input
        print("Anyways, do you like any sports? (yes/no) : ")
        sport = input().lower() #Takes the sport of the user as a input from the user

    #if the input is yes
    if sport == "yes":
        print("What sport? :") #Responds to the input
        sport = input() #Takes the sport of the user as a input from the user
        print(f"Great! I like {sport} too!") #Responds to the input

#if the input is no
elif sport == "no":
    print("That's too bad") #Responds to the input

print("Anyways, do you like any movies? (yes/no) : ")

movie = input().lower() #Takes the movie of the user as a input from the user

#if the input is yes
if movie == "yes":
    print("What movie? :") #Responds to the input

    movie = input() #Takes the movie of the user as a input from the user

    print(f"Great! I like {movie} too!") #Responds to the input

#if the input is no
elif movie == "no":
    print("That's too bad") #Responds to the input

print(f"I't was nice chatting with you {name} bye")

if loopans == "no":
    print("Bye")