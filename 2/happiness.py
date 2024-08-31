n, m = map(int, input("Enter the values of number of array elements and number of elements in sets A and B : ").split())

array = list(map(int, input(f"Enter integers for the array, separated by spaces: ").split()))

A = set(map(int, input(f"Enter integers for set A, separated by spaces: ").split()))

B = set(map(int, input(f"Enter integers for set B, separated by spaces: ").split()))

happiness = 0
for element in array:
    if element in A:
        happiness += 1
    if element in B:
        happiness -= 1

print(f"Your total happiness is: {happiness}")
