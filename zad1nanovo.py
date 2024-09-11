#1 zad
#1[x]
#2[x]
#3[]
#4[]
#5[]
#6[]
#7[]


#1
import random


def myInput(low , promp , high):
    while True:
        try:
            number = int(input(promp))
            if(low > number > high):
                raise ValueError("Number out of range")
            else:
                return number
        except ValueError as e:
                 print(e)



if __name__ == "__main__":
    n = myInput(15 , "n=" , 35)
    mylist1 = []
    for i in range(n):
        mylist1.append(random.randint(30,300))

    mylist11 = [x for x in mylist1 if x//10 % 10 % 3 == 0]

    mylist12 = [x for x in mylist1 if x % 6 == 4]
    minNumber = min(mylist12)
    minIndex = mylist1.index(minNumber)

    print(mylist12)
    print(minNumber)
    print(minIndex)
