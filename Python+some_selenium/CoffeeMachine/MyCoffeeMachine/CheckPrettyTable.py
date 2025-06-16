from prettytable import PrettyTable

table = PrettyTable()
print(table)
table.add_column("Pokemon Name:", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'r'
table.left_padding_width = 10
table.right_padding_width = 5
print(table)
