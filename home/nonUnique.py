# You are given a list of integers. 
# For this task, you should return a list consisting of only the non-unique elements in this list. 
# To do so you will need to remove all unique elements (elements which are contained in a given list only once). 
# When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3]. 

def nonUnique(data):
    return [element for element in data if data.count(element) > 1]

if __name__ == "__main__":
    assert isinstance(nonUnique([1]), list), "The result must be a list"
    assert nonUnique([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert nonUnique([1, 2, 3, 4, 5]) == [], "2nd example"
    assert nonUnique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert nonUnique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
       