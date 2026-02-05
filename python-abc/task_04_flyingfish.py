#!/usr/bin/env python3
"""Defines Fish, Bird and FlyingFish classes (multiple inheritance)."""


class Fish:
    """Fish class."""

    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Bird class."""

    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class inheriting from Fish and Bird."""

    def fly(self):
        """Override fly behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat behavior."""
        print("The flying fish lives both in water and the sky!")
