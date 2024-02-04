def divideThem(arr1, arr2):         

    if (len(arr1) != len(arr2)):
        return print("Arrays must be of same length.")              # MADE TO DIVIDE ARR1 BY ARR2, JUST SWITCH TO DIVIDE OTHER WAY
    for i in range(len(arr1)):
        if (arr2[i] == 0) or ((len(str(arr2[i]))) == 0):
            return print("Array 2 can not contain any zeroes.")

    newArray = []
    counter = 0
    for i in range(len(arr1)):
        if (isinstance(arr1[i], str)):
            for j in range(len(str(arr1[i]))):
                counter = counter + 1
            newArray.append(counter / arr2[i])

        elif(isinstance(arr2[i], str)):
            for j in range(len(str(arr2[i]))):
                counter = counter + 1
            newArray.append(arr1[i] / counter)  

        else: 
            newArray.append(arr1[i] / arr2[i])
        counter = 0
    print(newArray)



# if __name__ == "__main__":
#     arr1 = [0, 4, 3]
#     arr2 = ["burger", 4 ,3]
#     divideThem(arr1, arr2)