from classes import *


def servise_country():
    services = input("""
    ----------------------------- -------------------
    👉 Counter Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in CountriTable.select("country"):
            print(i)
        return servise_country()
    elif services == '2':
        name = input("Name : ")
        create_date = input("Date : ")
        country = CountriTable(name, create_date)
        print(country.insert("country"))
        return servise_country()
    elif services == '3':
        column = input("Column Name : ")
        date = (input("Row : "))
        if column != "countr_id":
            print(CountriTable.delete(column, date, "country"))

        else:
            print(CountriTable.delete_id(column, date, "country"))
        return servise_country()
    elif services == "4":
        country = input("New Country : ")
        id = int(input("Country id : "))
        query = f"""
        UPDATE country SET name = '{country}' WHERE country_id = {id}
                                    """
        print(CountriTable.update(query))
        return servise_country()
    elif services == "5":
        return main()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_country()


def servise_city():
    services = input("""
    ------------------------------------------------
    👉 City Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in City.select("city"):
            print(i)
        return servise_city()

    elif services == "2":
        name = input("Name : ")
        country_id = int(input("Country id : "))
        create_date = input("Date : ")
        country = City(name, country_id, create_date)
        print(country.insert("city"))
        return servise_city()

    elif services == "3":
        column = input("Column Name : ")
        date = input("Row : ")
        if column != "city_id":
            print(City.delete(column, date, "city"))

        else:
            print(City.delete_id(column, date, "city"))
        return servise_city()
    elif services == "4":
        country = input("New City : ")
        id = int(input("City id : "))
        query = f"""
                UPDATE city SET name = '{country}' WHERE city_id = {id}
                                            """
        print(City.update(query))
        return servise_city()
    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_city()


def servise_address():
    services = input("""
    ------------------------------------------------
    👉 Address Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------

    Enter :   """)
    if services == '1':
        for i in Address.select("address"):
            print(i)
        return servise_address()

    elif services == '2':
        name = input("Name : ")
        city_id = int(input("City id : "))
        create_date = input("Date : ")
        address = Address(name, city_id, create_date)
        print(address.insert("address"))
        return servise_address()
    elif services == "3":
        column = input("Column Name : ")
        date = input("Row : ")
        if column != "address_id":
            print(Address.delete(column, date, "address"))

        else:
            print(Address.delete_id(column, date, "address"))
        return servise_address()
    elif services == "4":
        country = input("Name  : ")
        id = int(input("address id : "))
        query = f"""
                UPDATE address SET name = '{country}' WHERE address_id = {id}
                                            """
        print(Address.update(query))
        return servise_address()
    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_address()


def servise_customer():
    services = input("""
     ------------------------------------------------
    👉 Customer Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter : """)
    if services == '1':
        for i in Customer.select("customer"):
            print(i)
        return servise_customer()

    elif services == '2':
        first = input("First Name : ")
        last = (input("Last Name : "))
        phone = input("Phone Nomber : ")
        password = input("Password : ")
        birth_date = input("Birthday : ")
        adres = int(input("Adress_id : "))
        create_date = input("Date : ")
        address = Customer(first, last, phone, password, birth_date, adres, create_date)
        print(address.insert("customer"))
        return servise_customer()

    elif services == "3":
        column = input("Column Name : ")
        date = input("Row : ")
        if column != "countr_id":
            print(Customer.delete(column, date, "customer"))

        else:
            print(Customer.delete_id(column, date, "customer"))
        return servise_customer()

    elif services == "4":
        country = input("First Name  : ")
        id = int(input("Customer id : "))
        query = f"""
                UPDATE customer SET first_name = '{country}' WHERE customer_id = {id}
                                            """
        print(Customer.update(query))
        return servise_customer()

    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_customer()


def servise_product():
    services = input("""
    ------------------------------------------------
    👉 Product Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------

    Enter :""")
    if services == '1':
        for i in Product.select("product"):
            print(i)
        return servise_product()

    elif services == '2':
        title = input("Title : ")
        dick = (input("Description : "))
        reyting = float(input("Reyting : "))
        create_date = (input("Crete Date : "))
        address = Product(title, dick, reyting, create_date)
        print(address.insert("product"))
        return servise_product()

    elif services == "3":
        column = input("Column Name : ")
        date = input("Row : ")
        if column != "product_id":
            print(Product.delete(column, date, "product"))

        else:
            print(Product.delete_id(column, date, "product"))
        return servise_product()

    elif services == "4":
        country = input("Title  : ")
        id = int(input("Product Id   : "))
        query = f"""
                UPDATE product SET title = '{country}' WHERE product_id = {id}
                                            """
        print(Product.update(query))
        return servise_product()

    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_product()


def servise_product_type():
    services = input("""
    ------------------------------------------------
    👉 Product type Table 
        1. Select
        2. Insert
        3. Delete
        4. Update
        5. Back
    ------------------------------------------------
    Enter :  """)
    if services == '1':
        for i in ProductType.select("product_type"):
            print(i)
        return servise_product_type()
    elif services == '2':
        name = input("Name : ")
        color = input("Color : ")
        price = input("Price : ")
        product = int(input("Product Id :"))
        create_date = input("Create Date : ")
        product_tp = ProductType(name, color, price, product, create_date)
        print(product_tp.insert("product_type"))
        return servise_product_type()
    elif services == "3":
        column = input("Name : ")
        date = input("Row : ")
        if column != "product_type_id":
            print(ProductType.delete(column, date, "product_type"))

        else:
            print(ProductType.delete_id(column, date, "product_type"))
        return servise_product_type()

    elif services == "4":
        country = input("Name : ")
        id = int(input("Product Type Id  : "))
        query = f"""
                       UPDATE product_type SET name = '{country}' WHERE product_type_id = {id}
                                                   """
        print(ProductType.update(query))
        return servise_product_type()
    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_product_type()


def servise_category():
    services = input("""
        ------------------------------------------------
        👉 Category Table 
            1. Select
            2. Insert
            3. Delete
            4. Update
            5. Back
        ------------------------------------------------

        Enter :  """)
    if services == '1':
        for i in Category.select("category"):
            print(i)
        return servise_category()

    elif services == '2':
        title = input("Title : ")
        description = input("Description : ")
        create = input("Create date : ")
        category = Category(title, description, create)
        print(category.insert("category"))
        return servise_category()

    elif services == "3":
        column = input("Colume Name : ")
        date = input("Row : ")
        if column != "category_id":
            print(Category.delete(column, date, "category"))

        else:
            print(Category.delete_id(column, date, "category"))
        return servise_category()

    elif services == "4":
        country = input("title : ")
        id = int(input("category Id  : "))
        query = f"""
                           UPDATE category SET title = '{country}' WHERE category_id = {id}
                                                       """
        print(Category.update(query))
        return servise_category()

    elif services == "5":
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_category()


def servise_product_category():
    services = input("""
           ------------------------------------------------
           👉 Product Category Table 
               1. Select
               2. Insert
               3. Delete
               4. Update
               5. Back
           ------------------------------------------------

           Enter :  """)
    if services == '1':
        for i in ProductCategory.select("product_category"):
            print(i)
        return servise_product_category()

    elif services == '2':
        product_id = int(input("Product Id : "))
        category = int(input("Category Id : "))
        created = input("Created date : ")
        pc = ProductCategory(product_id, category, created)
        print(pc.insert("product_category"))
        return servise_product_category()

    elif services == '3':
        column = input("Name : ")
        date = input("Row : ")
        if column != "category_id":
            print(ProductCategory.delete(column, date, "product_category"))

        else:
            print(ProductCategory.delete_id(column, date, "product_category"))
        return servise_product_category()

    elif services == "4":
        country = input("Name : ")
        id = int(input("category Id  : "))
        query = f"""
                           UPDATE product_category SET product_id  = '{country}' WHERE product_category_id = {id}
                                                       """
        print(ProductCategory.update(query))
        return servise_product_category()
    elif services == '5':
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_product_category()


def servise_product_customer():
    services = input("""
               ------------------------------------------------
               👉 Product Customer Table 
                   1. Select
                   2. Insert
                   3. Delete
                   4. Update
                   5. Back
               ------------------------------------------------

               Enter :  """)
    if services == '1':
        for i in ProductCustomer.select("product_customer"):
            print(i)
        return servise_product_customer()

    elif services == '2':
        product_id = int(input("Product Id : "))
        category = int(input("Customer Id : "))
        pc = ProductCustomer(product_id, category)
        print(pc.insert("product_customer"))
        return servise_product_customer()

    elif services == '3':
        column = input("Name : ")
        date = input("Row : ")
        if column != "category_id":
            print(ProductCustomer.delete(column, date, "product_customer"))

        else:
            print(ProductCustomer.delete_id(column, date, "product_customer"))
        return servise_product_customer()

    elif services == "4":
        country = int(input("New product id : "))
        id = int(input("category Id  : "))
        query = f"""
                               UPDATE product_customer SET product_id  = {country} WHERE product_customer_id = {id}
                                                           """
        print(ProductCustomer.update(query))
        return servise_product_customer()
    elif services == '5':
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_product_customer()


def servise_store():
    services = input("""
               ------------------------------------------------
               👉 Store Table 
                   1. Select
                   2. Insert
                   3. Delete
                   4. Update
                   5. Back
               ------------------------------------------------

               Enter :  """)
    if services == '1':
        for i in Store.select("store"):
            print(i)
        return servise_store()

    elif services == '2':
        name = input("Name : ")
        description = input("Description : ")
        address = int(input("Address Id : "))
        pc = Store(name, description, address)
        print(pc.insert("store"))
        return servise_store()

    elif services == '3':
        column = input("Name : ")
        date = input("Row : ")
        if column != "store_id":
            print(Store.delete(column, date, "store"))

        else:
            print(Store.delete_id(column, date, "store"))
        return servise_store()

    elif services == "4":
        country = input("Name : ")
        id = int(input("store Id  : "))
        query = f"""
                               UPDATE store SET name  = '{country}' WHERE store_id = {id}
                                                           """
        print(Store.update(query))
        return servise_store()
    elif services == '5':
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_store()


def servise_punk():
    services = input("""
               ------------------------------------------------
               👉 Punk Table 
                   1. Select
                   2. Insert
                   3. Delete
                   4. Update
                   5. Back
               ------------------------------------------------

               Enter :  """)
    if services == '1':
        for i in Punk.select("punk"):
            print(i)
        return servise_punk()()

    elif services == '2':
        name = input("Name : ")
        address = int(input("Address Id : "))
        pc = Punk(name, address)
        print(pc.insert("punk"))
        return servise_punk()

    elif services == '3':
        column = input("Name : ")
        date = input("Row : ")
        if column != "punk_id":
            print(Punk.delete(column, date, "punk"))

        else:
            print(Punk.delete_id(column, date, "punk"))
        return servise_punk()

    elif services == "4":
        country = input("Name New : ")
        id = int(input("punk Id  : "))
        query = f"""
                               UPDATE punk SET name  = '{country}' WHERE punk_id = {id}
                                                           """
        print(Punk.update(query))
        return servise_punk()
    elif services == '5':
        return main()

    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday service mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return servise_punk()


def main():
    tables = input("""
    ______________________________________________________
        1. Country
        2. City
        3. Address
        4. Customer
        5. Product
        6. ProductType
        7. Category
        8. Product Category
        9. Product Customer
        10. Store
        11. Punk
    ______________________________________________________
        👉👉👉  """)
    if tables == '1':
        return servise_country()

    elif tables == '2':
        return servise_city()
    elif tables == '3':
        return servise_address()
    elif tables == '4':
        return servise_customer()
    elif tables == '5':
        return servise_product()
    elif tables == '6':
        return servise_product_type()
    elif tables == '7':
        return servise_category()
    elif tables == '8':
        return servise_product_category()
    elif tables == '9':
        return servise_product_customer()
    elif tables == '10':
        return servise_store()
    elif tables == '11':
        return servise_punk()
    else:
        print("❌❌❌❌❌❌❌❌❌❌")
        print("____ EROOR ____")
        print("Bunday Table mavjud emas !!!")
        print("❌❌❌❌❌❌❌❌❌❌")
        return main()


if __name__ == '__main__':
    main()
