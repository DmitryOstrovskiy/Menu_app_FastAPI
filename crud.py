from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from .models import Menu, Submenu, Dish
from .schemas import MenuIn, SubmenuIn, DishIn


def get_menu(db: Session, menu_id: str):
    return db.query(Menu).filter(Menu.id == menu_id).first()


def get_menus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Menu).offset(skip).limit(limit).all()


def create_menu(db: Session, menu: MenuIn):
    menu_data = jsonable_encoder(menu)
    db_menu = Menu(**menu_data)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def delete_menu(db: Session, menu_id: str):
    db.query(Menu).filter(Menu.id == menu_id).delete()
    db.commit()


def get_submenu(db: Session, submenu_id: str):
    return db.query(Submenu).filter(Submenu.id == submenu_id).first()


def get_submenus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Submenu).offset(skip).limit(limit).all()


def create_submenu(db: Session, menu_id: str, submenu: SubmenuIn):
    submenu_data = jsonable_encoder(submenu)
    db_submenu = Submenu(**submenu_data, menu_id=menu_id)
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def delete_submenu(db: Session, submenu_id: str):
    db.query(Submenu).filter(Submenu.id == submenu_id).delete()
    db.commit()


def get_dish(db: Session, dish_id: str):
    return db.query(Dish).filter(Dish.id == dish_id).first()


def get_dishes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Dish).offset(skip).limit(limit).all()


def create_dish(db: Session, submenu_id: str, dish: DishIn):
    dish_data = jsonable_encoder(dish)
    db_dish = Dish(**dish_data, submenu_id=submenu_id)
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish


def delete_dish(db: Session, dish_id: str):
    db.query(Dish).filter(Dish.id == dish_id).delete()
    db.commit()
