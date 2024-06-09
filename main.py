from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
def correct_name(contacts_list):
    for contact in contacts_list:
        full_name = ' '.join(contact[:3]).split()
        contact[:3] = full_name + [''] * (3 - len(full_name))
    return contacts_list

def correct_phone(contacts_list):
    pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    res = r'+7(\2)\3-\4-\5\7\8\9'
    for contact in contacts_list:
        contact[5] = re.sub(pattern, res, contact[5])
    return contacts_list

def remove_duplicates(contacts_list):
    correct_contacts_list = {}
    for contact in contacts_list:
        key = (contact[0], contact[1])
        if key not in correct_contacts_list:
            correct_contacts_list[key] = contact
        else:
            for i in range(len(contact)):
                if contact[i] and not correct_contacts_list[key][i]:
                    correct_contacts_list[key][i] = contact[i]
    return list(correct_contacts_list.values())

new_contacts_list = remove_duplicates(correct_name(correct_phone(contacts_list)))

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list)