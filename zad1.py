import random


## funkciq koqto ni slaga dolna i gorna granica na chislo koeto e prompt na potrebitelq
## s try except blok proverqvame dali chisloto e v intervala ako ne e izkarva greshka
def myinput(promp , low , high):
    while True:
        try:
            number = int(input(promp))
            if(number< low or number> high):
                raise ValueError("Number out of range")
            else:
                return number
        except ValueError as e:
            print(e)
            
            
## ako __name__ e razlichen ot __main__ tozi kod ne se izpulnqva
if __name__ == "__main__":
    n = myinput("n=" , 15 , 30)
    mylist1 = []
    for i in range(n):
        ## slagame random chisla v intervala 30-300 v mylist1
        mylist1.append(random.randint(30,300))
    print(mylist1)
        
    ## slagame v mylist11 chislata ot mylist1 koito imat vtorata cifra otzad napred ravna na 3
    mylist11 = [x for x in mylist1 if x//10 % 10 % 3 == 0]
    print(len(mylist11))
    
    mylist12 = [x for x in mylist1 if x & 6 == 4]
 
    mylist2 = [x for x in mylist1 if 9 < x < 100 and x % 2 == 0 or x % 3 == 0]