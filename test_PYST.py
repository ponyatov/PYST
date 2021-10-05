from PYST import *
import pytest

def test_any(): assert True

def test_hello():
    Object('hello').test() == '\n<object:hello>'

def test_vm():
    vm.head(test=True) == '\n<vm:Smalltalk>'
