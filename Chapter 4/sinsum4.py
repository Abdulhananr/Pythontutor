from math import sin, pi
from sinesum2 import table  # Assuming sinesum2.py contains the table function
import argparse

# Initialize ArgumentParser object
parser = argparse.ArgumentParser()

# Define a function to evaluate command-line arguments as Python expressions
def eval_cml_arg(text):
    return eval(text)

# Add command-line arguments
parser.add_argument(
    '--n', '--n_list', type=eval_cml_arg, default='[1, 3, 5, 10, 30, 100]',
    help='List of n values')
parser.add_argument(
    '--alpha', '--alpha_list', type=eval_cml_arg, default='[0.01, 0.25, 0.49]',
    help='List of alpha values')
parser.add_argument('--T', type=eval_cml_arg, default='2*pi',
                    help='Domain of function')

# Parse the command-line arguments
args = parser.parse_args()

# Call the table function with the parsed arguments
table(args.n, args.alpha, args.T)

"""
Sample run:
python sinesum4.py --n '[1, 3, 5, 10, 30, 100]' --alpha '[0.01, 0.25, 0.49]' --T 2*pi
"""

# Explanation:
# 1. The code imports the necessary modules, including argparse for parsing command-line arguments.
# 2. An ArgumentParser object named parser is initialized.
# 3. A function eval_cml_arg is defined to evaluate command-line arguments as Python expressions using the eval function.
# 4. Command-line arguments (--n, --alpha, --T) are added to the parser with appropriate help messages.
# 5. The parse_args() method is called to parse the command-line arguments into an object named args.
# 6. The table function is called with the parsed arguments (n, alpha, T) to generate the sine sum table.
# 7. A sample run demonstrates how to use the script with different arguments.
# 8. Detailed comments provide explanations for each part of the code.
