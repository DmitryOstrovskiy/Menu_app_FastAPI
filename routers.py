from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .crud import get_menu, get_menus, create_menu, delete_menu, get_submenu, get_submenus, create_submenu, delete_submenu, get_dishes, create_dish
from .schemas import MenuIn, MenuOut, SubmenuIn, SubmenuOut, DishIn, DishOut
from .database import get_db

router = APIRouter()


@router.get("/menus/{menu_id}", response_model=MenuOut)
def read_menu(menu_id: str, db: Session = Depends(get_db)):
    db_menu = get_menu(db, menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    return db_menu


@router.get("/menus/", response_model=List[MenuOut])
def read_menus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    menus = get_menus(db, skip=skip, limit=limit)
    return menus


@router.post("/menus/", response_model=MenuOut)
def create_new_menu(menu: MenuIn, db: Session = Depends(get_db)):
    return create_menu(db=db, menu=menu)


@router.delete("/menus/{menu_id}")
def remove_menu(menu_id: str, db: Session = Depends(get_db)):
    db_menu = get_menu(db, menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    delete_menu(db, menu_id)
    return {"detail": "Menu deleted"}


@router.get("/menus/{menu_id}/submenus{submenu_id}", response_model=SubmenuOut)
def read_submenu(submenu_id: str, db: Session = Depends(get_db)):
    db_submenu = get_submenu(db, submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="Submenu not found")
    return db_submenu


@router.get("/menus/{menu_id}/submenus/", response_model=List[SubmenuOut])
def read_submenus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    submenus = get_submenus(db, skip=skip, limit=limit)
    return submenus


@router.post("/menus/{menu_id}/submenus/", response_model=SubmenuOut)
def create_new_sumenu(submenu: SubmenuIn, db: Session = Depends(get_db)):
    return create_submenu(db=db, submenu=submenu)


@router.delete("/menus/{menu_id}/submenus{submenu_id}")
def remove_submenu(submenu_id: str, db: Session = Depends(get_db)):
    db_submenu = get_submenu(db, submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="Submenu not found")
    delete_submenu(db, submenu_id)
    return {"detail": "Submenu deleted"}


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}", response_model=DishOut)
def read_dish(dish_id: str, db: Session = Depends(get_db)):
    db_dish = get_submenu(db, dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="Dish not found")
    return db_dish


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes/", response_model=List[DishOut])
def read_dishes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dishes = get_dishes(db, skip=skip, limit=limit)
    return dishes


@router.post("/menus/{menu_id}/submenus/{submenu_id}/dishes/", response_model=DishOut)
def create_new_dish(dish: DishIn, db: Session = Depends(get_db)):
    return create_dish(db=db, dish=dish)


@router.delete("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
def remove_dish(dish_id: str, db: Session = Depends(get_db)):
    db_dish = get_menu(db, dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="Dish not found")
    delete_menu(db, dish_id)
    return {"detail": "Dish deleted"}
