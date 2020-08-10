movie_name = input()

student_ticket_count = 0
standard_ticket_count = 0
kids_ticket_count = 0
all_tickets_sold = 0

while movie_name != "Finish":
    total_seats = int(input())
    free_seats = total_seats
    ticket_type = input()
    while free_seats > 0 and ticket_type != "End":
        all_tickets_sold += 1
        free_seats -= 1

        if ticket_type == "student":
            student_ticket_count += 1
        elif ticket_type == "standard":
            standard_ticket_count += 1
        else:
            kids_ticket_count += 1
        if free_seats > 0:
            ticket_type = input()


    percent_movie_ocup = 100 - (free_seats / total_seats * 100)
    print(f"{movie_name} - {percent_movie_ocup:.2f}% full.")

    movie_name = input()

print(f"Total tickets: {all_tickets_sold}")

sold_stud_tick_per = student_ticket_count / all_tickets_sold * 100
sold_standard_tick_per = standard_ticket_count / all_tickets_sold * 100
sold_kids_tick_per = kids_ticket_count / all_tickets_sold * 100

print(f"{sold_stud_tick_per:.2f}% student tickets.")
print(f"{sold_standard_tick_per:.2f}% standard tickets.")
print(f"{sold_kids_tick_per:.2f}% kids tickets.")
