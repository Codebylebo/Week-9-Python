fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

fruits[0] = "kiwi"  # Change the first item
print(fruits)  # Output: ['kiwi', 'banana', 'cherry']

fruits = ["kiwi", "melon", "mango"]
fruits.append("orange")  # Add an item to the end
print(fruits)  # Output: ['kiwi', 'melon', 'mango', 'orange']

fruits.insert(1, "lemon")  # Add an item at a specified index
print(fruits)  # Output: ['kiwi', 'lemon', 'melon', 'mango', 'orange']

fruits.remove("melon")  # Remove an item by value
print(fruits)  # Output: ['kiwi', 'lemon', 'mango', 'orange']

fruits.pop()  # Remove the last item
print(fruits)  # Output: ['kiwi', 'lemon', 'mango']

#sorting
fruits = ["banana", "apple", "orange", "cherry"]
fruits.sort()  # Sort the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.reverse()  # Reverse the list / fruits.sort(reverse=True)  # Sort in descending order
print(fruits)  # Output: ['orange', 'cherry', 'banana', 'apple']
