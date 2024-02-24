from data import Database


def created_table():
    country_table = f"""
        CREATE TABLE country(
            country_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            last_update TIMESTAMP DEFAULT now(),
            create_date DATE);"""

    city_table = f"""
            CREATE TABLE city(
                city_id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                country_id INT REFERENCES country(country_id),
                last_update TIMESTAMP DEFAULT now(),
                create_date DATE);"""

    address = f"""
                CREATE TABLE address(
                    address_id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    city_id INT REFERENCES city(city_id),
                    last_update TIMESTAMP DEFAULT now(),
                    create_date DATE);"""

    customer = f"""
                    CREATE TABLE customer(
                        customer_id SERIAL PRIMARY KEY,
                        first_name VARCHAR(50) NOT NULL,
                        last_name VARCHAR(50),
                        phone_number VARCHAR(10) NOT NULL,
                        password VARCHAR(10) NOT NULL,
                        birth_date DATE NOT NULL,
                        address_id INT REFERENCES address(address_id),
                        last_update TIMESTAMP DEFAULT now(),
                        create_date DATE);"""

    product = f"""
            CREATE TABLE product(
                product_id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                description TEXT,
                reyting FLOAT,
                last_update TIMESTAMP DEFAULT now(),
                create_date DATE);"""

    product_type = f"""
            CREATE TABLE product_type(
                product_type_id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                color VARCHAR(20),
                price FLOAT NOT NULL,
                product_id INT REFERENCES product(product_id),
                last_update TIMESTAMP DEFAULT now(),
                create_date DATE);"""

    category = f"""
            CREATE TABLE category(
                category_id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                description TEXT,
                last_update TIMESTAMP DEFAULT now(),
                create_date DATE);"""

    product_category = f"""
            CREATE TABLE product_category(
                product_category_id SERIAL PRIMARY KEY,
                product_id INT REFERENCES product(product_id),
                category_id INT REFERENCES category(category_id),
                last_update TIMESTAMP DEFAULT now(),
                create_date DATE);"""



    product_customer = f"""
                        CREATE TABLE product_customer(
                            product_customer_id SERIAL PRIMARY KEY,
                            product_id INT REFERENCES product(product_id),
                            customer_id INT REFERENCES customer(customer_id),
                            last_update TIMESTAMP DEFAULT now());"""

    store = f"""
                        CREATE TABLE store(
                            store_id SERIAL PRIMARY KEY,
                            name VARCHAR(20),
                            description TEXT,
                            address_id INT REFERENCES address(address_id),
                            last_update TIMESTAMP DEFAULT now());"""

    punk = f"""
                            CREATE TABLE punk(
                                punk_id SERIAL PRIMARY KEY,
                                name VARCHAR(20),
                                address_id INT REFERENCES address(address_id),
                                last_update TIMESTAMP DEFAULT now());"""

    data_table = {
        "country_table": country_table,
        "city_table": city_table,
        "address": address,
        "customer": customer,
        "product": product,
        "product_type": product_type,
        "category": category,
        "product_category": product_category,
        "product_customer": product_customer,
        "store": store,
        "punk": punk
    }

    for i in data_table:
        print(f"{i} {Database.connect(data_table[i], "create")}")


# if __name__ == "__main__":
#     created_table()
