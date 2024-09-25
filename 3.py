tuple_ = 1,2,3,4
tuple_2 = (1,2,3,4)
tuple_3 = tuple([1, 2, 3, 4])
print(type(tuple_))
print(tuple_2)
print(tuple_3)

tuple_0 = 1,2,3,4, True, 'String' #Кортедж. Не изменить, но занимает мало памяти
list_= [1,2,3,4, True, 'String'] #Список. Можно изменить но занимает много памяти
print(tuple_0.__sizeof__())
print(list_.__sizeof__())

tuple_7 = ([1, 2], 0)
print(tuple_7)
tuple_7[0][0] = 200 #Так храним список в кортедже
print(tuple_7)
