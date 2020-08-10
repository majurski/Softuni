from itertools import chain, zip_longest

number_of_cards = int(input())
indexes = [0,1,2,3]

deck = [i for i in range(1, number_of_cards + 1)]

def func(lst, index):
    shuffle1 = lst[:index]
    shuffle2 = lst[index:]
    res = []
    for val in list(chain(*zip_longest(shuffle1,shuffle2))):
        if val != None:
            res.append(val)
    return res

result = deck
end_results = []
for i in indexes:
    result = func(result, i)
    end_results.append(result)
print(end_results[-1:][0])




