from data import Database


class Base:

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    @staticmethod
    def delete(column, data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}' """
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {data} """
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class CountriTable:
    def __init__(self, name: str, create_date: str):
        self.name = name
        self.create_date = create_date

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table):
        query = f"""INSERT INTO {table}(name, create_date) VALUES ('{self.name}','{self.create_date}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}' """
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {data} """
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class City(Base):
    def __init__(self, name: str, country_id, create_date: str):
        self.name = name
        self.country_id = country_id
        self.create_date = create_date

    def insert(self, table):
        query = f"""INSERT INTO {table}(name, country_id,create_date) VALUES ('{self.name}',{self.country_id},'{self.create_date}')"""
        return Database.connect(query, "insert")


class Address(CountriTable):
    def __init__(self, name: str, city_id: int, create_date: str):
        super().__init__(name, create_date)
        self.city_id = city_id

    def insert(self, table):
        query = f""" INSERT INTO {table}(name, city_id,create_date) VALUES ('{self.name}',{self.city_id},'{self.create_date}')"""
        return Database.connect(query, "insert")


class Customer(Base):
    def __init__(self, first_name: str, last_name: str, phone_number: str, password, birth_date: str, address_id: int,
                 create_date):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.password = password
        self.birth_date = birth_date
        self.address_id = address_id
        self.create_date = create_date

    def insert(self, table):
        query = f"""INSERT INTO {table}(first_name,last_name,phone_number,password,birth_date,address_id,
        create_date) VALUES ('{self.first_name}','{self.last_name}','{self.phone_number}',
        '{self.password}','{self.birth_date}',{self.address_id},'{self.create_date}')"""
        return Database.connect(query, "insert")


class Product(Base):
    def __init__(self, title, description, reyting, create_date):
        self.title = title
        self.description = description
        self.reyting = reyting
        self.create_date = create_date

    def insert(self, table):
        query = f"""INSERT INTO {table}(title, description,reyting,create_date) VALUES ('{self.title}','{self.description}',
        '{self.reyting}','{self.create_date}')"""
        return Database.connect(query, "insert")


class ProductType(Base):
    def __init__(self, name, color, price, product_id, create_date):
        self.name = name
        self.color = color
        self.price = price
        self.product_id = product_id
        self.create_date = create_date

    def insert(self, table):
        query = f"""INSERT INTO {table}(name, color,price, product_id, create_date) VALUES ('{self.name}','{self.color}',
        {self.price}, {self.product_id},'{self.create_date}')"""
        return Database.connect(query, "insert")


class Category(Base):
    def __init__(self, title, description, create_date):
        self.title = title
        self.description = description
        self.create_date = create_date

    def insert(self, table):
        query = f"""INSERT INTO {table}(title, description, create_date) VALUES ('{self.title}','{self.description}','{self.create_date}')"""
        return Database.connect(query, "insert")


class ProductCategory(Base):
    def __init__(self, product_id: int, category_id: int, create_date):
        self.product_id = product_id
        self.category_id = category_id
        self.create_date = create_date

    def insert(self, table):
        query = f"""INSERT INTO {table}(product_id, category_id, create_date) VALUES 
        ({self.product_id},{self.category_id},'{self.create_date}')"""
        return Database.connect(query, "insert")


class ProductCustomer(Base):
    def __init__(self, product_id, customer_id):
        self.prduct_id = product_id
        self.costomer_id = customer_id

    def insert(self, table):
        query = f""" INSERT INTO {table}(product_id, customer_id) VALUES 
        ({self.prduct_id},{self.costomer_id})
        """

        return Database.connect(query, "insert")


class Store(Base):
    def __init__(self, name, description, address_id):
        self.name = name
        self.description = description
        self.address_id = address_id

    def insert(self, table):
        query = f""" INSERT INTO {table}(name,description,address_id) VALUES
        ('{self.name}','{self.description}',{self.address_id})
        """
        return Database.connect(query, "insert")


class Punk(Base):
    def __init__(self, name, address_id):
        self.name = name
        self.address_id = address_id

    def insert(self, table):
        query = f""" INSERT INTO {table}(name,address_id) VALUES 
        ('{self.name}',{self.address_id})
        """
        return Database.connect(query, "insert")

#
# if __name__ == "__main__":
# for i in Category.select("category"):
#     print(i)
# column = input("Column Name : ")
# date = input("Row : ")
# if column != "countr_id":
#     print(Customer.delete(column, date, "customer"))
# else:
#     print(Customer.delete(column, date, "customer"))
#     data = Address("AQSH", 5, "2012-3-23")
#     print(data.insert())
# c = Product_type("Samsung", "QOra", 1200, 4, "2023-1-12")
# print(c.insert("product_type"))
# c = Category("MMMmm", "jbiubi", "2021-01-11")
# print(c.insert(), "category")
# c = ProductCategory(7, 5, "2020-01-01")
# print(c.insert("product_category"))
