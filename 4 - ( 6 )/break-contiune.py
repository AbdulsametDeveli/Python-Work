name = 'Sadık Turan'

for letter in name:
    if letter == 'ı': 
        break
    print(letter)  #S a d 
    
x = 0 
while x < 5:
    x += 1
    if x == 2:
        continue
    print(x)
# 0 1 3 4 5
    
# 1- 100 e kadar tek sayilarin toplami

x = 1
result = 0
while x <= 100:
    x += 1
    if x % 2 == 0:
        continue
    result += x
    x += 2
print(f'Tek sayilarin toplami: {result}')