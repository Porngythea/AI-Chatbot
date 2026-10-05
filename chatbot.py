print ("Hello! I am an AI Bot. What's your name? : ")
name = input()
print(f"Nice to meet you, {name}!")
print("How are you feeling today? (good/bad) : ")
mood = input().lower()
if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that!")
else:
    print("I see, no matter how you're feeling. It's always going to be a great day!")
print(f"It was nice chatting with you!")