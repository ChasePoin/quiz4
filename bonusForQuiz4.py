def count(arr) -> None:
    counter = 0
    newArray = []
    for i in range(len(arr)):
        for j in range(len(str(arr[i]))):
            counter = counter + 1
        newArray.append(counter)
        counter = 0
    print(newArray)

# testing it 
# if __name__ == "__main__":
#      argh = [24812390, 12, "gold", 12312321321, "grah"]
#    
#      count(argh)