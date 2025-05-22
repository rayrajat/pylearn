'''Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of  members per group where k ≠ .1

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear k times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of k and the room number list.'''

K = int(input())
set_a = list(map(int, input().split()))

# Count occurrences using a dictionary
count_dict = {}
for num in set_a:
    count_dict[num] = count_dict.get(num, 0) + 1

    '''count how many times each item (in this case, num) appears in a collection, like a list.

What it does:
count_dict.get(num, 0) tries to get the current count of num from the dictionary.

If num is already in count_dict, it returns its value (the current count).

If num is not in the dictionary, it returns 0.

Then it adds 1 to that count.

Finally, it updates the dictionary with the new count.'''



# Find the element with count == 1
for key, value in count_dict.items():
    if value == 1:
        print(key)
        break
