#1 This is the first program of the File
""" Store the following in a dictionaryionary: Book name (key), [number of pages, price, genre, publication]- for n
number of books.
Create a menu based program to:
• Display all the book names with the same publication sorted alphabetically in tabular form.
• Add the string: “Short story”, if the number of pages is less than 75 and genre is Novel. The string must
be placed after number of pages, within the list.
• Display the book details having the highest and the lowest price. """
def f1():
    dictionary={}
    n=int(input("Kindly enter the number of books required :\t"))
    for i in range(n):
        lis=[]
        name=input("Enter the book name:\t")
        pages=int(input("Enter the number of pages:\t"))
        lis.append(pages)
        price=int(input("Enter the price of the book:\t "))
        lis.append(price)
        genre=str(input("Enter the genre:\t"))
        lis.append(genre)
        publication=str(input("Enter the publication:\t"))
        lis.append(publication)
        dictionary.update({name:lis})
        dictionary.values()
        
   
    #1
    price_dict={}
    for key in sorted(dictionary.keys()):
        print (key,dictionary[key],end=" ")
        print("\r")
        price_dict.update({key:dictionary[key][1] })
    #3
    max_key = max(price_dict, key=price_dict.get) 
    min_key = min(price_dict, key=price_dict.get)

    print(" Book with the highest price is :\t",max_key)
    print(" Book with the lowest price is :\t",min_key)

    #2
    for key in sorted(dictionary.keys()):
        if(dictionary[key][0] < 75 and dictionary[key][2] == "Novel"):
            dictionary[key].append("Short Novel")

    print(" Revised Dictionary :\t")
    for key in sorted(dictionary.keys()):
        print (key,dictionary[key],end=" ")
        print("\r")


   
f1()