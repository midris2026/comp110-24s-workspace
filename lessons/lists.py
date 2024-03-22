
#iniatilize an empty list
grocery_list: list[str] = list() # <- list constructur
grocery_list: list[str] = [] # <- literal
print(grocery_list)

#add item to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("after appending:")
print(grocery_list)

#create an already populated list(how to make a real string)
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("populated list: ")
print(grocery_list2)
grocery_list2.append("eggs")

#indexing lists
print("the first element of string")
print(grocery_list[0])

#modifying by index
print("before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print(grocery_list)

#remove item from a list
grocery_list.pop(1)
print("After removing almond milk: ")
print(grocery_list)

#function name: display
#parameter: list[str]
#return nothing
#print out the list

def display(a: list[str]) -> None:
    "returns nothing"
    print(a)
display(grocery_list)
display(["m","b","a"])

display(grocery_list)
x = display(["m","b","a"])
print(x)

#create list
#name: create
#parameters: str and str
#RV: list[str]
#Put both parameters into list and return that list
def create(a: str, b: str) -> list[str]:
    my_list: list[str] = [a, b]
    return my_list
print(create("Hello", "World"))