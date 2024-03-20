# Suppose log_results is an empty dictionary
log_results = {}

# Update log_results with a new key-value pair
key = "name"
element_text = "Alice"
log_results.update(key, element_text)

# Now log_results is {'name': 'Alice'}
print(log_results)

# Update log_results with another key-value pair
key = "age"
element_text = 25
log_results.update(key, element_text)

# Now log_results is {'name': 'Alice', 'age': 25}
print(log_results)

# Update log_results with an existing key
key = "name"
element_text = "Bob"
log_results.update(key, element_text)

# Now log_results is {'name': 'Bob', 'age': 25}
print(log_results)
