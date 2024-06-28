# Print using index, index starts at 0.
countries = ["Brazil", "USA", "Australia"]

print(countries[1])

# Change values by accessing index
countries[1] = "Germany"
print(countries)

# Append 
countries.append("Fiji")
print(countries)

# Remove
countries.remove("Brazil")
print(countries)

# Len if called with list counts items, if called with word or string counts characters.
print(len(countries)) # Get the list length how many items the list contains = 3
print(len(countries[0])) # Counts how many characters in index 0 = "Germany" = 7