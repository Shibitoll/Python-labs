# Заданий текст
text = "           Exploring the lush rainforests of Costa Rica is an unforgettable adventure. The vibrant colors of exotic birds and the soothing sounds of cascading waterfalls create a sensory wonderland. Trekking through dense foliage, you'll encounter diverse wildlife, from playful monkeys to elusive jaguars. Costa Rica's commitment to sustainability is admirable. Eco-friendly lodges and eco-tours ensure minimal environmental impact. You can also savor delicious local cuisine, like Gallo Pinto, a traditional rice and bean dish. Whether you're ziplining through the treetops or relaxing on pristine beaches, Costa Rica offers a perfect blend of natural beauty and cultural richness. It's a paradise for nature enthusiasts and adventurers alike.    "


#ЧАСТИНА 1 //ВАСИЛЕНКО
# Використовуємо функцію split() для розділення тексту на слова
words = text.split()

# Використовуємо функцію strip() для видалення зайвих пробілів з початку і кінця тексту
stripped_text = text.strip()

# Замінити слово "Costa Rica" на "Beautiful Costa Rica" за допомогою функції replace()
modified_text = text.replace("Costa Rica", "Beautiful Costa Rica")

# Вивести результати
print("\nФункція 1: \nТекст розділений на слова: ", words)
print("\nФункція 2: \nТекст без зайвих пробілів: ", stripped_text)
print("\nФункція 3: \nТекст із заміною словосполучення: ", modified_text)

#ЧАСТИНА 2 //Отрох

# Використовуємо функцію map(), щоб пройтися по масиву слів і capitalize() для того, щоб першу літеру зробити великою

def capitalizeWords(n):
    return n.capitalize()

capitalized_words = map(capitalizeWords, words)

# Використовуємо функцію join() щоб об'єднати список заданим символом і отримати з цього рядок

formatted_text = ' |♂| '.join(words)

# Використовуємо функції chr() та ord() для шифрування тексту у код Цезаря з поточним здвигом в 3 літери.

def caesar_cipher(text, shift):
    encryption = ""
    for char in text:
        if char.isalpha():  # перевіряємо, чи символ є буквою
            shift_amount = shift % 26  # обмежуємо сдвиг від 0 до 25
            if char.isupper():
                new_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            else:
                new_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            encryption += new_char
        else:
            encryption += char  # лишаємо символи, які не є буквами без змін
    return encryption

shift = 3 # визначення кількості здвигу
encryption = caesar_cipher(text, shift)


# Вивести результати
print("\nФункція 4: \nТекст зі словами з великої літери:\n ", list(capitalized_words))
print("\nФункція 5: \nВідформатований текст:\n ", formatted_text)
print("\nФункція 3: \nЗашифрований текст:\n ", encryption)


#ЧАСТИНА 3 // Медвідь Дмитро

# Першу букву кожного слова переводить в верхній регістр, а всі інші в нижній
x = text.title()

# Перетворення рядка до верхнього регістру
y = text.upper()

# Перетворення рядка до нижнього регістру
z = text.lower()

# Вивести результати
print("\nФункція 7: \nПершу букву кожного слова переводить в верхній регістр: ", x)
print("\nФункція 8: \nПеретворення рядка до верхнього регістру: ", y)
print("\nФункція 9: \nПеретворення рядка до нижнього регістру: ", z)

#Частина 4 // Бондарєв Іван

# Обертаємо текст задом наперед за допомогою зрізів рядків
reversed_text = text[::-1]

# Перетворити текст на список символів
text_list = list(text)

from collections import Counter
# Розділити текст на слова
words = text.split()

# Знайти кількість входжень кожного слова
word_counts = Counter(words)

# Вивести результат
print("Текст задом наперед:", reversed_text)
print("Список символів тексту:", text_list)
print("Кількість повторювання слова:", word_counts)