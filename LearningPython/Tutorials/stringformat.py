# they use {} instead of %
price = 49
instead_price = 100
txt = "The price is {} dollars instead of {} dollars"
print(txt.format(price, instead_price))

txt = "The price is {:.13f} dollars instead of {:.2f} dollars"
print(txt.format(price, instead_price))

txt = "The price is {} dollars instead of {:.2f} dollars" # you can't mix 
# float specifiers with numbers indicating which variable to use
print(txt.format(price, instead_price))

txt = "The price is {1} dollars instead of {0} dollars"
print(txt.format(price, instead_price))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))