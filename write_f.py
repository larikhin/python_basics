with open('new.txt', 'w') as f:
    olimpics = [2016, 2020, 2024]
    for year in olimpics:
        f.write(str(year))
        f.write('\n')
