# Question: WAP to fill the given letter template with name and date

letter = '''
Dear <Name>,
YOU ARE SELECTED
<Date>
'''

name = input("enter name: ")
date = input("enter date: ")

letter = letter.replace("<Name>", name)
letter = letter.replace("<Date>", date)
print(letter)