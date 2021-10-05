## @file
## @brief Smalltalkish in Python

import config
import os, sys

## generic root object
class Object:
    def __init__(self, V):
        self.value = V

    ## @name dump

    ## `print` callback
    def __repr__(self): return self.dump()

    ## `pytest` callback
    def test(self): return self.dump(test=True)

    ## full text tree dump
    def dump(self, depth=0, prefix='', test=False):
        # head
        def pad(depth): return '\n' + '\t' * depth
        ret = pad(depth) + self.head(prefix, test)
        # subtree
        return ret

    ## short `<T:V>` header
    def head(self, prefix='', test=False):
        return f'{prefix}<{self.tag()}:{self.val()}>'

    ## object class/type tag
    def tag(self): return self.__class__.__name__.lower()

    ## object value for dumps and slot names
    def val(self): return f'{self.value}'

## scalar type
class Primitive(Object): pass

## floating point
class Number(Object): pass

## integer
class Integer(Number): pass

class Hex(Integer): pass

class Bin(Integer): pass

class String(Primitive): pass

class Nil(Primitive): pass

## executable
class Active(Object): pass

## program representation (low-level bytecode commands)
class ByteCode(Active): pass

## Virtual Machine
class VM(Active): pass

vm = VM('Smalltalk')

## system init
if __name__ == '__main__':
    print(vm)
