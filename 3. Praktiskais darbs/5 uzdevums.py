pirk_sum = float(input("Ievadi pirkumu summu: "))

if pirk_sum > 500 or pirk_sum == 500:
    atl1 = pirk_sum * 25/100
    pirk_sum = pirk_sum - atl1
elif pirk_sum > 200 or pirk_sum == 200:
    atl2 = pirk_sum * 15/100
    pirk_sum = pirk_sum - atl2

print("Pircejam jamaksa", pirk_sum, "eiro")


    

