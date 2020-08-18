#!/usr/bin/env python3
# Find peaks in an array

def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    elif list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]
    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1,
                          len(list_of_integers) - 1)


def find_peak_util(arr, low, high, n):
    mid = low + (high - low) // 2

    if arr[mid-1] and arr[mid] < arr[mid-1]:
        return find_peak_util(arr, low, mid-1, n)
    elif arr[mid+1] and arr[mid] < arr[mid+1]:
        return find_peak_util(arr, mid + 1, high, n)
    elif arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid]
    else:
        return arr[low]


