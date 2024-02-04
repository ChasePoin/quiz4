from addition.addingThemAll import addThem as add
from divide.divideThemAll import divideThem as divide
from multiplication.multiplyThemAll import multiplyThem as multiply

# each function takes two arrays of similar length, three functions to multiply, divide, or add/sub each number
# can either use strings or integers
# divide will NOT take zero in arr2, as divide() is made to divide arr1 / arr2


arr1 = ["hamburger", 4, 3]
arr2 = [3, 2, 0]

multiply(arr1, arr2)
divide(arr1, arr2)
add(arr1, arr2)