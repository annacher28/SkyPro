is_year_leap = int(input ("Введите год (числом): "))

is_year = is_year_leap % 4 == 0
    

print ("Год", is_year_leap,":", is_year )
