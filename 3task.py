def BinarySearch(L, el):
    if el < L[0] or el > L[-1]:
        return False    
    first = 0
    last = len(L)
    while first < last-1:
        mid = (first+last)//2
        if el > L[mid]:
            last = mid
        else:
            first = mid
    return first

L = [36, 72, 108, 144, 147, 161]
el = 162
print(BinarySearch(L, el))    