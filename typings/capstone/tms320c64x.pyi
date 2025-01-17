"""
This type stub file was generated by pyright.
"""

import ctypes
from .tms320c64x_const import *

class TMS320C64xOpMem(ctypes.Structure):
    _fields_ = ...


class TMS320C64xOpValue(ctypes.Union):
    _fields_ = ...


class TMS320C64xCondition(ctypes.Structure):
    _fields_ = ...


class TMS320C64xFunctionalUnit(ctypes.Structure):
    _fields_ = ...


class TMS320C64xOp(ctypes.Structure):
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
    


class CsTMS320C64x(ctypes.Structure):
    _fields_ = ...


def get_arch_info(a): # -> tuple[Unknown, Unknown, Unknown, Unknown]:
    ...

