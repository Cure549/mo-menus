#!/usr/bin/env python3

# Custom imports
from mo_menus.Menu import Menu
from mo_menus.Entry import Entry
# Prettify is not necessary.
# Just a nice library to have to reduce ANSI color code clutter.
from mo_menus.Prettify import Prettify


def main():
    # Uncomment an example call to see result.
    # Each example is heavily documented.
    # example1()
    # example2()
    # example3()
    # example4()
    # example5()
    example6()


def example1():
    """
        This is the minimal code needed to create a working menu.
    """

    # Create list of entries
    main_entries = [
        Entry("Do Thing", print, "Passed in parameter")
    ]

    # Create's menu with list of entries
    main_menu = Menu("Main Menu", main_entries)

    # Starts Menu
    main_menu.start()


def example2():
    """
        This is how additional entries are added.
        To add additional parameters to a function call,
        simply add them as a parameter to Entry()
    """

    # Create list of entries
    main_entries = [
        Entry("Do Thing", print, "Passed in parameter"),
        Entry("Show Monster", print, "This was added...", "And now this!")
    ]

    # Create's menu with list of entries
    main_menu = Menu("Main Menu", main_entries)

    # Starts Menu
    main_menu.start()


def example3():
    """
        This covers how to create a sub-menu.
    """

    # Create list of entries
    main_entries = [
        Entry("Do Thing", print, "Passed in parameter"),
        # Takes no additional args. Menu() will figure out the rest.
        Entry("Show other menu")
    ]

    # Create another list of entries
    other_entries = [
        Entry("Print Hello", print, "Hello")
    ]

    # Create's menus with list of entries
    main_menu = Menu("Main Menu", main_entries)
    other_menu = Menu("Other Menu", other_entries)

    # Tell an entry to open a menu
    main_menu.give_entry("Show other menu").opens_menu(other_menu)

    # Tells a menu to become a sub-menu
    # Pass in the parent of the sub-menu
    other_menu.make_me_submenu(main_menu)

    # Starts Menu
    main_menu.start()


def example4():
    """
        Now let's cover how to make the entries have a more dynamic action.
        This will involve the use of using our own functions.
    """

    # Let's create some basic functions to print 'some' HP and Mana
    def my_hp(hp):
        print("My HP is:", hp)

    def my_mana(mana):
        print("My Mana is:", mana)

    # Create list of entries
    main_entries = [
        Entry("Basic Entry", print, "Passed in parameter"),
        # Takes no additional args. Menu() will figure out the rest.
        Entry("Show other menu")
    ]

    # Create another list of entries
    other_entries = [
        Entry("Show HP", my_hp, 10),
        Entry("Show Mana", my_mana, 5)
    ]

    # Create's menus with list of entries
    main_menu = Menu("Main Menu", main_entries)
    other_menu = Menu("Other Menu", other_entries)

    # Tell an entry to open a menu
    main_menu.give_entry("Show other menu").opens_menu(other_menu)

    # Tells a menu to become a sub-menu
    # Pass in the parent of the sub-menu
    other_menu.make_me_submenu(main_menu)

    # Starts Menu
    main_menu.start()


def example5():
    """
        Now that all the fundamentals have been covered, let's go over
        some customization options.
        Additional customization features will be added in the future.
    """

    # Let's create some basic functions to print 'some' HP and Mana
    def my_hp(hp):
        print("My HP is:", hp)

    def my_mana(mana):
        print("My Mana is:", mana)

    def print_monsters(monsters):
        for mnstr in monsters:
            print(mnstr)

    # Create list for print_monsters()
    monsters = [
        "Demon",
        "Skeleton",
        "Zombie",
        "Vampire"
    ]

    # Create list of entries
    main_entries = [
        Entry("Basic Entry", print, "Passed in parameter"),
        # Takes no additional args. Menu() will figure out the rest.
        Entry("Show other menu")
    ]

    # Create another list of entries
    other_entries = [
        Entry("Show HP", my_hp, 10),
        Entry("Show Mana", my_mana, 5),
        Entry("Show Monsters", print_monsters, monsters)
    ]

    # Create's menus with list of entries
    main_menu = Menu("Main Menu", main_entries)
    other_menu = Menu("Other Menu", other_entries)

    # Tell an entry to open a menu
    main_menu.give_entry("Show other menu").opens_menu(other_menu)

    # Tells a menu to become a sub-menu
    # Pass in the parent of the sub-menu
    other_menu.make_me_submenu(main_menu)

    # ----Personalization options----

    # Add input error verbosity
    main_menu.verbose_errors(True)
    other_menu.verbose_errors(True)

    # Color is set to your default .bashrc specified output color.

    # Adds color to the previous menu button
    main_menu.prev_color(Prettify.RED)

    # Adds color to the menu title
    main_menu.title_color(Prettify.GREEN)

    # Adds color to the option value
    main_menu.option_color(Prettify.YELLOW)

    # Adds color to the entry value
    main_menu.entry_color(Prettify.CYAN)

    # Adds color to other menu
    other_menu.prev_color(Prettify.BLUE)
    other_menu.title_color(Prettify.GREEN)
    other_menu.option_color(Prettify.YELLOW)

    # Starts Menu
    main_menu.start()


def example6():
    """
        To use the experimental box feature. Simply set the draw_mode to
        "experimental".
    """

    # Let's create some basic functions to print 'some' HP and Mana
    def my_hp(hp):
        print("My HP is:", hp)

    def my_mana(mana):
        print("My Mana is:", mana)

    def print_monsters(monsters):
        for mnstr in monsters:
            print(mnstr)

    # Create list for print_monsters()
    monsters = [
        "Demon",
        "Skeleton",
        "Zombie",
        "Vampire"
    ]

    # Create list of entries
    main_entries = [
        Entry("Basic Entry", print, "Passed in parameter"),
        # Takes no additional args. Menu() will figure out the rest.
        Entry("Show other menu")
    ]

    # Create another list of entries
    other_entries = [
        Entry("Show HP", my_hp, 10),
        Entry("Show Mana", my_mana, 5),
        Entry("Show Monsters", print_monsters, monsters)
    ]

    # Create's menus with list of entries
    main_menu = Menu("Main Menu", main_entries)
    other_menu = Menu("Other Menu", other_entries)

    # Tell an entry to open a menu
    main_menu.give_entry("Show other menu").opens_menu(other_menu)

    # Tells a menu to become a sub-menu
    # Pass in the parent of the sub-menu
    other_menu.make_me_submenu(main_menu)

    # ----Personalization options----

    # Add input error verbosity
    main_menu.verbose_errors(True)
    other_menu.verbose_errors(True)

    # Color is set to your default .bashrc specified output color.

    # Adds color to the previous menu button
    main_menu.prev_color(Prettify.RED)

    # Adds color to the menu title
    main_menu.title_color(Prettify.GREEN)

    # Adds color to the option value
    main_menu.option_color(Prettify.YELLOW)

    # Adds color to the entry value
    main_menu.entry_color(Prettify.CYAN)

    # Set the menu draw mode to the more modern, experimental mode.
    main_menu.draw_mode = "experimental"
    other_menu.draw_mode = "experimental"

    # Adds color to other menu
    other_menu.prev_color(Prettify.BLUE)
    other_menu.title_color(Prettify.GREEN)
    other_menu.option_color(Prettify.YELLOW)

    # Starts Menu
    main_menu.start()


if (__name__ == "__main__"):
    # If this file is invoked from the terminal, call main.
    main()
