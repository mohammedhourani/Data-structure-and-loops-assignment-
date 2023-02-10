keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Initialize an empty dictionary
dictionary = {}

# Iterate over the lists and add the elements to the dictionary
for key, value in zip(keys, values):
    dictionary[key] = value

print(dictionary)  # Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
