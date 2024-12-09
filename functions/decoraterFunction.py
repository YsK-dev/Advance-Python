def greet(fn):
    def inner():
        print("welcome bro ")
        fn()
        print("see you later")
    return inner
    
@greet
def goodMorning(typeofdream):
    print(f"Good Morning today I had a {typeofdream} dream :/")
@greet
def intro(name):
     print(f"Hi! My name is {name}")


# reultG = greet(goodMorning)

# reultG()

# resultI = greet(intro)
# resultI()

goodMorning("good")
intro()