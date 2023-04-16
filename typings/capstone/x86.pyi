"""
This type stub file was generated by pyright.
"""

import ctypes
from .x86_const import *

class X86OpMem(ctypes.Structure):
    _fields_ = ...


class X86OpValue(ctypes.Union):
    _fields_ = ...


class X86Op(ctypes.Structure):
    _fields_ = ...
    @property
    def imm(self): # -> Any:
        ...
    
    @property
    def reg(self): # -> Any:
        ...
    
    @property
    def mem(self): # -> Any:
        ...
    


class CsX86Encoding(ctypes.Structure):
    _fields_ = ...


class CsX86(ctypes.Structure):
    _fields_ = ...


def get_arch_info(a): # -> tuple[Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, list[Any]]:
    ...

