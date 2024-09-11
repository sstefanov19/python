import random
def myInput(prompt , low , high) :
    while True:
        try:
            number = int(input(prompt))
            if(low > number > high):
                raise ValueError("Out of range")
            else:
                return number
        except ValueError as e:
            print(e)



if __name__ == "__main__":
    n = myInput("n=" , 15 , 35)
    list1 = []
    for i in range(n):
        list1.append(random.randint(30 , 300))

    list11 = [x for x in list1 if x//10 % 10  % 3 == 0]

    list12 = [x for x in list1 if x % 6 == 4]
    minVal = min(list12)
    indexVal = list1.index(minVal)

    list2 = [x for x  in list1 if 9 < x < 100 and (x % 2 == 0 or x % 3 == 0)]
    print(list2)

    list22 = [list2[i] for i in range(1 , len(list2) , 2)]

    try:
        print(sum(list22) / len(list22))
    except ZeroDivisionError as e:
        print(e)

    list23 = [x for x in list2 if x % 2 ==0]
    try:
        min_even = min(list23)
        list2.remove(min_even)

    except ValueError:
        print("No such data")
