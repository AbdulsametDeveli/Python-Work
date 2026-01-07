numbers = [1, 2, 3, 4, 5]

""" print(numbers[0])   # Output: 1
print(numbers[1])   # Output: 2
print(numbers[2])   # Output: 3
print(numbers[3])   # Output: 4
print(numbers[4])   # Output: 5
 """
for a in numbers:
    print('Hello')
    
names = ['çınar', 'sadık', 'sena']

for name in names:
    print(f'my name is {name}')

name = 'Sadık Turan'
for n in name:
    print(n)
    
tuple = ((1,2), (1,3), (3,5), (5,7))
for a,b in tuple:
    print(a,b)
    
d = {'k1': 1, 'k2': 2, 'k3': 3}

for key, value in d.items():
    print(f'key: {key} value: {value}')
""" for item in d:
    print(item)  # çıktı anahtarları verir
     """