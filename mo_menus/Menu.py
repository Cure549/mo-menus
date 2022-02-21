#!/usr/bin/env python3

import os
from mo_menus.Entry import Entry
from mo_menus.Prettify import Prettify
from Boxxy.Boxxy import Boxxy


class Menu:
    def __init__(self, title, entries):
        # Handle params
        self._title = title
        self._entries = self._eval_entries(entries)

        # Supported options: "classic",
        #                    "experimental"
        self._draw_mode = "classic"

        # Sub menu pre-reqs
        self._is_submenu = False
        self._parent_menu = None

        # Currently not working.
        self._wipe_on_input = False

        # Design options
        self.__prefix = "\033["
        self.__default_color = f"{self.__prefix}0m"
        self.__end_color = self.__default_color
        self._prev_color = self.__default_color
        self._title_color = self.__default_color
        self._option_color = self.__default_color
        self._entry_color = self.__default_color

        # Stores user input
        self._enable_input = True
        self._user_input = None
        self._request_msg = "Please select an option: > "
        self._quit_keyword = "Quit"
        self._back_keyword = "Back"

        # Error handling
        self._error_msg = f"{Prettify.RED}ERROR:{Prettify.END} Invalid input"
        self._verbose_errors = False
        self._check_errors = (
            KeyboardInterrupt,
            EOFError,
            ValueError,
            UnboundLocalError,
        )

        # Adds default quit button.
        # Get's replaced with back button if menu is a sub-menu.
        quit_entry = Entry(self._quit_keyword)
        self._entries.update({0: quit_entry})

    @property
    def draw_mode(self):
        return self._draw_mode

    @draw_mode.setter
    def draw_mode(self, mode):
        self._draw_mode = mode

    def prev_color(self, *color):
        self._prev_color = ""

        for format in color:
            self._prev_color += format

    def title_color(self, *color):
        self._title_color = ""

        for format in color:
            self._title_color += format

    def option_color(self, *color):
        self._option_color = ""

        for format in color:
            self._option_color += format

    def entry_color(self, *color):
        self._entry_color = ""

        for format in color:
            self._entry_color += format

    def start(self):
        # Menu Loop
        while True:
            # Draw Menu and get validated input
            self.draw_menu()

            # Quits Menu
            # Should only ever be called by Top Level Menu
            # DO NOT add quit entry to a sub menu. Add a back entry instead.
            if (
                self._entries.get(self._user_input).description
                == self._quit_keyword
            ):
                break

            # Invoke what entry references
            entry = self._entries.get(self._user_input)
            if isinstance(entry.invoke, Menu):
                # Do submenu things
                entry.invoke.start()
                break
            else:
                if (entry.invoke_params is None):
                    entry.invoke()
                else:
                    entry.invoke(*entry.invoke_params())

    def verbose_errors(self, toggle):
        self._verbose_errors = toggle

    def wipe_prints(self):
        if self._wipe_on_input:
            # Get Count
            # +2 due to input and title line.
            line_count = len(self._entries.keys()) + 2
            # Place Cursor and clear menu
            print(f"\033[{line_count}F\033[J", end="")

    def get_validated_input(self):
        """Sets self._user_input to a validated key that can be
        used to access one of the existing entries.
        """
        try:
            self._user_input = int(input(self._request_msg))
            test_key = self._entries.get(self._user_input)
            # Forcefully set input and test_key. Run validation afterwards.
            if (test_key is None):
                raise ValueError("Entry does not exist.")

        except self._check_errors as e:
            print_error = ""

            if type(e) == EOFError:
                # Keeps consistency in feedback in terms of format.
                if self._verbose_errors:
                    print_error = f"{self._error_msg}, {e}"
                else:
                    print_error = f"{self._error_msg}"
                self.wipe_prints()
                print(print_error)
                self.draw_menu()
            else:
                if self._verbose_errors:
                    print_error = f"{self._error_msg} {e}"
                else:
                    print_error = f"{self._error_msg}"
                self.wipe_prints()
                print(print_error)
                self.draw_menu()

    def draw_menu(self):
        """Draws menu and correlated sub menus to stdout."""
        prev_button = ""

        if self._is_submenu:
            # local vars to make PEP-8 compliance possible
            title_desc = self._parent_menu._title
            prev_desc = (self._entries.get(0)).description
            prev_color = self._prev_color
            end_color = self.__end_color
            prev_to_title = f"{prev_desc} to {title_desc}"
            # Sets prev_button to be back
            prev_button = f"{prev_color}⮪ [0] {prev_to_title}{end_color}"
        else:
            # Sets prev_button to be quit
            prev_button = f"{self._prev_color}⮪ [0] {(self._entries.get(0)).description} program{self.__end_color}"

        if (self.draw_mode == "classic"):
            print(prev_button)

            print(self._title_color, f"\n\t~{self._title}~", self.__end_color)

            # Print every entry
            for key in range(1, len(self._entries.keys()) + 1):
                if (self._entries.get(key) is not None):
                    # local vars to make PEP-8 compliance possible
                    # 'f' prefix for 'format'
                    f_end_color = self.__end_color
                    f_key = f"{self._option_color}[ {key} ] : {f_end_color}"
                    f_description = f"{(self._entries.get(key)).description}"
                    f_entry = f"{self._entry_color}{f_description}{f_end_color}"
                    print(f_key, f_entry, sep="")

        elif (self.draw_mode == "experimental"):

            box_title = self._title
            box_prev = f"⮪ [0] {(self._entries.get(0)).description}"
            box_data = []

            for key in range(1, len(self._entries.keys()) + 1):
                if (self._entries.get(key) is not None):
                    box_data.append(
                        f"[ {key} ] : {(self._entries.get(key)).description}")

            Boxxy(box_title, box_prev, box_data, "single", 5)

        if self._enable_input:
            # Result of this call is a validated key from user
            # stored in 'self._user_input'
            self.get_validated_input()

        self.wipe_prints()

    def make_me_submenu(self, parent_menu):
        # Create back button that invokes parent_menu
        back_entry = Entry("Back", parent_menu)
        self._entries.update({0: back_entry})

        self._parent_menu = parent_menu
        self._is_submenu = True

    def give_entry(self, requested_descr):
        # Returns <Entry object> that has the requested description.
        for entry in self._entries:
            if self._entries.get(entry).description == requested_descr:
                return self._entries.get(entry)

    # Evaluates entries and returns a dictionary of entries
    # DO NOT TOUCH!
    def _eval_entries(self, dirty_entries):
        # Create Dictionary
        clean_entries = {}

        # Set starting option value
        option_val = 1
        for entry in dirty_entries:
            # Loop through each dirty entry, and append option_val as key
            # and entry as value.
            clean_entries.update({option_val: entry})
            # Increment option_val
            option_val += 1

        # return dictionary
        return clean_entries
