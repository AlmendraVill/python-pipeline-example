import numpy as np

class GeometryCalculator:
    def rectangle_area(self, width, length):
        if width <= 0 or length <= 0:
            raise ValueError("Width and length must be positive numbers.")
        return length * width
    
    def rectangle_perimeter(self, width, length):
        if width <= 0 or length <= 0:
            raise ValueError("Width and length must be positive numbers.")
        return 2 * (length + width)
    
    def circle_area(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return np.pi * radius ** 2
    
    def circle_circumference(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return 2 * np.pi * radius
    
if __name__ == "__main__":
    calculator = GeometryCalculator()
    
    # Example usage
    print("Rectangle Area (5, 10):", calculator.rectangle_area(5, 10))
    print("Rectangle Perimeter (5, 10):", calculator.rectangle_perimeter(5, 10))
    print("Circle Area (7):", calculator.circle_area(7))
    print("Circle Circumference (7):", calculator.circle_circumference(7))