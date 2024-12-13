class Meta(type):
    def __new__(self,className,bases,attributes):
        print(attributes)

        a = {}

        for name, val in attributes.items():
            if name.startswith("_"):
                a[name] = val
            else:
                a[name.upper()] = val


        return type(className,bases,attributes)
 

class Person(metaclass=Meta):
    x = 5
    y = 10

    def hello(self):
        print("hi !")


p = Person()

sonuc=p.x
sonuc=p.y
print(sonuc)
# sonuc = Test()

# sonuc = type(Test

# print(sonuc)