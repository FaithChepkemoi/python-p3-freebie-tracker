
from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', back_populates='company', overlaps= 'devs')
    devs = relationship('Dev', secondary='freebies', back_populates ='companies', overlaps ='freebies')

    def __repr__(self):
        return f'<Company {self.name}>'

    def give_freebie(self, session, dev, item_name, value):
        freebie = Freebie(item_name=item_name, value=value, dev_id=dev.id, company_id=self.id)
        session.add (freebie)
        session.commit()


    @classmethod
    def oldest_company(cls):
        return session.query(cls).order_by(cls.founding_year).first()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    freebies = relationship('Freebie', back_populates='dev', overlaps= "companies")
    companies = relationship('Company', secondary='freebies', back_populates='devs', overlaps ="freebies")

    def __repr__(self):
        return f'<Dev {self.name}>'

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie, session):
        if freebie.dev == self:
            freebie.dev = dev
            session.commit()
        else: 
            raise ValueError("You cannot give away freebies that doesn't belong to you.")

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

    dev = relationship ('Dev',  back_populates= 'freebies')
    company = relationship ('Company',  back_populates= 'freebies')

    def __repr__(self):
        return f'<Freebie {self.item_name}, {self.value}>'

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"