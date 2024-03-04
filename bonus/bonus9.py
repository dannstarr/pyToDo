password = input("Enter a new password: ")
result = []

if len(password) >= 8:
    result.append(True)
    
has_num = False
for char in password:
   if char.isdigit():
       has_num = True
result.append(has_num)

has_upper = False
for char in password:
    if char.isupper():
        has_upper = True
result.append(has_upper)

print(result)

if all(result):
    print("Strong password")
else:
    print("weak")


