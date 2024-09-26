phone_book = {'Vladimir': 89086376658, 'Slava': 89086376659} #Ключ значение разделяеться : Эта пара один обьект
print(phone_book)

print(phone_book['Vladimir']) #Чтобы узнать значение обращаемся к ключу

phone_book['Vladimir']=1234567890 #Можем заменить значение
print(phone_book)

phone_book['Polina'] =987654321 #Если попытаться найти несуществующее значение, оно просто добавиться в список
print(phone_book)

del phone_book ['Polina'] #Чтобы удалить из списка, есть функция del
print(phone_book)

phone_book.update({'Charli': 2233457669, 'Ants': 8889765565}) #Чтобы добавить сразу несколько значений используем .update
print(phone_book)

print(phone_book.get('Vladimir'))
print(phone_book.get('Kamila'))
print(phone_book.get('Kamila', 'Такого ключа нет')) # get Показывает значение по указонному ключу. Если его не существует пишет None. В методе можно указать значение по умолчанию (последняя сточка)

phone_book.pop('Vladimir') #Метод уберает ключ и возвращает значение
print(phone_book)
#a = phone_book.pop('Vladimir')
#print(a)  #Ключ не видно но значение есть

