#array
arr = [2,1,9,8,7]


#bubble sort function

def bubble(arr):
    n = len(arr)

    #traverse through all elements
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

bubble(arr)

print('sorted array is')

for i in range(len(arr)):
    print(arr[i])


