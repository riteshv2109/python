# a="hey i am ritesh"
# print(len(a))

fruit="mango"
len1=len(fruit)
print("mango is a",len1,"letter word")

print(fruit[1:4])
print(fruit[1:-3])
# python automatically subtracts -ve slicing with the length of the 
# string i.e. len(mango)=5 so,end =5-3=2.
# if the given slicing is from [4:2] then nothing is printed.

nm="harry"
print(nm[-4:-2])