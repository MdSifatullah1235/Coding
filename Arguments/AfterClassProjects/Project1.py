def shutdown(inp):
    if inp == "yes":
        return "Shutting down...."
    
    elif inp == "no":
        return "Aborting shut down..."
    
    else:
        return "Sorry, invalid input."

inpu = input("Enter yes or no to shutdown: ")
print(shutdown(inpu))