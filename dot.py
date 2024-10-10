def dot(arr1, arr2):
    ans = 0
    for i in range(min(len(arr1), len(arr2))):
        ans += arr1[i] * arr2[i]
    
    return ans

n1 = int(input("Enter size of array1: "))
arr1 = []

for i in range(n1):
    arr1.append(int(input(f"arr1[{i}] = ")))
    
n2 = int(input("Enter the size of array2: "))
arr2 = []

for i in range(n2):
    arr2.append(int(input(f"arr2[{i}] = ")))
    
ans = dot(arr1, arr2)
print(f"The dot product of the vectors is: {ans}")
