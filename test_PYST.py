from PYST import *
import pytest

def test_any(): assert True

def test_hello():
    Object('hello').test() == '\n<object:hello>'

def test_vm():
    vm.head(test=True) == '\n<vm:Smalltalk>'

def test_bc_push():
    assert push().test() == '\n<push:0>'
    assert push(1).test() == '\n<push:1>'

def test_bc_math():
    assert add().test() == '\n<add:176>'
    assert push2().test() == '\n<push2:119>'
