n_guests = int(input())
guests = set()
for _ in range(n_guests):
    reservation_n = input()
    guests.add(reservation_n)

command = input()

while command != "END":
    if command in guests:
        guests.remove(command)

    command = input()

sorted_guests = sorted(guests)

print(len(sorted_guests))
for guest in sorted_guests:
    print(guest)