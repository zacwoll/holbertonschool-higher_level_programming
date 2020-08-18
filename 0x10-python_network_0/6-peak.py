#!/usr/bin/env python3
# Find peaks in an array

def find_peak(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    elif arr[-1] > arr[-2]:
        return arr[-1]
    return find_peak_util(arr, 0, len(arr) - 1, len(arr) - 1)


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


