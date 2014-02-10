#A median is a numerical value separating the upper half of a list of numbers from the lower half.
# For this mission, you are given a list of integers. 
#With it, you must separate the upper half of the numbers from the lower half and find the median


def getMedian(data):
    data.sort()
    return (data[(len(data) - 1) / 2] + data[len(data) / 2 ]) / 2.0


if __name__ == '__main__':
    assert getMedian([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert getMedian([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert getMedian([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert getMedian([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
