units=float(input("Enter the number of units you consumed: "))
if units < 50:
    amount= units * 3.75
    surcharge= 25
elif units <= 100:
    amount= 150 + ((units - 50) * 3.50)
    surcharge= 50
elif units <=200:
    amount= 200 + ((units - 100) * 3.00)
    surcharge= 75
else:
    amount = 150 + 162.50 + 526 + ((units - 200) * 5.00)
    surcharge= 100
total= amount + surcharge
print("The electricity bill is: %.2f" %total, "Taka")
Dollar= total/122  # Now the current rate of Dollar in Bangladesh is near about 122 Taka.
print('Or The electricity bill is : %.2f' %Dollar, "Dollar")