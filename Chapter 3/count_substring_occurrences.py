def count_substring_occurrences(dna_sequence, substring):
    """
    Count the number of times a specific substring appears in a DNA sequence.
    
    Parameters:
    dna_sequence (str): The DNA sequence to be analyzed.
    substring (str): The substring to count in the sequence.
    
    Returns:
    int: The number of times the substring appears in the sequence.
    """
    count = 0
    substring_length = len(substring)
    for index in range(len(dna_sequence) - substring_length + 1):
        if dna_sequence[index:index + substring_length] == substring:
            count += 1
    return count

# Define the DNA sequence and the substring to count
dna_sequence = 'ATATGCGGATACCTATA'
substring = 'ATA'

# Print the number of times the substring appears in the DNA sequence
print(count_substring_occurrences(dna_sequence, substring))

"""
Sample run:
python count_substring_occurrences.py
3
"""
