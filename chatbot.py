def chatbot():

    print("👋")
    print("You can chat with me 🤗")
    print("Type 'bye' anytime to exit.\n")

    while True:

        user_input = input("You: ").lower()

        if user_input == "hello":
            print("PyBuddy: Hi there 👋")

        elif user_input == "who are you":
            print("PyBuddy: I am PyBuddy, your companion 😄")
            print("PyBuddy: What is your name?")

            name = input("You: ")

            print(f"PyBuddy: {name} is a cool name 🤩")

        elif user_input == "who created you":
            print("PyBuddy: I was created by a future programmer 😎")

        elif user_input == "tell me a joke":
            print("PyBuddy: Why do programmers prefer dark mode? 😂 Because light attracts bugs!")

        elif user_input == "that's funny":
            print("PyBuddy: What's more fun is being able to chat with you 😍")

        elif user_input == "thank you":
            print("PyBuddy: your welcome! 😇")

        elif user_input == "bye":
            print("PyBuddy: Goodbye 👋 Have a great day 🫶")
            break

        else:
            print("PyBuddy: Sorry, I didn't understand 😅")

chatbot()