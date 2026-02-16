book_1 = "python basics"
price_1 = 450
book_2 = "data science intro"
price_2 = 600

total = price_1 + price_2

receipt = """book store receipt
book title: {} price:₹{}
book title: {} price:₹{}
total amount: ₹{}
thank you for shopping with us""".format(book_1, price_1, book_2, price_2, total)
print(receipt.upper())


