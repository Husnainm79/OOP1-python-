#Husnain Manzooor
#261 933 726

#question 1

class Library:
    def __init__(x):
        x.books = []

    def add_book(x, title, author, publication_year):
        book = Book(title, author, publication_year)
        x.books.append(book)
        return book

    def remove_book(x, book):
        x.books.remove(book)

    def list_books(x):
        for book in x.books:
            print(f"{book.title} by {book.author}, published in {book.publication_year}")

    def checkout_book(x, book, borrower):
        book.checkout(borrower)

    def checkin_book(x, book):
        book.checkin()


class Book:
    def __init__(x, title, author, publication_year):
        x.title = title
        x.author = author
        x.publication_year = publication_year
        x.borrowers = []

    def checkout(x, borrower):
        if borrower in x.borrowers:
            print("Book has been checked out already.")
        else:
            x.borrowers.append(borrower)
            borrower.checkout(x)
            print(f"{self.title} has been checked out by {borrower.name}.")

    def checkin(x):
        if len(x.borrowers) == 0:
            print("Book has been checked in already.")
        else:
            borrower = x.borrowers.pop()
            borrower.checkin(x)
            print(f"{x.title} has been checked in by {borrower.name}.")

    def list_borrowers(x):
        for borrower in x.borrowers:
            print(f"{borrower.name} ({borrower.id})")


class Borrower:
    def __init__(x, name, id):
        x.name = name
        x.id = id
        x.books = []

    def checkout(x, book):
        x.books.append(book)

    def checkin(x, book):
        x.books.remove(book)

    def list_books(x):
        for book in x.books:
            print(book.title)



library = Library()


book1 = library.add_book("The Great Cristiano Ronaldo", "M.H.Manzoor", 2017)
book2 = library.add_book("To sabotage old trafford", "Leo ,Messi", 2019)
book3 = library.add_book("2022", "SIUUUUUU", 2023)


library.list_books()


borrower1 = Borrower("Husnain", 1)
borrower1

#q2
class Bird:
    def __init__(y, name, color, gender):
        y.name = name
        y.color = color
        y.gender = gender

    def get_name(y):
        return y.name

    def set_name(y, name):
        y.name = name

    def get_color(y):
        return y.color

    def set_color(y, color):
        y.color = color

    def get_gender(y):
        return y.gender

    def set_gender(y, gender):
        y.gender = gender

    def display(y):
        print(f"Name: {y.name}, Color: {y.color}, Gender: {y.gender}")


class Cage:
    def __init__(y, cage_no, size):
        y.cage_no = cage_no
        y.size = size
        y.birds = []

    def add_bird(y, bird):
        y.birds.append(bird)

    def delete_bird(y, bird):
        y.birds.remove(bird)

    def display_cage_data(y):
        print(f"Cage No: {y.cage_no}, Size: {y.size}")
        print("Birds:")
        for bird in y.birds:
            bird.display()

bird1 = Bird("hawk", "Brown", "Male")
bird2 = Bird("Peacock", "Green and blue", "Female")
bird3 = Bird("Crow", "Grey and black", "Male")


bird1.display()


cage = Cage(1, "Large")
cage.add_bird(bird1)
cage.add_bird(bird2)


cage.display_cage_data()


cage.delete_bird(bird1)


cage.display_cage_data()
#q3
class Company:
    def __init__(z, name, business_type, hq_address):
        z.name = name
        z.business_type = business_type
        z.hq_address = hq_address
        z.employees = []

    def add_employee(z, employee):
        z.employees.append(employee)


class Employee:
    def __init__(z, name, address, cell_number):
        z.name = name
        z.address = address
        z.cell_number = cell_number


def main():
    
    company = Company("SIUUUUU.", "Software", "Behind dogar restauarant phase 5")

  
    employee1 = Employee("Cristiano Ronaldo", "al nassr", "456-7891")
    employee2 = Employee("Leo Messi", "psg", "156-4879")
    company.add_employee(employee1)
    company.add_employee(employee2)

    
    print(f"Company Name: {company.name}")
    print(f"Business Type: {company.business_type}")
    print(f"Headquarter Address: {company.hq_address}")
    print("Employees:")
    for employee in company.employees:
        print(f"{employee.name}, {employee.address}, {employee.cell_number}")


if __name__ == "__main__":
    main()

       
