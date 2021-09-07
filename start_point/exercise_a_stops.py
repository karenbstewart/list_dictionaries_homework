stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St" )
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont" )
#4. Print out the index position of "Linlithgow"
stop_count = stops.index("Linlithgow")
print("Linlithgow appears at index position ", stop_count, " in the list")
#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
#6. Delete "Cumbernauld" from the list by index
stops.pop(2)
#7. Print the number of stops there are in the list
num_of_stops = len(stops)
print("There are ",num_of_stops, " stops on the list.")
#8. Sort the list alphabetically
alphabetically = sorted(stops)
#9. Reverse the positions of the stops in the list
alphabetically.reverse()
#10 Print out all the stops using a for loop
for stops in alphabetically:
    print(stops)