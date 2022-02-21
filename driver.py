#!/usr/bin/env python3

# Built-In imports
import os

# Custom imports
from Menu import Menu
from Entry import Entry
from Prettify import Prettify

def main():
    main_entries = [
        Entry("Show Health", show_hp, 5, 74, 18),
        Entry("Show Monster", show_monster, "Skeleton"),
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
    
    # Add features
    
    # Add quit button
    main_menu.verbose_errors(True)
    
    # Sets entry to open submenu
    main_menu.give_entry("Show Attack Options").opens_menu(attack_menu)
    attack_menu.give_entry("Show Inventory").opens_menu(inventory_menu)
    
    # Makes a sub menu
    attack_menu.make_me_submenu(main_menu)
    inventory_menu.make_me_submenu(attack_menu)



    # Start Menu
    main_menu.start()
    
def show_hp(hp, strength, agility):
    print("HP:", hp)
    print("Strength:", strength)
    print("Agility:", agility)
    
def show_monster(monster):
    print("Monster:", monster)

if (__name__ == "__main__"):
    # If this file is invoked from the terminal, call main.
    main()