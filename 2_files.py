"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    text_len = len(text)
    print(f"Длина получившейся строки: {text_len}")
    words_number = len(text.split())
    print(f"количество слов в тексте: {words_number}")
    text_new = text.replace(".","!")
    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(text_new)

if __name__ == "__main__":
    main()
