x = int(input ("Введите порядковый номер месяца: "))
month_to_season = x
if x < 3 or x==12:
      print("Зима")
elif 3 <= x < 6 :
      print("Весна")
elif 6 <= x < 9 :
      print("Лето")
elif 9 <= x <= 11 :
      print("Осень")
