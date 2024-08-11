from sqlalchemy import create_engine, Column, Integer, String, Text, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


# # Exam: 01. Model Recipe
class Recipe(Base):
    __tablename__ = 'recipies'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)

    # Exam: 08.	Extend the Recipe Model
    chef_id = Column(Integer, ForeignKey('chefs.id'))
    chef = relationship("Chef", back_populates="recipes")


# # 7.Model Chef
class Chef(Base):
    __tablename__ = 'chefs'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    recipes = relationship('Recipe', back_populates='chef')








