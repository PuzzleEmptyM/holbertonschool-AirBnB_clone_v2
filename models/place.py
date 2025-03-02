#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table

place_amenity = Table(
    "place_amenity", Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.state_id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False,
                             back_populates="place_amenities",
                             overlaps="place_amenity"
                             )
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked Reviews, using FileStorage """
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """returns list of Amenity instances upon place_id"""
            amenities_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, value):
            """setter for amenity_ids list - class attribute"""
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
