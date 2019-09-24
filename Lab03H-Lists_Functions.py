lucky_numbers = [4, 8, 9, 18, 42, 56]
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"]

print(lucky_numbers)
print(friends)
print("\n")
# friends.extend(lucky_numbers)
# print(friends)

friends.append("Olek")
print(friends)

friends.insert(1, "Aleksander")
print(friends)
print("\n")
friends.remove("Olek")
friends.clear()
print(friends)

print("\n")
lucky_numbers = [4, 8, 9, 18, 42, 56]
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"]

friends.pop()
print(friends)

print(friends.index("Jane"))

print(friends.count("Jim"))

print("\n")
friends.sort()
lucky_numbers.sort()
print(lucky_numbers)
print(friends)
print("\n")

friends.reverse()
lucky_numbers.reverse()
print(lucky_numbers)
print(friends)
print("\n")

friends2 = friends.copy()
print(friends2)









