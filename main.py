
list = [4,5,7,5,4,8]
list1 = [9, 10, 19, 13, 19, 13]
list2 = [16, 0, 11, 4, 8, 16, 0, 11]

def repeats(arr):
    newArr = []
    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            newArr.append(arr[i])

    return sum(newArr)

print(repeats(list))
print(repeats(list1))
print(repeats(list2))