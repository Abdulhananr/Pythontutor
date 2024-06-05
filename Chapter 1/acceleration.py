velocity = 3  # initial velocity (m/s)
time = 1  # time (s)
acceleration = 2  # acceleration (m/s^2)

# calculate distance traveled
results = velocity * time + 0.5 * acceleration * time ** 2

print(results)  # print the result


"""
This code calculates the distance traveled by an object under constant acceleration, using the formula:

s = v0t + 0.5at^2

where:
- s is the distance traveled (m)
- v0 is the initial velocity (m/s)
- t is the time (s)
- a is the acceleration (m/s^2)

"""