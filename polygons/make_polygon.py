"""
Python module to create equilateral polygons.
"""

from math import sin, cos, radians

class Polygon():
    """Class to define a polygon object."""

    def __init__(self):
        self.name = 'Polygon'
        self.n_sides = 4
        self.radius = 10
        self.side_length = self._calc_side_from_radius_(n_sides=self.n_sides, radius=self.radius)
        self.apothem_length = self._calc_apothem_(n_sides=self.n_sides, radius=self.radius)
        self.area = self._calc_area_(n_sides=self.n_sides, side_length=self.side_length, apothem=self.apothem_length)
        self.perimeter = self._calc_perimeter_(n_sides=self.n_sides, side_length=self.side_length)

    def set_name(self, name='Polygon'):
        """Method to set polygon name"""
        self.name = name

    def get_name(self):
        """Returns the polygon's name"""
        return self.name

    def set_n_sides(self, n_sides):
        """Method to set the polygon's number of sides"""
        self._validate_polygon_(n_sides)
        self.n_sides = n_sides
        self._update_polygon_(param='radius')

    def get_n_sides(self):
        """Returns the polygon's number of sides."""
        return self.n_sides

    def set_radius(self, radius=3):
        """Method to set the polygon's radius."""
        self._validate_length_(radius)
        self.radius = radius
        self._update_polygon_(param='radius')

    def get_radius(self):
        """Returns the polygon's radius."""
        return self.radius

    def set_side_length(self, side_length):
        """Method to set the polygon's side length."""
        self._validate_length_(side_length)
        self.side_length = side_length
        self._update_polygon_(param='side')

    def get_side_length(self):
        """Returns the length of the polygon's sides"""
        return self.side_length

    def get_area(self):
        """Returns the polygon area."""
        return self.area

    def get_perimeter(self):
        """Returns the polygon perimeter."""
        return self.perimeter

    def get_apothem_length(self):
        """Returns the length of the polygon's apothem."""
        return self.apothem_length

    def info(self):
        """Prints polygon parameters."""
        print('###  POLYGON PARAMETERS  ###')
        print('NAME : ', self.name)
        print('NUM SIDES : ', self.n_sides)
        print('RADIUS : ', self.radius)
        print('SIDE LENGTH : ', self.side_length)
        print('APOTHEM LENGTH : ', self.apothem_length)
        print('AREA : ', self.area)

    @staticmethod
    def _calc_radius_from_side_(n_sides, side_length):
        """Calculate polygon radius from given side length and number of sides"""
        return side_length / sin(radians(180.)/n_sides) / 2

    @staticmethod
    def _calc_side_from_radius_(n_sides, radius):
        """Calculate polygon radius from given side length and number of sides"""
        return 2 * radius * sin(radians(180.)/n_sides)

    @staticmethod
    def _calc_apothem_(n_sides, radius):
        """Calculate polygon apothem."""
        return radius * cos(radians(180.)/n_sides)

    @staticmethod
    def _calc_area_(n_sides, side_length, apothem):
        """Calculate the polygon area."""
        return n_sides * side_length * apothem / 2

    @staticmethod
    def _calc_perimeter_(n_sides, side_length):
        """Calculate the polygon perimeter."""
        return n_sides * side_length

    def _update_polygon_(self, param):
        """Update the polygon parameters based on changed parameter."""
        if param == 'radius':
            self.side_length = self._calc_side_from_radius_(n_sides=self.n_sides, radius=self.radius)
        else:
            self.radius = self._calc_radius_from_side_(n_sides=self.n_sides, side_length=self.side_length)
        self.apothem_length = self._calc_apothem_(n_sides=self.n_sides, radius=self.radius)
        self.area = self._calc_area_(n_sides=self.n_sides, side_length=self.side_length, apothem=self.apothem_length)
        self.perimeter = self._calc_perimeter_(n_sides=self.n_sides, side_length=self.side_length)

    @staticmethod
    def _validate_polygon_(n_sides):
        """Validate that n_sides is a positive integer greater or equal to 3."""
        if (n_sides >= 3) and (isinstance(n_sides, int)):
            return True
        else:
            raise ValueError("Polygon n_sides parameter must be an integer greater than or equal to 3.")

    @staticmethod
    def _validate_length_(length):
        """Validate that length is a positive number."""
        if (length > 0) and (isinstance(length, (int, float))):
            return True
        else:
            raise ValueError("Polygon length parameter must be a positive number greater than 0.")