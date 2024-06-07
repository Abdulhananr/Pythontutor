import sys

try:
    # Read the value of C from the command line arguments
    C = float(sys.argv[1])
except IndexError:
    # Handle case where no argument is provided
    print('C must be provided as a command-line argument')
    sys.exit(1)
except ValueError:
    # Handle case where the provided value is not a valid float
    print('C must be a pure number')
    sys.exit(1)

"""
Sample run:
python cml_exception.py
C must be provided as a command-line argument
python cml_exception.py a
C must be a pure number
python cml_exception.py 3
"""
