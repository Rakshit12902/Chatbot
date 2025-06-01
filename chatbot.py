import random
import datetime
def bot():
    funfact=["ChatBot: Did you know? Honey never spoils!"" Archaeologists found 3,000-year-old honey ""in Egyptian tombs that's still edible!",
            "Bananas are berries, but strawberries aren't .",
            "Fingernails grow faster than toenails. ",
            "Dolphins have distinct whistles they use to name each other, like humans use names. ",
            "The Human Stomach Can Dissolve Razor Blades."]
    jokes=["chatbot: What does a storm cloud wear under his raincoat? Thunderwear.",
            "How does the ocean say hi? It waves!"
                  ,"Name the kind of tree you can hold in your hand? A palm tree!",
                  "What do you call a guy who's really loud? Mike",
                  "What did the lava say to his girlfriend? I lava you!",
                  " What's Thanos' favorite app on his phone? Snapchat."]
    quotes=["“Learn as if you will live forever, live like you will die tomorrow.” —Mahatma Gandhi",
            "When you change your thoughts, remember to also change your world.” —Norman Vincent Peale",
            "Success is getting what you want; happiness is wanting what you get.”―W. P. Kinsella",
            "“Goal setting is the secret to a compelling future.” —Tony Robbins",
            "“Education is the most powerful weapon which you can use to change the world.” —Nelson Mandela"]
    last_topic=None
    print("Hello i am chatbot ! Type bye to exit")
    while(True):
        user_input=input("You:").lower()
        if("hello"in user_input or "hi"in user_input or "hey"in user_input):
            print("chatbot: Hello How can i help you")
        elif("how are you"in user_input):
            print('chatbot: I am fine ')
        elif("what is your name "in user_input or "who are you"in user_input):
            print("chatbot: I am your friendly chatbot ")
        elif("what can you do"in user_input):
            print("chatbot: I can chat with you! Try asking me things like the date  time joke fun fact quotes .")
        elif("joke"in user_input):
            joke=random.choice(jokes) 
            print("chatbot:",joke)
            last_topic="joke"
        elif("fun fact" in user_input):
            funfacts=random.choice(funfact)
            print("chatbot:",funfacts)
            last_topic="fun fact"
        elif("quote"in user_input or "thought"in user_input):
            quote=random.choice(quotes)
            print("chatbot:",quote)
            last_topic="quote"
        elif "one more" in user_input or "another" in user_input or "ek aur "in user_input or "more"in user_input:
            if last_topic == "funfact":
                print("ChatBot:", random.choice(funfacts))
            elif last_topic == "joke":
                print("ChatBot:", random.choice(jokes))
            elif last_topic=="quote":
                print("chatbot:",random.choice(quotes))
            else:
                print("ChatBot: One more *what*? Try asking for a joke  fun fact or quotes first! ")

        elif "bored" in user_input:
            print("ChatBot: Let’s fix that! Want to hear a joke or a fun fact or a thought ?")
        elif("time"in user_input):
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"ChatBot: The current time is {now}")
        elif("date"in user_input):
            from datetime import datetime
            today = datetime.today().strftime("%Y-%m-%d")
            print(f"ChatBot: Today's date is {today}")
        elif("thankyou"in user_input or "thanks"in user_input):
            print("chatbot: Your Welcome! Happy to help")
        elif("bye"in user_input):
            print("chatbot: Goodbye!, Have a great day")
        else:
            print("ChatBot: Hmm... I’m still learning. Can you ask me something else? ")



bot()