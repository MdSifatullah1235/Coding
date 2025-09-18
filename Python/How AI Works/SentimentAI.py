import colorama
from colorama import Fore,Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN} Hello Im Sentiment Spy{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA} What is your name? {Style.RESET_ALL}").strip()

if not user_name:
    user_name = "Mystery Spy"

conversation_hist = []

print(f"\n{Fore.CYAN} Hello Agent {user_name} {Style.RESET_ALL}")

print(f"Type a sentence and I will anylyze it with textblobs sentiment analysis\n")
print(f"Type {Fore.YELLOW} 'reset' {Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN},"
      f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED} Please enter some text {Style.RESET_ALL}")
        continue
    if user_input.lower() == "exit":
        print("Exiting")
    
    elif user_input.lower() == "reset":
        conversation_hist.clear()
        print(f"{Fore.CYAN} All conversation history reset {Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_hist:
            print(f"{Fore.RED} No conversation history {Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History: {Style.RESET_ALL}")
            for idx, (text, polarity,sentiment_type) in enumerate(conversation_hist, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "👍"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "👎"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                
                print(f"{idx}. {color}{emoji}{text}"
                      f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
        continue

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
    print(f"{color}{emoji} {sentiment_type} sentiment detected!"
          f"Polarity: {polarity:.2f}{Style.RESET_ALL}")