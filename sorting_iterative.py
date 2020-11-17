#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(1, len(items)):
        if items[i-1] > items[i]:
            return False
    return True
        

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

    sorted = 0
    while not (is_sorted(items) or sorted == len(items)):
        for i in range(1, len(items)-sorted):
            if items[i-1] > items[i]:
                hold = items[i]
                items[i] = items[i-1]
                items[i-1] = hold
        sorted += 1 
    

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    start = 0
    while not (is_sorted(items) or (start == len(items))):
        min = items[start]
        min_ind = start

        for i in range(start, len(items)):
            if items[i] < min:
                min = items[i]
                min_ind = i
        
        hold = items[start]
        items[start] = min
        items[min_ind] = hold

        print(items)

        start += 1


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    unsorted_ind = 1
    while unsorted_ind < len(items):
        for i in range(0, unsorted_ind):
            if items[unsorted_ind] < items[i] or i==unsorted_ind:
                items.insert(i, items.pop(unsorted_ind))
                break
        unsorted_ind += 1
        
