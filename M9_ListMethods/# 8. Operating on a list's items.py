# 8. Operating on a list's items (uhh)
print("Input List 1 item count:", end=" ")
icount = int(input())

print("Input List 1 items:", end=" ")
list1 = [int(input()) for x in range (icount)]

print("Input List 2 item count:", end=" ")
iicount = int(input())

print("Input items:", end=" ")
list2 = [int(input()) for x in range(iicount)]

mean1 = sum(list1) / len(list1)
mean2 = sum(list2) / len(list2)

for item1 in list1:
    print(" ")
    print(f"Item: {item1}")
    print(f"Added to itself: {item1 + item1}")
    print(f"Multiplied by itself: {item1 * item1}")
    print(f"Itself as the exponent: {item1 ** item1}")
    print(" ")

for item2 in list2:
    print(" ")
    print(f"Item: {item2}")
    print(f"Added to itself: {item2 + item2}")
    print(f"Multiplied by itself: {item2 * item2}")
    print(f"Itself as the exponent: {item2 ** item2}")
    print(" ")

print("List 1:", list1)
print("List 2:", list2)
print("Sum of List 1 items:", sum(list1))
print("Sum of List 2 items:", sum(list2))
print(f"Mean of List 1 items: {mean1:.2f}")
print(f"Mean of List 2 items: {mean2:.2f}")