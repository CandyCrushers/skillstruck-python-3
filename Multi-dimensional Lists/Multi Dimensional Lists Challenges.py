# Secret Agent Name Generator 

'''first_names = ["Blaze", "Shadow", "Phoenix", "Raven"]
last_names = ["Steel", "Storm", "Knight", "Wolf"]

agent_names = []

for first in first_names:
    name_combinations = []
    
    for last in last_names:
        name_combinations.append(first + " " + last)
    
    agent_names.append(name_combinations)

print(agent_names)'''


# ----------------------------------------------------------------------

# Fruit Blender 


'''fruit_nam = input("Enter fruits").split()
combos = ["apple", "grape", "peach", "cinnamon", "vanilla"]
list = []

for y in fruit_nam: 
    combo = []
    for i in combos:
        full_combo = y + " " + i
        combo.append(full_combo)
    list.append(combo)

print(list)'''

# ----------------------------------------------------------------------

# Subtracting in a 2D List

'''rows = [int(n) for n in input("Input a list of numbers").split()]
cols = [2,5,10,100]
list = []

for x in rows: 
    row = []
    for y in cols: 
        substract = x - y 
        row.append(substract)
    list.append(row)

print(list)'''