numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)  # Listenin en küçük elemanını döner
val = max(numbers)  # Listenin en büyük elemanını döner
val = min(letters)  # Alfabetik olarak en küçük eleman
val = max(letters)  # Alfabetik olarak en büyük eleman

val = numbers[3:6]  # İndeks 3'ten 5'e kadar olan elemanları döner
val = letters[2:5]  # İndeks 2'den 4'e kadar olan elemanları döner
numbers[4] = 40  # İndeks 4'teki elemanı 40 yapar
letters[1] = 'G'  # İndeks 1'deki elemanı 'G' yapar

val = numbers.count(10)  # Listede 10 sayısının kaç tane olduğunu döner
val = letters.count('a')  # Listede 'a' karakterinin kaç tane olduğunu döner
val = numbers.index(16)  # 16 sayısının indeksini döner
val = letters.index('b')  # 'b' karakterinin indeksini döner
numbers.sort()  # Liste elemanlarını küçükten büyüğe sıralar
letters.sort()  # Liste elemanlarını alfabetik olarak sıralar


numbers.reverse()  # Liste elemanlarının sırasını tersine çevirir
letters.reverse()  # Liste elemanlarının sırasını tersine çevirir
numbers.append(100)  # Listenin sonuna 100 değerini ekler
letters.append('z')  # Listenin sonuna 'z' karakterini ekler
numbers.insert(3, 78)  # 3. indekse 78 değer
numbers.remove(9)  # Listeden 9 değerini siler
letters.remove('s')  # Listeden 's' karakterini siler
numbers.pop()  # Listeden son elemanı siler
letters.pop()  # Listeden son elemanı siler

print(numbers)
print(letters)
val = numbers.copy()  # Listeyi kopyalar
print(val)
