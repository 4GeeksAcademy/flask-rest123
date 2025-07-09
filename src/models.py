from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(120),  nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(5), nullable=False)
    gender: Mapped[str] = mapped_column(String(10), nullable=False)
    height: Mapped[float] = mapped_column(Float, nullable=False)


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    climate: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    diameter: Mapped[float] = mapped_column(Float, nullable=False)
    gravity: Mapped[float] = mapped_column(Float, nullable=False)


class FavoritePlanet(db.Model):
    id_user: Mapped[int] = mapped_column(
        ForeignKey("user.id"), primary_key=True)
    id_planet: Mapped[int] = mapped_column(
        ForeignKey("planet.id"), primary_key=True)


class FavoritePeople(db.Model):
    id_user: Mapped[int] = mapped_column(
        ForeignKey("user.id"), primary_key=True)
    id_people: Mapped[int] = mapped_column(
        ForeignKey("people.id"), primary_key=True)
