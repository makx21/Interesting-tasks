def nonUnique(data):
    return [element for element in data if data.count(element) > 1]

if __name__ == "__main__":
    assert isinstance(nonUnique([1]), list), "The result must be a list"
    assert nonUnique([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert nonUnique([1, 2, 3, 4, 5]) == [], "2nd example"
    assert nonUnique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert nonUnique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
       