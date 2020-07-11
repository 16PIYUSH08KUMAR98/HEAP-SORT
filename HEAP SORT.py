#heapify
def heapify(arr , n,i):
    largest = i
    left_child = 2*i + 1
    right_child = 2* i +2
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child
    if right_child < n and arr[largest]< arr[right_child]:
        largest = right_child
    if largest != i:
        arr[i] ,arr[largest] = arr[largest] ,arr[i]
        heapify( arr ,n,largest)

#sort
def heapSort(arr):
    n = len(arr)

    # maxheap
    for i in range(n//2, -1 , -1):
      heapify(arr, n,i)
    # element extraction
    for i in  range(n-1,0 ,-1):
      #swap
      arr[i] , arr[0] = arr[0], arr[i]

      #Heapify root element
      heapify(arr , i, 0)

 #main
    arr = [1,2,3,5,7,12,7,10]
    heapSort(arr)
    n= len(arr)
    print ("Sorted array is the")
    for i in  range(n):
        print ( "%d " % arr[i], end = '' )
