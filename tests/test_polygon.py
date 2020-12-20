
import unittest
from polygons.make_polygon import Polygon

NAME = 'test_polygon'
N_SIDES = 4
RADIUS = 7.071067811865475
APOTHEM = 5.
SIDE = 10.
AREA = 100.
PERIMETER = 40.

class Test_Polygon(unittest.TestCase):

    def setUp(self):
        self.polygon = Polygon()

    def test_set_name(self):
        """Test set_name method."""
        self.polygon.set_name(name=NAME)
        self.assertTrue(self.polygon.name == NAME)

    def test_get_name(self):
        """Test get_name method."""
        self.polygon.set_name(name=NAME)
        name = self.polygon.get_name()
        self.assertTrue(name == NAME)

    def test_set_n_sides(self):
        """Test set_n_sides method."""
        self.polygon.n_sides = N_SIDES
        self.polygon.radius = RADIUS
        self.polygon.side_length = SIDE
        self.polygon.set_n_sides(N_SIDES)
        self.assertTrue(self.polygon.n_sides == N_SIDES)
        self.assertEqual(round(self.polygon.radius, 6), round(RADIUS, 6))
        self.assertEqual(round(self.polygon.apothem_length, 6), APOTHEM)
        self.assertEqual(round(self.polygon.area, 6), AREA)
        self.assertEqual(self.polygon.perimeter, PERIMETER)
        with self.assertRaises(ValueError):
            self.polygon.set_n_sides(-1)
            self.polygon.set_n_sides(float(N_SIDES))
            self.polygon.set_n_sides(-1.)

    def test_get_n_sides(self):
        """Test get_n_sides method."""
        self.polygon.set_n_sides(n_sides=N_SIDES)
        self.assertEqual(self.polygon.get_n_sides(), N_SIDES)

    def test_set_radius(self):
        """Test set_radius method."""
        self.polygon.n_sides = N_SIDES
        self.polygon.radius = RADIUS
        self.polygon.side_length = SIDE
        self.polygon.set_radius(RADIUS)
        self.assertEqual(self.polygon.radius, RADIUS)
        self.assertEqual(round(self.polygon.radius, 6), round(RADIUS, 6))
        self.assertEqual(round(self.polygon.apothem_length, 6), APOTHEM)
        self.assertEqual(round(self.polygon.area, 6), AREA)
        self.assertEqual(self.polygon.perimeter, PERIMETER)
        with self.assertRaises(ValueError):
            self.polygon.set_radius(-1)

    def test_get_radius(self):
        """Test get_radius_method."""
        self.polygon.set_radius(radius=RADIUS)
        self.assertEqual(self.polygon.get_radius(), RADIUS)

    def test_set_side_length(self):
        """Test set_side_length method."""
        self.polygon.n_sides = N_SIDES
        self.polygon.radius = RADIUS
        self.polygon.side_length = SIDE
        self.polygon.set_side_length(SIDE)
        self.assertEqual(self.polygon.side_length, SIDE)
        self.assertEqual(round(self.polygon.radius, 6), round(RADIUS, 6))
        self.assertEqual(round(self.polygon.apothem_length, 6), APOTHEM)
        self.assertEqual(round(self.polygon.area, 6), AREA)
        self.assertEqual(self.polygon.perimeter, PERIMETER)
        with self.assertRaises(ValueError):
            self.polygon.set_side_length(-1)

    def test_get_side_length(self):
        """Test get_side_length method."""
        self.polygon.set_n_sides(N_SIDES)
        self.polygon.set_radius(RADIUS)
        sl = self.polygon.get_side_length()
        self.assertEqual(round(sl, 6), SIDE)

    def test_get_area(self):
        """Test get_area method."""
        self.polygon.set_n_sides(N_SIDES)
        self.polygon.set_side_length(SIDE)
        self.assertEqual(round(self.polygon.get_area(), 6), AREA)

    def test_get_apothem_length(self):
        """Test get_apothem_length method."""
        self.polygon.set_n_sides(N_SIDES)
        self.polygon.set_radius(RADIUS)
        ap = self.polygon.get_apothem_length()
        self.assertEqual(round(ap, 6), APOTHEM)

    def test_calc_radius_from_side_(self):
        """Test _calc_radius_from_side_ method."""
        self.assertEqual(round(self.polygon._calc_radius_from_side_(n_sides=N_SIDES, side_length=SIDE), 6),
                         round(RADIUS, 6))

    def test_calc_side_from_radius_(self):
        """Test _calc_side_from_radius_ method."""
        self.assertEqual(round(self.polygon._calc_side_from_radius_(n_sides=N_SIDES, radius=RADIUS), 6), SIDE)

    def test_calc_apothem_(self):
        """Test _calc_apothem_ method."""
        self.assertEqual(round(self.polygon._calc_apothem_(n_sides=N_SIDES, radius=RADIUS), 6), APOTHEM)

    def test_calc_area_(self):
        """Test _calc_area_ method."""
        self.assertEqual(self.polygon._calc_area_(n_sides=N_SIDES, side_length=SIDE, apothem=APOTHEM), AREA)

    def test_calc_perimeter_(self):
        """Test _calc_perimeter_ method."""
        self.assertEqual(self.polygon._calc_perimeter_(n_sides=N_SIDES, side_length=SIDE), PERIMETER)

    def test_validate_polygon_(self):
        """Test _validate_polygon_ method."""
        self.assertTrue(self.polygon._validate_polygon_(N_SIDES))
        with self.assertRaises(ValueError):
            self.polygon._validate_polygon_(-1)
            self.polygon._validate_polygon_(float(N_SIDES))
            self.polygon._validate_polygon_(-1.)

    def test_validate_length_(self):
        """Test _validate_length_ method."""
        self.assertTrue(self.polygon._validate_length_(SIDE))
        with self.assertRaises(ValueError):
            self.polygon._validate_length_(-1)
            self.polygon._validate_length_(NAME)


if __name__ == '__main__':
    unittest.main()