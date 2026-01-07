#def square(num):return num * 2

numbers = [1, 3, 5, 9, 10, 4]

#result = list(map(lambda num: num ** 2, numbers))
#for item in map(square, numbers):
#    print(item)
    
#def check_even(num): return num % 2 == 0
check_even = lambda num: num % 2 == 0
#result = list(filter(chec_even, numbers))
#result = list(filter(lambda num: num % 2 == 0, numbers))

result = check_even(numbers[2])
print(result)