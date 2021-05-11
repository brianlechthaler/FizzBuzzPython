from unittest import TestCase as __tc__
from fizzbuzzpurepython import DivisibilityCheck as __divcheck__


class TestDivisibilityCheck(__tc__):
    def test_euclidian_quotient(self):
        # Create a new DivisibilityCheck object
        divcheck = __divcheck__(3,1)
        # Get the DivisibilityCheck object's Euclidian Quotient
        euclqout = divcheck.euclidian_quotient()
        # Pass this test if the generated Euclidian Quotient is what it should be
        self.assertEqual(euclqout,
                         0)

    def test_evenly_divisible(self):
        # Create a new DivisibilityTest object
        divcheck = __divcheck__(4,2)
        # Get the DivisibilityCheck object's evenly_divisible boolean value
        dchkbool = divcheck.evenly_divisible()
        # Pass this test if the generated boolean value is True like it should be
        self.assertEqual(dchkbool,
                         True)
