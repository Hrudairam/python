#regex
#regular expression are power ful tolls(modules) in python which is used to find a pattern with in given strings or statements or files we mainly used for text manipulatioon
'''a="codegnan\nis\tin\nvja"
print(a)'''

#rstring
'''a=r"codegnan\nis\nvja"
print(a)'''

#compile(),searc(),findall(),split(),sub()
#sequence characters
'''\w->it matches alphanumeric
\W->it matches non-alphanumeric
\d->it matches any digit
\D->it matches non digit
\s->it reprsents white spaces
\S->it reprsents non-white spaces'''

#compile()
'''a="maths map cat code cash money mat cap dog donkey"
b=re.compile(r"m\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)'''

'''d=re.search(r"m\w+",a)
print(d)'''


'''#sub()
d=re.sub(r"maths","science",a)
print(d)'''

#import re
'''a="year 2026 month 2 date 16"
b=re.findall(r"\d+",a)
print(b)'''

'''a="year 2026 month 2 date 16"
b=re.findall(r"\D+",a)
print(b)'''

#bmi
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))
if bmi < 18.5:
    print("Category: Underweight")
elif bmi >= 18.5 and bmi < 24.5:
    print("Category: Healthy Weight")
elif bmi >= 24.5 and bmi < 29.5:
    print("Category: Overweight")
else:
    print("Category: Obesity")


































