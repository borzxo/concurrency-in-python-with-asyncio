quantity = int(input("Listing quantity -> "))
chapter = int(input("Chapter number -> "))
for i in range(1, quantity+1):
    name = f'listing_{chapter}_{i}.py'
    with open(name, 'w') as file:
        file.close()
