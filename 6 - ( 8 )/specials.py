mylist = [1, 2, 3]
myString = 'my string'

# Temel tiplerin davranışlarını inceleme
print(len(mylist))
print(len(myString))
print(type(mylist))
print(type(myString))

class Movie():
    # Yapıcı Metot (Constructor): Obje oluşturulurken çalışır.
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu.')

    # String Metodu: Objeyi yazdırdığımızda (print) ne görüneceğini belirler.
    def __str__(self):
        return f"{self.title} by {self.director}"

    # Length Metodu: len() fonksiyonu çağrıldığında ne döneceğini belirler.
    def __len__(self):
        return self.duration

    # Silici Metot (Destructor): Obje bellekten silindiğinde çalışır.
    def __del__(self):
        print('film objesi silindi')

# --- Kullanım ---

# duration (süre) kısmına integer (tam sayı) veriyoruz ki len() hata vermesin.
m = Movie('film adı', 'yönetmen adı', 120)

# __str__ metodu sayesinde anlamlı bir yazı çıkar:
print(str(m))  # Çıktı: film adı by yönetmen adı

# __len__ metodu sayesinde filmin süresini alırız:
print(len(m))  # Çıktı: 120

# Objeyi manuel olarak silmek istersek:
# (Bunu yazmasak bile program bittiğinde otomatik silinir ve mesaj yazar)
del m