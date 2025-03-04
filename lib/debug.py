#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie , Base

# Create an SQLite database engine and initialize the database
engine = create_engine('sqlite:///freebies.db')

Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


if __name__ == '__main__':
    import ipdb; ipdb.set_trace()

   
    company1= Company(name = "Scinov", founding_year = 2015) 
    company2= Company(name = "Taisa", founding_year = 2021) 

    dev1= Dev(name= "Faith")
    dev2= Dev(name= "Nyolei")

    session.add_all([company1, company2, dev1, dev2])
    session.commit()

    # Assign freebies to developers from specific companies
    company1.give_freebie(dev1, "Laptop", 1)
    company1.give_freebie(dev2, "smartphone", 2)

    company2.give_freebie(dev1, "notebook", 3)
    company2.give_freebie(dev2, "Headphones", 4)

    freebies = session.query(Freebie).all()
    for freebie in freebies:
        print(freebie.print_details())

    print(dev1.received_one("Laptop"))
    print(dev1.received_one("smart watch"))

