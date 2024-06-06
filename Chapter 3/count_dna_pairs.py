def count_dna_pairs(dna_sequence, pair):
    """
    Count the number of times a specific pair of nucleotides appears consecutively in a DNA sequence.
    
    Parameters:
    dna_sequence (str): The DNA sequence to be analyzed.
    pair (str): The pair of nucleotides to count in the sequence.
    
    Returns:
    int: The number of times the pair appears consecutively in the sequence.
    """
    # Convert the pair to a tuple for comparison
    nucleotide_pair = tuple(pair)
    # Initialize the counter
    count = 0
    # Iterate over the DNA sequence in pairs
    for nucleotide1, nucleotide2 in zip(dna_sequence[:-1], dna_sequence[1:]):
        # Check if the current pair matches the target pair
        if (nucleotide1, nucleotide2) == nucleotide_pair:
            count += 1
    return count

# Define the DNA sequence and the pair of nucleotides to count
dna_sequence = 'ATATGCGGACCTAT'
nucleotide_pair = 'AT'

# Print the number of times the pair appears in the DNA sequence
print(count_dna_pairs(dna_sequence, nucleotide_pair))

"""
Sample run:
python count_dna_pairs.py
3
"""
