dict={"nov":"ritesh","dec":"abhinav","sep":"priyanshu"}
print(dict)

print(dict["dec"])
print(dict.get("dec"))

'''the difference between these two is :
if u want that program show error when key isn't present in dictionary
then use 1st syntax 

otherwise if u want that program do not show error when the key value
isn't present then use 2nd syntax .
in 2nd syntax it will show NONE if key isn't present'''

print(dict.keys())
print(dict.values())