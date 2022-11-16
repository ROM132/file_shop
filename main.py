import csv


class Shop_file:
    with open("Test.csv", "r") as f:
        reader = f.read()

    def __init__(self):
        self.buy = None
        self.reader_update = None

    def RulePick(self):
        qus = input("Enter (a) to login as Admin or (u) to login as user: ")
        if qus == "a":
            s.Admin()
        elif qus == "u":
            pass
        else:
            print("Invalid input try again!")
            s.RulePick()

    def Admin(self):
        s.Delete_blank_line()
        with open("Test.csv", "r") as f1:
            self.reader_update = f1.read()

        s.print_admin_option()
        qus = input("Enter your choice: ")
        if qus == "1":
            print(f"\n{self.reader_update}"), input("Press enter to go back: ")
            s.Admin()

        elif qus == "2":
            s.Add_Product()

        elif qus == "3":
            s.Delete_product()
        elif qus == "4":
            s.change_product_name()
        elif qus == "5":
            s.change_product_price()
        elif qus == "6":
            with open("Text2.csv", "r") as r1:
                reader = r1.read()

            with open("Test.csv", "w") as r2:
                print("Everything reset!"), input("Press enter to go back: ")
                r2.write(reader)
            s.Admin()
        elif qus == "7":
            print("Ok good bey")
            exit()
        else:
            print("Invalid input try again!")
            s.Admin()

    def Add_Product(self):
        name = input("Enter the name of the product: ")
        reader = self.reader_update.split()
        if name in reader:
            print("There is a product with this name already try another name")
            s.Add_Product()
        while True:
            price = input("Enter the price of the product: ")
            if price.isdigit():
                price = int(price)
                break
            else:
                print("Enter a number next time!")
                continue

        with open("Test.csv", "a") as a:
            a.write(f"\n{name}, {price}")
            print("The product add successfully!!")
        s.Admin()

    def Delete_product(self):
        lines = list()
        name = input("Enter the name of the product: ")
        control_when_to_exit_the_loop = 0
        with open("Test.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if name in row:
                    control_when_to_exit_the_loop += 1
                    pass
            if control_when_to_exit_the_loop == 0:
                print(f"The Product ({name}) do not found!")
                s.Admin()

        with open("Test.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == name:
                        lines.remove(row)
                        print("The Product remove successfully!")

            with open('Test.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
            s.Admin()

    def change_product_name(self):
        lines = list()
        name_of_the_product = input("Enter the name of the product: ")
        num_to_check = 0
        with open("Test.csv", "r+") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if name_of_the_product == row[0]:
                    num_to_check += 1
                    new_name = input("Enter the new name: ")
                    row[0] = new_name
                lines += f"{','.join(row)}\n"
            string = ''.join(lines)

            if num_to_check == 0:
                print(f"The product ({name_of_the_product}) Do not found try again!")
                s.Admin()

            with open("Test.csv", "w")as w:
                w.write(string)
                input("The product name change successfully!\nPress enter to go back: ")
            s.Admin()

    def change_product_price(self):
        lines = list()
        name_of_the_product = input("Enter the name of the product: ")
        num_to_check = 0
        with open("Test.csv", "r+") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if name_of_the_product == row[0]:
                    num_to_check += 1
                    new_price = input("Enter the new Price: ")
                    row[1] = new_price
                lines += f"{','.join(row)}\n"
            string = ''.join(lines)

            if num_to_check == 0:
                print(f"The product ({name_of_the_product}) Do not found try again!")
                s.Admin()

            with open("Test.csv", "w") as w:
                w.write(string)
                input("The product price change successfully!\nPress enter to go back: ")
            s.Admin()

    def print_admin_option(self):
        print("\n1. Display Product\n"
              "2. Add Product\n"
              "3. Delete Product\n"
              "4. Change Product Name\n"
              "5. Change Product Price\n"
              "6. Restart All\n"
              "7. Exit")

    def Delete_blank_line(self):
        output = ""
        with open("Test.csv") as t:
            for line in t:
                if not line.isspace():
                    output += line
        t = open("Test.csv", "w")
        t.write(output)


s = Shop_file()
s.Admin()
