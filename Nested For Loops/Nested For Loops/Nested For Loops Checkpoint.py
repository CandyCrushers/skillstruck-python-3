rows = 3 
pets = ["Dog", "Snake", "Elephant", "Porkypine", "Alligator"]
list = [[j for j in pets] for i in range(rows)]
print(list)