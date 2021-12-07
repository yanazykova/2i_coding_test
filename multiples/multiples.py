def multiples_of_7_8_9():
    print("Here is the list of multiples of 7, up to 100: ")
    range_1 = range(0, 101)
    seven_multiples = []
    for n in range_1:
        if n % 7 == 0:
            seven_multiples.append(n)
    print(seven_multiples)

    print("Here is the list of multiples of 8, up to 200: ")
    range_2 = range(0, 201)
    eight_multiples = []
    for n in range_2:
        if n % 8 == 0:
            eight_multiples.append(n)
    print(eight_multiples)

    print("Here is the list of multiples of 9, up to 300: ")
    range_3 = range(0, 301)
    nine_multiples = []
    for n in range_3:
        if n % 9 == 0:
            nine_multiples.append(n)
    print(nine_multiples)
        
multiples_of_7_8_9()  