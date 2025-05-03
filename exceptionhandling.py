a=input("enter the number=")
print(f"multiplication table for {a} is:")

try:
  for i in range(1,11):
     print(f"{int(a)}X {i} = {int(a)*i}")
     
     
except Exception as e:
    print(e)
    
print("this isn't going to be run if some error occurs above")