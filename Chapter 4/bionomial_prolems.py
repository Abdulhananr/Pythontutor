from binomial_distribution import binomial

print('What is the probability of getting two heads when '
      'flipping a coin 5 times?')
print(f'{binomial(2, 5, 0.5):.6f}\n')

print('What is the probability of getting four ones in a row '
      'when throwing a die?')
print(f'{binomial(4, 4, 1 / 6):.6f}\n')

print('What is the probability that a skier will experience a ski '
      'break during five competitions in a world championship?')
print(f'{1 - binomial(0, 5, 1 / 120):.6f}')

"""
What is the probability of getting two heads when flipping a coin 5 times?
0.312500

What is the probability of getting four ones in a row when throwing a die?
0.000772

What is the probability that a skier will experience a ski break during five
competitions in a world championship?
0.040978
"""
