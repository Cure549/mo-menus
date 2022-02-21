#!/usr/bin/env python3

class Entry:
    def __init__(self, description, invoke=None, *invoke_params):
        self._description = description # Description shown in stdout
        
        # When invoke is called, it will either open a sub menu or call a function.
        # Based off the referenced type. Menu || Method || Function
        self._invoke = invoke
        self._invoke_params = invoke_params
        
    def invoke_params(self):
        return self._invoke_params
    
    def opens_menu(self, menu):
        self._invoke = menu
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, new_description):
        self._description = new_description
        
    @property
    def invoke(self):
        return self._invoke
    
    @invoke.setter
    def invoke(self, new_invoke):
        self._invoke = new_invoke