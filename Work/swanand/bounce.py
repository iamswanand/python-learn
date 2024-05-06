height = 100
rebound_percentage = 3 / 5
for i in range(10):
    height = height * rebound_percentage
    print(i + 1, round(height, 4))
