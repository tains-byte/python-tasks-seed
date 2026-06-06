"""
Sorting algorithms
"""

from __future__ import annotations
from typing import Any
from comp_swap_container import CompSwapList


def trivial_sort2(data: CompSwapList[Any]):
    """
    Sorts a container with 2 or fewer elements

    :param data: data to sort inplace
    :type data: MutableSequence[Ordered]
    """
    if len(data) <= 1:
        pass
    if len(data) > 2:
        raise ValueError("Expected at most 2 elements!")
    if data.less(1, 0):
        data.swap(0, 1)


def merge_sort(data: CompSwapList[Any]):
    """
    Merge Sort

    :param data: data to sort inplace
    :type data: CompSwapList[Any]
    """
    if len(data) <= 1:
        return

    buffer = [None] * len(data)
    
    def _merge_sort(left, right):
        if right - left <= 1:
            return
            
        mid = (left + right) // 2
        _merge_sort(left, mid)
        _merge_sort(mid, right)
        
        for i in range(left, right):
            buffer[i] = data.get(i)
            
        i, j, k = left, mid, left
        
        while i < mid and j < right:
            if data.less(j, i): 
                data.set(k, buffer[j])
                j += 1
            else:
                data.set(k, buffer[i])
                i += 1
            k += 1
            
        while i < mid:
            data.set(k, buffer[i])
            i += 1
            k += 1
            
        while j < right:
            data.set(k, buffer[j])
            j += 1
            k += 1

    _merge_sort(0, len(data))

def selection_sort(data: CompSwapList[Any]):
    """
    Selection sort

    :param data: data to sort inplace
    :type data: CompSwapList[Any]
    """
    n = len(data)
    
    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            if data.less(j, min_idx):
                min_idx = j

        if min_idx != i:
            data.swap(i, min_idx)
