# Pyramid Pattern
n = 5
for i in range(1, n+1):
    # Print spaces
    pt(' ' * (n - i), end='')
    # Print stars
    print('* ' * i)
