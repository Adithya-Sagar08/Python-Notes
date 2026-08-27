#11. Three Numbers in Ascending Order

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b:
    if b <= c:
        print("Ascending order:", a, b, c)
    else:
        if a <= c:
            print("Ascending order:", a, c, b)
        else:
            print("Ascending order:", c, a, b)
else:
    if a <= c:
        print("Ascending order:", b, a, c)
    else:
        if b <= c:
            print("Ascending order:", b, c, a)
        else:
            print("Ascending order:", c, b, a)


#12. Store Discount and Membership


amount = float(input("Enter purchase amount: "))
membership = input("Do you have membership? ")

if amount > 100:

    if membership == "yes":
        discount = 20
    else:
        discount = 10

else:
    discount = 0

final_amount = amount - (amount * discount / 100)

print("Discount:", discount, "%")
print("Final amount:", final_amount)


#13. Character Classification


ch = input("Enter character: ")

if ch.isalpha():

    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")

else:
    print("Neither")


#14. Book Recommendation


age = int(input("Enter age: "))
genre = input("Enter genre: ")

if age < 18:

    if genre == "Fantasy":
        print("Recommended book: Harry Potter")
    elif genre == "Mystery":
        print("Recommended book: Nancy Drew")
    else:
        print("Recommended book: The Little Prince")

else:

    if genre == "Mystery":
        print("Recommended book: Sherlock Holmes")
    elif genre == "Fantasy":
        print("Recommended book: The Hobbit")
    else:
        print("Recommended book: 1984")


#15. Movie Ticket Price


age = int(input("Enter age: "))
matinee = input("Is it a matinee show? ")

if age < 12:

    if matinee == "yes":
        price = 8
    else:
        price = 10

elif age > 65:

    if matinee == "yes":
        price = 8
    else:
        price = 10

else:

    if matinee == "yes":
        price = 12
    else:
        price = 15

print("Ticket price: $", price)
