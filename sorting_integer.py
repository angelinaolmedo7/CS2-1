#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # TODO: Find range of given numbers (minimum and maximum integer values)
    # am I allowed to use min()/max()?
    if len(numbers) == 0:
        return 

    mn = numbers[0]
    mx = numbers[0]

    for num in numbers:
        if num < mn:
            mn = num
        if num > mx:
            mx = num

    # TODO: Create list of counts with a slot for each number in input range
    counts = [0]
    for _ in range(mn, mx):
        counts.append(0)

    # TODO: Loop over given numbers and increment each number's count
    for num in numbers:
        counts[num-mn] += 1

    # TODO: Loop over counts and append that many numbers into output list
    output = []
    for i in range(len(counts)):
        for _ in range(counts[i]):
            output.append(mn+i)

    numbers[:] = output
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    if len(numbers) == 0:
        return 

    mx = max(numbers)

    # TODO: Create list of buckets to store numbers in subranges of input range
    buckets = [[] * num_buckets]
    print(buckets)


    # TODO: Loop over given numbers and place each item in appropriate bucket
    for num in numbers:
        print(str(num * len(buckets) // (mx + 1)))
        buckets[num * len(buckets) // (mx + 1)].append(num)



    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    output = []
    for bucket in buckets:
        counting_sort(bucket)
        output.extend(bucket)

    numbers[:] = output
    # FIXME: Improve this to mutate input instead of creating new output list