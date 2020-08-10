from itertools import chain, zip_longest

number_of_cards = int(input())
indexes = [3,3,2]

deck = [i for i in range(1, number_of_cards + 1)]

def dividerL(lst, index):
    shuffle1 = lst[:index]
    return shuffle1

def dividerR(lst, index):
    shuffle2 = lst[index:]
    return shuffle2

def sticky(list1, list2):
    res = []
    a = list(chain(*zip_longest(list1,list2)))
    for val in a:
        if val != None:
            res.append(val)
    return res

for i in indexes:
    print(sticky(dividerL(deck, i), dividerR(deck, i)))


