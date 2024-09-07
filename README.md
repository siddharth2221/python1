# Pyramid Pattern in Python

This Python script prints a pyramid pattern of stars (`*`). The height of the pyramid is determined by the value of `n`.

## Code

```python
n = 5
for i in range(1, n+1):
    # Print spaces
    print(' ' * (n - i), end='')
    # Print stars
    print('* ' * i)
