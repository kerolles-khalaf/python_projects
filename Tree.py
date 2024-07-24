# Get tree height from user
height = int(input('Enter height of tree: '))
row = 0
while row < height:
    count = 0
    while count < height - row:
        print(end=' ')
        count += 1
# Print out stars, twice the current row plus one:
# 1. number of stars on left side of tree
# = current row value
# 2. exactly one star in the center of tree
# 3. number of stars on right side of tree
# = current row value
    count = 0
    while count < 2*row + 1:
        print(end='*')
        count += 1
    print()
    row += 1