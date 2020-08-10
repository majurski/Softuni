book_name = input()
number_books = int(input())
found = False
counter = 0

while counter < number_books:
    book_names = input()
    if book_name == book_names:
        found = True
        print(f"You checked {counter} books and found it.")
        break
    counter += 1


if found == False:
    print(f"The book you search is not here!")
    print(f"You checked {number_books} books.")