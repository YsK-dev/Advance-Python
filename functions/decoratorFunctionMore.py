def decGreet(count):
    def greet(fn):
        def inner(name):
            for _ in range(count):
                fn(name)
        return inner
    return greet
@decGreet(count = 2)
def gm(name):
    print(f"Good morning my name is {name}")

@decGreet(count=4)
def gd(name):
    print(f"Good days my name is {name}")

gm("yusuf")#example usage
gd("yakup")