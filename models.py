from sqlalchemy import (Table,
                        Column,
                        ForeignKey,
                        String,Integer)
from sqlalchemy.orm import relationship

from  sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

assoc_tabl=Table('assoc_tabl',Base.metadata,
                         Column('catalogs',Integer, ForeignKey('catalog.id')),
                         Column('products',Integer, ForeignKey('products.id')),)

class Catalog(Base):
    __tablename__='catalog'
    id=Column(Integer, primary_key=True,autoincrement=True)
    name =Column(String,unique=True)
    catalog_code=Column(String)


    def __init__(self, name: str, catalog_code: str):
          self.catalog_code = catalog_code
          self.name = name

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    plu = Column(String)
    price = Column(Integer)
    catalog=relationship('Catalog',secondary=assoc_tabl,backref='assoc_tabl')
    product = relationship('Products', secondary=assoc_tabl, backref='assoc_tabl')

    def __init__(self,name: str,plu:str,price:int,catalog):

        self.name=name
        self.price=price
        self.plu=plu
        self.catalog=catalog


