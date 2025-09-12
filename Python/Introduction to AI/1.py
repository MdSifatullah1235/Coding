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

#Ends the conversation
print(f"I't was nice chatting with you bye")