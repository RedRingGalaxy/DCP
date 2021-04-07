# Problem Statement [Medium]
'''
Given a pivot x, and a list lst, partition the list into three parts.

1. The first part contains all the elements in the lst that are less than x.
2. The second part contains all the elements in the lst that are equal to x.
3. The third part contains all the elements in the lst that are larger than x.

Ordering within a part can be arbitrary

ex: x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one of partition may be

[9, 3, 5, 10, 10, 12, 14]

'''

# One solution is sorting. Here try to make the solution exactly as shown in example.

# TODO: Partion the given list using divide and conquer
def partition(arr, pivot):
    sort(arr, pivot, 0, len(arr)-1)

# TODO: Divide the list using s (source) and d (destination) index value
def sort(arr, pivot, s, d) -> None:
    if s < d:
        mid =  (s+d)//2
        sort(arr, pivot, s, mid)
        sort(arr, pivot, mid+1, d)
        Merge(arr, pivot, s, mid, d)

# TODO: Merge by partion order using pivot value
def Merge(arr, pivot, s, mid, d) -> None:
    n1 = mid - s + 1 
    n2 = d - mid

    sub1 = [ arr[s+i] for i in range(n1)]
    sub2 = [ arr[mid+1+i] for i in range(n2)]

    i = j = 0
    k = s
    
    while i < n1 and j < n2:
        if sub1[i] > pivot and sub2[j] <= pivot:
            arr[k] = sub2[j]           
            j += 1
        elif sub1[i] <= pivot:
            i += 1
        else:
            break
        k +=1

    while i < n1:
        arr[k] =  sub1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] =  sub2[j]
        j += 1
        k += 1
            

if __name__ == "__main__":
    lst = [9, 3, 12, 5, 14, 10, 27, 10]
    print(lst)
    partition(lst,10)
    print(lst)