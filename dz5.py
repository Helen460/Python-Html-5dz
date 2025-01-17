#1. Підрахувати середню довжину слова у введеному реченні.
sentence = input("Введіть речення: ")
length = len(sentence)
word_count = sentence.count(" ") + 1
print("Середня довжина слова: ", length / word_count)

#2. Підрахувати, скільки разів певне слово міститься в рядку тексту.
text = input("Введіть текст: ")
word = input("Введіть слово для пошуку: ")
word_count = text.lower().split().count(word.lower())
print("Слово: ", word,  "міститься в рядку тексту: ", word_count)

#3. Напишіть програму, яка генерує пароль вказаної довжини.
import random
import string
length = int(input("Введіть довжину пароля: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for _ in range(length))
print("Пароль: ", password)

#4. Визначити, яка буква в тексті зустрічається найчастіше.
text = input("Введіть текст: ")
text = text.lower()
letters = [char for char in text if char.isalpha()]
letter_counts = []
for letter in set(letters):
    count = letters.count(letter)
most_common_letter = max(set(letters), key=letters.count)
print("Найчастіше зустрічається буква: ", most_common_letter)

#5. Написати програму, яка перевіряє коректність email, вказаного з клавіатури.
email = input("Введіть email: ")
if email.startswith("@") or email.endswith("@"):
    print("Невірний email: email не може починатися або закінчуватися на '@'.")
else:
    if "@" in email:
        local_part, domain_part = email.split("@", 1)
        if "." in domain_part and domain_part.count(".") >= 1:
            domain_part = domain_part.replace(".", "", 1)
            if len(domain_part) >= 2:
                print("Email введено правильно.")
            else:
                print("Невірний email: після крапки має бути не менше двох літер.")
        else:
            print("Невірний email: має бути хоча б одна крапка після '@'.")
    else:
        print("Невірний email: відсутній символ '@'.")

#6. Написати програму, яка підраховує кількість слів, а також голосних і приголосних літер у рядку, введеному користувачем. Додатково вивести кількість знаків пунктуації, цифр та інших символів. Урахувати, що між словами (а також до і після слів) може бути більше одного пробілу. Приклад виводу програми:
#Загалом символів у рядку тексту – 38, з них:
#Слів – 6
#Голосних літер - 12
#Приголосних літер - 21
#Знаків пунктуації - 2
#Цифр – 0
#Інших символів – 3

import string
text = input("Введіть текст: ")
vowels = "аеєєиіїоуюяАЕЄЄИІЇОУЮЯ"
consonants = "бвгґдеєжзийклмнопрстуфхцчшщьюяБВГҐДЕЄЖЗИЙКЛМНПРСТУФХЦЧШЩЬЮЯ"
punctuation = string.punctuation
digits = "0123456789"
word_count = 0
vowel_count = 0
consonant_count = 0
punctuation_count = 0
digit_count = 0
other_count = 0

text = text.strip()
index = 0
text_len = len(text)

while index < text_len:
    if text[index].isalpha():
        word_count += 1
        while index < text_len and (text[index].isalpha() or text[index].isdigit()):
            index += 1
    else:
        index += 1

index = 0
while index < text_len:
    char = text[index]
    
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    elif char in punctuation:
        punctuation_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        other_count += 1
    
    index += 1
print("Загалом символів у рядку тексту – ", len(text), "з них:")
print("Слів – ", word_count)
print("Голосних літер - ", vowel_count)
print("Приголосних літер - ", consonant_count)
print("Знаків пунктуації - ", punctuation_count)
print("Цифр – ", digit_count)
print("Інших символів – ", other_count)

#7. Напишіть програму, яка буде друкувати ромбоподібний малюнок на основі введеного рядка (максимальна довжина – 50 символів). Приклад виводу, якщо рядок «testing»:
#       t
#      te
#     tes
#    test
#   testi
#  testin
# testing
# esting
# sting
# ting
# ing
# ng
# g

import os
os.system('cls')
text = input("Введіть рядок (максимум 50 символів): ")
for i in range(len(text)):
    print(" " * (len(text) - i - 1) + text[:i + 1])
    
for i in range(1, len(text)):
    print(" " * i + text[i:])

text = input("Введіть рядок: ")

#8. Визначити, чи є рядок паліндромом. Приклади паліндромів:
# І розморозь зором зорі
# Жара. Літо. Голого тіла раж.
# Ущипне — та шатен: пищу!
# А баба на волі — цілована баба
# Три психи пили Пилипихи спирт.
# Кіт утік.
# І що сало? Ласощі…
# О, гомін німого
# А мене нема…

import re
text = input("Введіть рядок: ")
cleaned_text = re.sub(r'[\s.,!?;:()\-"]', '', text).lower()
reversed_text = cleaned_text[::-1]
if cleaned_text == reversed_text:
    print("Рядок є паліндромом.")
else:
    print("Рядок не є паліндромом.")

#9. Показати на екрані фразу «ЦЕ СПАМ!», якщо введений з клавіатури рядок містить слова типу "кредит", "швидке схвалення", "готівка", "знижка", "розпродаж",
#  "виграш", "viagra", "схуднення", "найкращий продукт", "легкий заробіток", "без ризику", "швидкі гроші", "виграй гроші", "гроші за реєстрацію", "легко і 
# швидко", "терміново", "тільки сьогодні", "суперпропозиція", "не втратьте шанс", "подарунки для вас", "нові знижки" i тд. В іншому випадку показати фразу 
# «це не спам». Регістр рядка не має значення.
spam = [
    "кредит", "швидке схвалення", "готівка", "знижка", "розпродаж", "виграш",
    "viagra", "схуднення", "найкращий продукт", "легкий заробіток", "без ризику",
    "швидкі гроші", "виграй гроші", "гроші за реєстрацію", "легко і швидко",
    "терміново", "тільки сьогодні", "суперпропозиція", "не втратьте шанс",
    "подарунки для вас", "нові знижки"
]
text = input("Введіть рядок: ")
text_lower = text.lower()
is_spam = any(word in text_lower for word in spam)
if is_spam:
    print("ЦЕ СПАМ!")
else:
    print("ЦЕ НЕ СПАМ!")