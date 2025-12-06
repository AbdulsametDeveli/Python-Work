#message = 'Hello There. My Name is Sadik Turan'.split()
#print(message[0]) # Hello
 
#my_list = [1, 2, 3]
#my_list = ['bir', 2, True, 5.6]
#print(len(my_list))  # 4

list1 = ['one', 'two', 'three']
list2 = ['four', 'five', 'six']

Numbers = list1 + list2
print(Numbers)  # ['one', 'two', 'three', 'four', 'five', 'six']
print (len(Numbers))  # 6
print(Numbers[0])  # one
print(Numbers[2])  # three

userA = ['Sadik', 36]
userB = ['Cinar', 2]

users = [userA, userB]
print (userA)  # ['Sadik', 36]
print (userB)  # ['Cinar', 2]
print (users)  # [['Sadik', 36], ['Cinar', 2]]

print(users[1])  # ['Cinar', 2]
print(users[1][0])  # Cinar