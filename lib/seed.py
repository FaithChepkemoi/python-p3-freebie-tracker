#!/usr/bin/env python3

#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


 # Create instances of the Company model with name and founding year
company1= Company(name = "Scinov", founding_year = 2015) 
company2= Company(name = "Taisa", founding_year = 2021) 

dev1= Dev(name= "Faith")
dev2= Dev(name= "Nyolei")

session.add_all([company1, company2, dev1, dev2])
session.commit()

# Assign freebies to developers from specific companies
company1.give_freebie(session, dev1, "Laptop", 1)
company1.give_freebie(session, dev2, "smartphone", 2)
company2.give_freebie(session, dev1, "notebook", 3)

# Commit the freebies to the database
session.commit()

#print success message
print("Database has been successful.")