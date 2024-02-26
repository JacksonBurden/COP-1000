itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00
profit = retailPrice - wholesalePrice
percentage = 25
salePrice = retailPrice * (1 - percentage / 100)
saleProfit = salePrice - wholesalePrice
print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))