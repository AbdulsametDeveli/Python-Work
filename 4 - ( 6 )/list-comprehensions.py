numbers = []
for x in range (10):
    numbers.apppend(x)
    
print(numbers)
# list comprehension
numbers = [x for x in range(10)]
print(numbers)

for x in range(10):
    print(x**2)
numbers = [x**2 for x in range(10)]
print(numbers) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

numbers  = [x**2 for x in range(10) if x % 3 ==0]
print(numbers) # [0, 9, 36, 81]

myString = 'Hello'
myList =[]
for letter in myString:
    myList.append(letter)
print(myList)  # ['H', 'e', 'l', 'l', 'o']
myList = [letter for letter in myString]
print(myList)  # ['H', 'e', 'l', 'l', 'o']

years = [1983, 1999, 2008, 1956, 1986]
ages = [2019 - year for year in years]
print(ages)  # [36, 20, 11, 63, 33]

result = [x if x % 2 ==0 else 'Tek' for x in range(1,10)]
print(result)  # ['Tek', 2, 'Tek', 4, 'Tek', 6, 'Tek', 8, 'Tek']

results = []
for x in range (3):
    for y in range(3):
        results.append((x,y))
print(results)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]