def counter(max):
    num = 1

    while num <= max:
        yield num
    
        num += 1



generator = counter(20)

# print(dir(generator))

# print(next(generator))
# print(next(generator))
# print(next(generator))

# for i in generator:
#     print(i)

# result = list(generator)

# print(result)

lisT = (i for i in range(1,20))

print(next(lisT))
