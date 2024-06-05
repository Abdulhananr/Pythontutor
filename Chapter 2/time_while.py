import time

# Part 1: Loop runs for 10 seconds
t0 = time.time()
while time.time() - t0 < 10:
    print('....I like while loops!')
    # time.sleep(2)
print('Oh, no - the loop is over.')

# Part 2: Loop runs until 10 seconds have elapsed
t0 = time.time()
while time.time() - t0 < 10:
    print('....I like while loops!')
    time.sleep(2)
print('Oh, no - the loop is over.')
