#Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

ticket = int(input("Введите числа с билета"))
polovina_one = ticket % 10
ticket = ticket // 10 
polovina_one = (ticket % 10) + polovina_one
ticket = ticket // 10 
polovina_one = (ticket % 10) + polovina_one
ticket = ticket // 10 
polovina_two = ticket % 10
ticket = ticket // 10 
polovina_two = (ticket % 10) + polovina_two
ticket = ticket // 10 
polovina_two = (ticket % 10) + polovina_two
if polovina_one == polovina_two:
    print("Ваш билет счастливый")
else:
    print("Ваш билет не счастливый")    
  
