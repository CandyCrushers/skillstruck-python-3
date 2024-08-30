# Multiply by the Number of Rows

'''mylist = [1, 2, 3, 4, 5]
num_rows = int(input("How many rows do you want? "))
result = [[x * num_rows for x in mylist] for _ in range(num_rows)]
print(result)'''

# -----------------------------------------------------------------------


# Weather Watcher

'''rows = input("Input a list of weather").split()
cols = ["windy", "breezy", "calm"]


result = [[f"{weather} {wind}" for wind in cols] for weather in rows]

print(result)'''