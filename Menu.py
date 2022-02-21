#!/usr/bin/env python3

import subprocess
import sys
import os
from Entry import Entry
from Prettify import Prettify

class Menu:
    def __init__(self, title, entries):
        # Handle params
        self._title = title
        self._entries = self._eval_entries(entries)
        
        # Sub menu pre-reqs
        self._is_submenu = False
        self._parent_menu = None
        self._wipe_on_input = False
        
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
            UnboundLocalError
        )
        
        # Adds default quit button.
        quit_entry = Entry(self._quit_keyword)
        self._entries.update({0 : quit_entry})
        
    def start(self):
        # Menu Loop
        while True:
            # Draw Menu and get validated input
            self.draw_menu()
            
            # Quits Menu
            # Should only ever be called by Top Level Menu
            # DO NOT add quit entry to a sub menu. Add a back entry instead.
            if (self._entries.get(self._user_input).description == self._quit_keyword):
                break
        
            # Invoke what entry references
            entry = self._entries.get(self._user_input)
            if (isinstance(entry.invoke, Menu)):
                # Do submenu things
                entry.invoke.start()
                break
            else:
                if (entry.invoke_params == None):
                    entry.invoke()
                else:
                    entry.invoke(*entry.invoke_params())

    def verbose_errors(self, toggle):
        self._verbose_errors = toggle
        
    def wipe_prints(self):
        if (self._wipe_on_input):
            # Get Count
            # +2 due to input and title line.
            line_count = len(self._entries.keys()) + 2
            # Place Cursor and clear menu
            print(f"\033[{line_count}F\033[J", end="")
        
    def get_validated_input(self):
        """ Sets self._user_input to a validated key that can be used to access one of 
            the existing entries.
        """
        try:
            self._user_input = int(input(self._request_msg))
            test_key = self._entries.get(self._user_input)
            # Forcefully set input and test_key. Run validation afterwards.
            if (test_key == None):
                raise ValueError("Entry does not exist.")
            
        except self._check_errors as e:
            print_error = ""
            
            if (type(e) == EOFError):
                # Keeps consistency in feedback in terms of format.
                if (self._verbose_errors):
                    print_error = f"{self._error_msg}, {e}"
                else:
                    print_error = f"{self._error_msg}"
                self.wipe_prints()
                print(print_error)
                self.draw_menu()
            else:
                if (self._verbose_errors):
                    print_error = f"{self._error_msg} {e}"
                else:
                    print_error = f"{self._error_msg}"
                self.wipe_prints()
                print(print_error)
                self.draw_menu()


    def draw_menu(self):
        """ Draws menu and correlated sub menus to stdout.

        Args:
            do_input (bool, optional): Request input immediately after drawing. Defaults to False.
        """
        if (self._is_submenu):
            print(f"← [ 0 ] : {(self._entries.get(0)).description} to {self._parent_menu._title}")
        else:
            print(Prettify.RED, f"← [ 0 ] : {(self._entries.get(0)).description} program", Prettify.END)

        print(f"\n{self._title}")
        
        # Print every entry
        for key in range(1, len(self._entries.keys())+1):
            if (self._entries.get(key) != None):
                print(f"[ {key} ] : {(self._entries.get(key)).description}")
                
        if (self._enable_input):
            # Result of this call is a validated key from user stored in 'self._user_input'
            self.get_validated_input()
            
        self.wipe_prints()
    
    def make_me_submenu(self, parent_menu):
        # Create back button that invokes parent_menu
        back_entry = Entry("Back", parent_menu)
        self._entries.update({0 : back_entry})
        
        self._parent_menu = parent_menu
        self._is_submenu = True
        
    def give_entry(self, requested_descr):
        # Returns <Entry object> that has the requested description.
        for entry in self._entries:
            if (self._entries.get(entry).description == requested_descr):
                return self._entries.get(entry)
    
    # Evaluates entries and returns a dictionary of entries
    def _eval_entries(self, dirty_entries):
        # Create Dictionary
        clean_entries = {}

        # Set starting option value
        option_val = 1
        for entry in dirty_entries:
            # Loop through each dirty entry, and append option_val as key and entry as value.
            clean_entries.update({option_val : entry})
            # Increment option_val
            option_val += 1
        
        #return dictionary
        return clean_entries