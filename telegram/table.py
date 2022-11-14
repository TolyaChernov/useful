from prettytable import PrettyTable
table = PrettyTable()


table.field_names = ['Names', 'Agw', 'City']
table.add_row(['Alice', 20, 'Minsk'])
table.add_row(['Duck', 52, 'Gomel'])
table.add_row(['Nick', 18, 'Grodno'])

print(table)