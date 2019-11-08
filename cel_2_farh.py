def cel_to_fahr(cels):
    fahr = cels * 9/5 + 32
    return fahr
temperatures = [10, -20, 100]
for temp in temperatures:
    print(cel_to_fahr(temp))
