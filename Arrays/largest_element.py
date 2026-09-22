arr = list(map(int, input("Enter elements: ").split()))

largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print("Largest element:", largest)