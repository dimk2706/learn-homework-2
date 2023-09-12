import csv
"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    users= [
            {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
            {'name': 'Вася', 'age': 18, 'job': 'Programmer'}, 
            {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
            {'name': 'Миша', 'age': 23, 'job': 'Programmer'},
            {'name': 'Женя', 'age': 34, 'job': 'Scientist'},
        ]
    with open('export.csv', 'w', encoding='windows-1251', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in users:
            writer.writerow(user)

if __name__ == "__main__":
    main()
