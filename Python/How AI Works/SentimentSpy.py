import colorama
from colorama import Fore, Style
from textblob import TextBlob
import random

colorama.init()

print(f"{Fore.CYAN} Hello I'm Sentiment Spy {Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA} What is your name? {Style.RESET_ALL}").strip()

if not user_name:
    user_name = "Mystery Spy"

conversation_hist = []

print(f"\n{Fore.CYAN} Hello Agent {user_name} {Style.RESET_ALL}")

print(f"Type a sentence and I will analyze it with TextBlob's sentiment analysis\n")
print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, "
      f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}")

# Some fun/random normal questions
normal_questions = [
    "What's your favorite color?",
    "If you could travel anywhere, where would you go?",
    "Do you like reading books or watching movies more?",
    "What's your favorite food?",
    "Which superhero do you like the most?",
    "Do you enjoy playing games?",
    "What's one hobby you wish you had more time for?",
    "Do you prefer mornings or nights?",
    "If you had a superpower, what would it be?",
    "What's a song you never get bored of?"
]

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED} Please enter some text {Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":
        print("Exiting... Goodbye Agent!")
        break

    elif user_input.lower() == "reset":
        conversation_hist.clear()
        print(f"{Fore.CYAN} All conversation history reset {Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_hist:
            print(f"{Fore.RED} No conversation history {Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History: {Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_hist, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "👍"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "👎"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(f"{idx}. {color}{emoji} {text} "
                      f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
        continue

    # Sentiment Analysis
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "👍"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "👎"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_hist.append((user_input, polarity, sentiment_type))
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
          f"Polarity: {polarity:.2f}{Style.RESET_ALL}")

    # Ask a random fun question 30% of the time
    if random.random() < 0.3:
        question = random.choice(normal_questions)
        print(f"{Fore.CYAN}🤔 Quick Question: {question}{Style.RESET_ALL}")
