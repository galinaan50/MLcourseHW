from tkinter import ROUND


w=int(input('въведи тегло в кг'))
h=int(input('въведи височина в м.'/100))
BMI=w/(h*h)
ser=round(BMI,2)
print(f'Вашия индекс e ={ser}')

