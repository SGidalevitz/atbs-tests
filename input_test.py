import pyinputplus as pyip
import random
# sandwich maker

def is_greater_than_0(num):
    if (num == 0):
        raise Exception(f"{num} is not greater than 0.")
    return int(num)


bread = pyip.inputMenu(["sourdough", "white", "multigrain"])
protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu", "tuna"])
cheese_wanted = pyip.inputYesNo("Do you want cheese\n")
cheese = "no cheese"
if (cheese_wanted == "yes"):
    cheese = pyip.inputMenu(["cheddar", "swiss", "mozzarella"])
extras = ["mayo", "mustard", "lettuce", "tomato"]
extras_wanted = [False] * 4
for i, extra in enumerate(extras):
    want_this_extra = pyip.inputYesNo(f"Do you want {extra}?\n") == "yes"
    extras_wanted[i] = want_this_extra
print("How many sandwiches?")
sandwich_count = pyip.inputCustom(is_greater_than_0)
print(f"Order {random.randint(1000,9999)}: {sandwich_count} sandwiches - ingredients: {[bread, protein, cheese] + [extras[i] for i,condition in enumerate(extras_wanted) if (condition)]}")