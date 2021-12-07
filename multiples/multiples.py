def multiples_of_7_8_9():
    print("Here is the list of multiples of 7, up to 100: ")
    range_1 = range(0, 101)
    seven_multiples = []
    for n in range_1:
        if n % 7 == 0:
            seven_multiples.append(n)
    print(seven_multiples)

    print("Here is the list of multiples of 8, up to 200: ")
    eight_multiples = range(0, 201)
    
    for n in eight_multiples:
        if n % 8 == 0:
            print(n)

    print("Here is the list of multiples of 9, up to 300: ")
    nine_multiples = range(0, 301)
    for n in nine_multiples:
        if n % 9 == 0:
            print(n)
        
multiples_of_7_8_9()  