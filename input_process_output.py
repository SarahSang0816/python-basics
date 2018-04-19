# Convert elevator floor
# In Europe, floor 0 is the equivalent of floor 1 in the United States
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)

# Calculate pay
hour = input('Enter hour')
rate = input('Enter rate')
pay = float(hour) * float(rate)
print('Pay is: ', pay)
