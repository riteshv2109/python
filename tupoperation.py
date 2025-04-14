countries=("russia","usa","europe","uk")
temp=list(countries)

# adds item
temp.append("new york")
# remove item      
temp.pop(2)
# change item
temp[1]="newzealand"
countries=tuple(temp)
print(countries)