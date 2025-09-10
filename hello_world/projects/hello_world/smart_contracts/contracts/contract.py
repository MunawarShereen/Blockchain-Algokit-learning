from algopy import ARC4Contract, String, UInt64
from algopy.arc4 import abimethod


class Contracts(ARC4Contract):
    @abimethod(name="hello_world")
    def hello(self, name: String) -> String:
        return "Hello, " + name

    @abimethod()
    def add(self, a: UInt64, b: UInt64) -> UInt64:
        return a + b

    @abimethod()
    def subtract(self, a : UInt64 , b:UInt64 ) -> UInt64:
        return a-b

    @abimethod()
    def multiply(self, a:UInt64 , b: UInt64) -> UInt64:
        return a*b



