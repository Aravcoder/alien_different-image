numbers=(1,2,3,-12,-3,9,10)

print(numbers)
print("I will input a random nmber from the tuple: ",numbers[3])
print("I will print the lenght of this tuple : ",len(numbers))

count = 1

for i in numbers:
    print(i)
    print("The number of iterations in this for loop are : ",count)
    count=count+1
# numbers [1] = 100
# del numbers
# print(numbers)

print(-12 in numbers)
print(-1 in numbers)

# packing
address=("10","snoekbaarsstraat","aalsmeer","Netherlands","1432pe")
# unpacking
housenumber,street,city,country,pinaddress=address

print(city)
fruits="apple","banana","ornages","grapes"
print(fruits)

nested_tuple=(1,2,("apple","banana"),[5,6])
print(nested_tuple)
print(nested_tuple[2][1])
print(nested_tuple[3][0])

print(address[1:4])
print(address[:])
nested_tuple[3][0]=100
print(nested_tuple)