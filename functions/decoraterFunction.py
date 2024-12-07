def greet(fn):
    def inner():
        print("welcome bro ")
        fn()
        print("see you later")
    return inner
    
@greet
def goodMorning():
    print("Good Morning today I had a bad dream :/")
@greet
def intro():
     print("Hi! My name is YsK")


# reultG = greet(goodMorning)

# reultG()

# resultI = greet(intro)
# resultI()

goodMorning()
intro()