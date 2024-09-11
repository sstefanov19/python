import random
# import math
# def myInput(prompt , low , high):
#     while True:
#         try:
#             number = int(input(prompt))
#             if number <= low or number >= high:
#                 raise ValueError("out of reach")
#             else :
#                 return number
#         except ValueError as e:
#             print(e)



# if __name__ == "__main__":

#     n = myInput("n=" , 20 , 30)
#     list1 = [random.randint(-100 , 100) for _ in range(n)]

#     ## finding the sum by getting the odd indices starting from 1 and skipping 2
#     sum_odd_indices = sum(list1[i] for i in range(1 , len(list1) , 2))

#     count_units_div_2 = len([x for x in list1 if abs(x) % 10 % 2 == 0])

#     # solution number 1
#     # negative_elements = [x for x in list1 if x < 0 and x % 2 == 0]
#     # if negative_elements:
#     #    product_of_negative_even = math.prod(negative_elements)
#     # else:
#     #     product_of_negative_even = "No negative numbers"


#     #solution number 2
#     negative_elements = 1
#     for x in list1:
#         if x < 0 and x % 2 == 0:
#             negative_elements += x

#     if negative_elements == 1:
#         print("No negative elements found")
#     else:
#         print(negative_elements)


#     sorted_list = sorted(list1 , reverse=True)
#     print(sorted_list)



def myInput(prompt , low , high):
    while True:
        try:
            number = int(input(prompt))
            if number <= low or number >= high:
                raise ValueError("out of reach")
            else:
                return number
        except ValueError as e:
            print(e)



if __name__ == "__main__":

    n = myInput("n=" , 15 , 35)

    list1 = [random.randint(30 , 300) for _ in range(n)]

    number_elements_indices_3 = len([x for x in list1 if (x // 10) % 10 % 3 == 0])

    min_index_of_six = [x for x in list1 if x %  6 == 4]
    if min_index_of_six:
        min_element = min(min_index_of_six)
        min_index =  list1.index(min_element)
        print(min_index)
    else:
        print("No elements")


    list2 = [x for x in list1 if 10 <= x < 100 and (x % 2 == 0 or x % 3 == 0)]
    odd_index_elemts = [list[i] for i in range(1 , len(list1) , 2)]
    if(odd_index_elemts) :
        avarage_odd_index = sum(odd_index_elemts) / len(odd_index_elemts)
    else:
        print("No elements with that index")


    even_numbers = [x for x in list2 if x % 2 == 0]
    if(even_numbers):
        min_even = min(even_numbers)
        list2.remove(min_even)
    else:
        print("No even numbers")
        
