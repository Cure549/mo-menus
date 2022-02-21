#!/usr/bin/env python3

# Built-In imports
import os

# Custom imports
from mo_menus.Menu import Menu
from mo_menus.Entry import Entry
from mo_menus.Prettify import Prettify

def main():

    monsters = [
        "Demon",
        "Dog",
        "Rabbit"
    ]

    main_entries = [
        Entry("Show Health", show_hp, 5, 74, 18),
        Entry("Show Monster", show_monsters, monsters),
        Entry("Show Attack Options")
    ]
    
    attack_entries = [
        Entry("Attack"),
        Entry("Use Potion"),
        Entry("Show Inventory")
    ]
    
    inventory_entries = [
        Entry("Search"),
        Entry("Delete Item"),
        Entry("Take Item")
    ]
    
    inventory = [
        "Club",
        "Mace",
        "Potion"
    ]
    
    # Create menus
    main_menu = Menu("Main Menu", main_entries)
    attack_menu = Menu("Attack Menu", attack_entries)
    inventory_menu = Menu("Inventory Menu", inventory_entries)
    
    # ----------Add features----------------
    
    # Add error verbosity
    main_menu.verbose_errors(True)

    # Add Color using Prettify
    main_menu.prev_color(Prettify.RED)
    main_menu.title_color(Prettify.GREEN)
    main_menu.option_color(Prettify.YELLOW)

    attack_menu.prev_color(Prettify.RED)
    attack_menu.title_color(Prettify.GREEN)
    attack_menu.option_color(Prettify.YELLOW)
    
    # Sets entry to open submenu
    main_menu.give_entry("Show Attack Options").opens_menu(attack_menu)
    attack_menu.give_entry("Show Inventory").opens_menu(inventory_menu)
    
    # Makes a sub menu
    attack_menu.make_me_submenu(main_menu)
    inventory_menu.make_me_submenu(attack_menu)



    # Start Menu
    main_menu.start()
    
def show_hp(hp=0, strength=0, agility=0):
    print("HP:", hp)
    print("Strength:", strength)
    print("Agility:", agility)
    
def show_monsters(monsters):
    for mnstr in monsters:
        print(mnstr)

if (__name__ == "__main__"):
    # If this file is invoked from the terminal, call main.
    main()