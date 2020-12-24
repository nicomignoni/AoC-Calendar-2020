import math

with open('day_5.txt') as f:
    seats = f.read().splitlines()

# The 'F' and 'B' notation is just a fancy way of doing binary representation.
# If F = 0 and B = 1, that FBFBBFF -> 0101100 base 2 -> 44 base 10.
all_seats = list(range((2 ** 7) * (2 ** 3)))


# Part 1 
max_seat_ID = 0
for seat in seats:
    row     = seat[:-3].replace('F', '0').replace('B', '1')
    col     = seat[-3:].replace('L', '0').replace('R', '1')
    row_int = int(row, 2)
    col_int = int(col, 2)

    seat_ID = row_int * 8 + col_int
    all_seats.remove(seat_ID)
    if seat_ID > max_seat_ID:
        max_seat_ID = seat_ID

print(max_seat_ID)

# Part 2
for i in range(len(all_seats) - 1):
    if math.fabs(all_seats[i + 1] - all_seats[i]) != 1:
        print(all_seats[i + 1])
        break


    
    
    

    
