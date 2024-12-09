def double(fn):
    def inner(*args, **kwargs):
        fn(*args, **kwargs)
        return fn(*args, **kwargs)
    return inner

@double
def hi():
    print("Hİ !")

@double
def hello(name):
    print("HEllo",name)
@double
def goodDays():
    return "Have a good day sir"



hi()
hello("yakuo")
print(goodDays())