# Define a nested list 'q'
q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

# Iterate over each sublist 'i' in 'q'
for i in q:
    # Iterate over the indices of sublist 'i'
    for j in range(len(i)):
        # Print the element at index 'j' of sublist 'i'
        print(i[j], end=' ')
