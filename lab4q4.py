#Part a
my_dict = {}
for i in range(1, 31):
    my_dict[i] = (i ** 2) - 1
print(my_dict)

#Part b
for key, value in my_dict.items():
    print(f"{key}: {value}")

#Part c
total = 0
for value in my_dict.values():
    total += value
    
#Part d
keyForRemove = int(input("Enter a key to remove from the dictionary: "))
if keyForRemove in my_dict:
    del my_dict[keyForRemove]
    print("The key" + keyForRemove +" has been removed from the dictionary.")
else:
    print("The key" + keyForRemove + " is not present in the dictionary.")

print("Updated dictionary:", my_dict)