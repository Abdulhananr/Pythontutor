import sys
from math import *
from ast import literal_eval

def main():
    """
    Main function to read two command line arguments, evaluate them as mathematical expressions,
    and print their types and summed value.
    """
    try:
        # Read command line arguments and evaluate them as expressions
        input1 = literal_eval(sys.argv[1])
        input2 = literal_eval(sys.argv[2])
    except IndexError:
        # If there are not enough command line arguments, print an error message and exit
        print('input1 and input2 must be given on the command line')
        sys.exit(1)
    except (ValueError, SyntaxError):
        # If the arguments cannot be evaluated, print an error message and exit
        print('Invalid input: inputs must be valid Python expressions')
        sys.exit(1)

    # Sum the evaluated inputs
    result = input1 + input2

    # Print the types of the inputs and the result, along with the result value
    print(f'{type(input1)} + {type(input2)} becomes {type(result)}\nwith value {result}')

if __name__ == "__main__":
    main()

"""
Sample run:
python add_cml2.py 'sqrt(2)' 'sin(1.2)'
<class 'float'> + <class 'float'> becomes <class 'float'>
with value 2.34625264834
"""
