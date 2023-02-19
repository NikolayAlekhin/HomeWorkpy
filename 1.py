#Найдите сумму цифр трехзначного числа.

namber= int(input('Введите число:'))
a = namber % 10
namber = namber // 10
b = namber % 10
namber = namber // 10 
c = namber % 10 
print (a + b + c)