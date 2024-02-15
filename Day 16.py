from prettytable import PrettyTable
table= PrettyTable()
table.add_column("Pokemon", ["Squirtle", "Chandamer"])
table.add_column("Power", ["Water", "Fire"])
table.align="c"
print(table)
