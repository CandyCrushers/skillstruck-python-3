# Weekend


'''class Friday: 
    def __init__(self, activity, friend):
        self.activity = activity
        self.friend = friend

    def pictures(self): 
        print("We took so many pictures!")


thisWeekend = Friday("Movie", "Charlotte")

thisWeekend.money = 20 
thisWeekend.friend = "Shane"
print(thisWeekend.money)
print(thisWeekend.friend)
print(thisWeekend)'''

# ----------------------------------------------------------------------


# Shopping 

class Shopping:
    def __init__(self, item, quality):
        self.item = item
        self.quality = quality
        self.total = []  # Initialize self.total as an empty list

    def spending(self, cost):
        self.total.append(cost)  # Append the cost to the total list

# Create an instance of the Shopping class
sportStore = Shopping("Kayak", "High Quality")

# Call the spending method with different values
sportStore.spending(50)
sportStore.spending(75)
sportStore.spending(100)

# Print the total list
print(sportStore.total)  # Output: [50, 75, 100]
