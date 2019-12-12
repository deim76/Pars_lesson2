from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  models import Base,Catalog,Products


from sqldatabase.parser import Parser



class ProductsDB:
    def __init__(self,base,db_url):
        engine= create_engine(db_url)
        base.metadata.create_all(engine)
        session_db=sessionmaker(bind=engine)
        self.__session=session_db()

    @property
    def session(self):
        return self.__session

if __name__=='__main__':
    bd_url='sqlite:///catalogs.sqlite'
    db=ProductsDB(Base,bd_url)
    parser=Parser()
    list_cat=[]
    for i in parser.catalogs[0]:
         cat=Catalog(i['parent_group_name'], i['parent_group_code'])
         list_cat.append(cat)
         db.session.add(cat)
    for i in parser.products:
           list=[]
           list.append(list_cat[i['Catalog_code']])
           db.session.add(Products(i['name'], i['plu'], i['Price'], list))

    db.session.commit()












