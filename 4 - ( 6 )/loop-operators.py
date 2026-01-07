
for item in range(10):
    print(item)

print(list(range(5,100,10)))

# enumerate
index = 0 
greeting = 'Hello'
for index, item in enumerate(greeting):
    print(f'index: {index} letter: {item}')
    
    
# zip
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
for item in zip(list1, list2):
    print(item)
    