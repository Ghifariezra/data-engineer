"""
    1. Tuliskan skrip Python yang mencetak angka dari 1 sampai 10 menggunakan
    loop for
"""

# Action
for i in range(1, 11):
    print(i)

"""
    2. Buatlah fungsi Python dengan nama is_even yang menerima sebuah integer
    sebagai argumen dan mengembalikan True jika angka tersebut genap dan
    False jika ganjil.
"""

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(11))

"""
    3. Tulislah sebuah fungsi Python sum_list yang menerima sebuah list angka
    sebagai argumen dan mengembalikan jumlah dari semua angka dalam list
    tersebut. Gunakan loop for untuk mengiterasi list.
"""

def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_list([1, 2, 3, 4]))

"""
    4. Kembangkan sebuah fungsi Python yang disebut find_min_max yang menerima
    sebuah list integer dan mengembalikan sebuah tuple yang mengandung angka
    terkecil dan terbesar dari list tersebut. Jangan gunakan fungsi bawaan min()
    atau max(), melainkan gunakan loop for untuk mengiterasi list.
"""

def find_min_max(numbers):
    min_num = numbers[0]
    max_num = numbers[0]
    for number in numbers:
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number
    return (min_num, max_num)

print(find_min_max([1, 2, 3, 4]))

"""
    5. Tuliskan sebuah fungsi Python group_characters yang menerima sebuah string
    dan mengembalikan sebuah kamus di mana kunci adalah karakter dalam string
    dan nilai adalah jumlah kemunculan karakter tersebut dalam string tersebut.
"""

def group_characters(string):
    characters = {}
    for character in string:
        if character in characters:
            characters[character] += 1
            print(characters)
        else:
            characters[character] = 1
            print(characters)
    return characters

print(group_characters("hello world"))