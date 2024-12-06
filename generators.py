def counter(max):
    num = 1
    numbers =[]

    while num <= max:
        numbers.append(num)
        num += 1

    return numbers

result = counter(20)

print(result)