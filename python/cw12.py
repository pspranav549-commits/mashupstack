try:
    title = input("paathummayude aadu: ")

    if not title.replace(" ", "").isalpha():
        raise ValueError("Error: Book title must contain only alphabets and spaces.")

    year = input("1989: ")

    if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
        raise ValueError("Error: Publication year must be a 4-digit number starting with 19 or 20.")

    print("\nBook Details Accepted")
    print("Title:", title)
    print("Publication Year:", year)

except ValueError as e:
    print(e)

finally:
    print("\nThank you for using the Mini Library System.")