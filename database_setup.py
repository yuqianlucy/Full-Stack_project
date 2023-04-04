import sys
from sqlalchemy import Column,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base=declarative_base()


#creating class
class Restaurant(Base):

# creating table representation
    __tablename__='restaurant'
    #Creating columns
    name=Column(String(80),nullable=False)
    id=Column(Integer,primary_key=True)

class MenuItem(Base):
# creating table representation
    __tablename__='menu_item'
    #Creating columns
    name=Column(String(80),nullable=False)
    id=Column(Integer,primary_key=True)
    description = Column(String(250))
    course=Column(String(250))
    price=Column(String(8))
    restaurant_id=Column(Integer,ForeignKey('restaurant.id'))
    restaurant=relationship(Restaurant)

####### insert at end of file ####
engine=create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()
myFirstRestaurant=Restaurant(name="Pizza Palace")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()
cheesepizza=MenuItem(name="Cheese Pizza",course="Entree",price="$8.99",restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()
firstResult=session.query(Restaurant).first()
print(firstResult.name)
session.query(Restaurant).all
items=session.query(MenuItem).all()
for item in items:
    print (item.name)

veggieBurgers=session.query(MenuItem).filter_by(name='Veggie Burger')
for veggieBurger in veggieBurgers:
    print (veggieBurger.id)
    print (veggieBurger.price)
    print(veggieBurger.restaurant.name)
    print("\n")

UrbanVeggieBurger=session.query(MenuItem).filter_by(id=11).one()
print(UrbanVeggieBurger.price)
UrbanVeggieBurger.price='$2.99'
session.add(UrbanVeggieBurger)
print(UrbanVeggieBurger.price)
session.commit()
for veggieBurger in veggieBurgers:
    if veggieBurger.price !='$2.99':
        session.add(veggieBurger)
        session.commit()
for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name)
    print("\n")
spinach=session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
print(spinach.restaurant.name)
session.delete(spinach)
session.commit()