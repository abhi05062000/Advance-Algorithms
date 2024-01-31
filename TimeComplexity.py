#1. O(1) Constant Time: No matter how big your data set,it takes the same amount of time to run.Think of getting first element from an array.Easy peasy!
import math
def get_first_element(elements):
    return elements[0] if elements else None
    
numbers = [1,2,3,4,5]
result = get_first_element(numbers)
print(result)
