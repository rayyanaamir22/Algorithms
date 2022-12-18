from __future__ import annotations

class Complex:
    """
    Complex number class.
    """
    def __init__(self, real: float, imaginary: float) -> None:
        """
        Constructor.
        """
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other: Complex) -> Complex:
        """
        Add complex numbers.
        """
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)

    def __sub__(self, other: Complex) -> Complex:
        """
        Subtract complex numbers.
        """
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return Complex(real, imaginary)
    
    def __mul__(self, other: Complex) -> Complex:
        """
        Multiply complex numbers.
        """
        real = self.real * other.real
        imaginary = self.imaginary * other.imaginary
        return Complex(real, imaginary)
    
    def __truediv__(self, other: Complex) -> Complex:
        """
        Divide complex numbers.
        """
        real = round(self.real / other.real, 2)
        imaginary = round(self.imaginary / other.imaginary, 2)
        return Complex(real, imaginary)