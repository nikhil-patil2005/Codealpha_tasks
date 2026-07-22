def chatbot():

    print("=" * 55)
    print("🤖           SIGMA CHATBOT")
    print("=" * 55)
    print("Hello! I'm your virtual friend.")
    print("You can ask me simple questions.")
    print("Type 'help' to see what I can answer.")
    print("Type 'bye' anytime to end the chat.")
    print("=" * 55)

    while True:

        user = input("\n😊 You : ").lower().strip()

        if user in ["hello", "hi", "hey"]:
            print("🤖 Bot : Hello! Nice to meet you.")

        elif user == "how are you":
            print("🤖 Bot : I'm doing great. Hope you're having a wonderful day!")
  
        elif user == "good morning":
             print("🤖 Bot : Good morning! Have a great day!")

        elif user == "good afternoon":
            print("🤖 Bot : Good afternoon!")

        elif user == "good evening":
            print("🤖 Bot : Good evening! Hope you had a nice day.")

        elif user == "good night":
            print("🤖 Bot : Good night! Sweet dreams.")

        elif user == "how old are you":
            print("🤖 Bot : I'm just a chatbot, so I don't have an age.")

        elif user == "where are you from":
            print("🤖 Bot : I live inside this Python program.")

        elif user == "nice to meet you":
            print("🤖 Bot : Nice to meet you too!")

        elif user == "i am sad":
            print("🤖 Bot : I'm sorry to hear that. I hope things get better soon.")

        elif user == "i am happy":
            print("🤖 Bot : That's great! Keep smiling.")

        elif user == "tell me a fact":
            print("🤖 Bot : Python was created by Guido van Rossum in 1991.")

        elif user == "time":
            print("🤖 Bot : Sorry, I can't tell the current time yet.")

        elif user == "weather":
            print("🤖 Bot : I am not sure, today weather is rainy!")

        elif user == "your hobby":
            print("🤖 Bot : I love chatting with people.")

        elif user == "favorite game":
            print("🤖 Bot : I like watching kabaddi, but I don't like playing it.")

        elif user == "do you like music":
            print("🤖 Bot : Yes! Music makes conversations more enjoyable.")

        elif user == "can you help me":
            print("🤖 Bot : Of course! Ask me a simple question.")

        elif user == "what is your name":
            print("🤖 Bot : My name is sigmaBot.")

        elif user == "who created you":
            print("🤖 Bot : I was developed by Nikhil Patil using Python as part of the CodeAlpha internship.")

        elif user == "what can you do":
            print("🤖 Bot : I can chat with you and answer some simple questions.")

        elif user == "python":
            print("🤖 Bot : Python is a simple, powerful and beginner-friendly programming language.")

        elif user == "your favorite color":
            print("🤖 Bot : I like Blue because it reminds me of technology.")

        elif user == "your favorite food":
            print("🤖 Bot : I don't eat food, but maharashtrian meal smells amazing! ")

        elif user == "joke":
            print("🤖 Bot : Why do programmers prefer dark mode?")
            print("         Because light attracts bugs! ")
            

        elif user == "help":
            print("\n📋 You can ask me:")
            print("• hello")
            print("• how are you")
            print("• who are you")
            print("• what is your name")
            print("• who created you")
            print("• what can you do")
            print("• good morning")
            print("• good evening")
            print("• how old are you")
            print("• where are you from")
            print("• your hobby")
            print("• favorite game")
            print("• tell me a fact")
            print("• weather")
            print("• time")
            print("• joke")
            print("• thank you")
            print("• bye")

        elif user in ["thank you", "thanks"]:
            print("🤖 Bot : You're welcome! 😊")

        elif user == "bye":
            print("\n🤖 Bot : Goodbye! 👋")
            print("Have a wonderful day. See you again!")
            print("=" * 55)
            break

        else:
            print("🤖 Bot : Sorry, I don't understand that.")
            print("          Type 'help' to see what you can ask.")


chatbot()