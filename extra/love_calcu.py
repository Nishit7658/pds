def love_calculator(name1, name2):
    
    concate = name1 + name2
    concate.lower()
    count = 0
    count1 = 0
    tru = "true"
    lov = "love"

    for letter in tru:
        for char in concate:
            if letter == char:
                count += 1

    for letter in lov:
        for char in concate:
            if letter == char:
                count1 += 1

    print(f"{count}{count1}")

love_calculator("nick", "rock")
