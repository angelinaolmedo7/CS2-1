#!python

import sorting_iterative

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n) where n is the length of both lists combined
    TODO: Memory usage: O(n) because I made a new list for this, you could probably do it in place though"""
    
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    
    newlist = []
    while len(items1) > 0 and len(items2) > 0:
        if items1[0] < items2[0]:
            newlist.append(items1.pop(0))
        else: 
            newlist.append(items2.pop(0))
    newlist.extend(items1)
    newlist.extend(items2)

    return newlist


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: O of whatever the iterative algorithm you used is :/
    TODO: Memory usage: O(1)"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order

    # how long is half the list?
    half = len(items)//2
    if half == 0: # len is 0 or 1
        return items 

    # split list in two
    first_half = items[:half]
    second_half = items[half:]

    # sort w/ imported selection sort
    sorting_iterative.selection_sort(first_half)
    sorting_iterative.selection_sort(second_half)

    # merge them back together and assign to items
    items[:] = merge(first_half, second_half)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n log(n))
    TODO: Memory usage: O(n)"""
    
    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return(items)

    # TODO: Split items list into approximately equal halves
    half = len(items)//2
    
    first_half = items[:half]
    second_half = items[half:]

    # TODO: Merge sorted halves into one list in sorted order
    merge_sort(first_half)
    merge_sort(second_half)

    items[:] = merge(first_half, second_half)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: O(n), just goes through once
    TODO: Memory usage: O(1), in place comparisons"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # pivot is gonna be the last index. p is then len(items[low:high])-1

    pivot = items[high]
    p = high

    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # print(items)
    for i in range(low, high):
        if items[i] <= pivot:
            items.insert(low, items.pop(i))
            low += 1
        else:
            items.insert(low, items.pop(i))

    # TODO: Move pivot item into final position [p] and return index p
    items.insert(low, items.pop(p))
    return low



def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: O(n log(n))
    TODO: Worst case running time: O(n^2)
    TODO: Memory usage: O(log(n))"""
    # TODO: Check if high and low range bounds have default values (not given)
    if low == None or high == None:
        low = 0
        high = len(items)-1
            
    # TODO: Check if list or range is so small it's already sorted (base case)
    if low >= high:
        pass # small enough, could combine w/ next statement but will leave for clarity

    else: 
        # TODO: Partition items in-place around a pivot and get index of pivot
        p = partition(items, low, high)

        # TODO: Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, p-1)
        quick_sort(items, p, high)

if __name__ == "__main__":
    pass
