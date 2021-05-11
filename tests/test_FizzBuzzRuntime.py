from unittest import TestCase as __tc__
from fizzbuzzpurepython import FizzBuzzRuntime as __rt__


class TestFizzBuzzRuntime(__tc__):
    def test_is_fizz(self):
        self.assertEqual(__rt__().is_fizz(3),
                         True)
