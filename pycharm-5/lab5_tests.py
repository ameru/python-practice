poly1 = [2.3, 4.7, 1.0]
poly2 = [1.2, 2.1, -3.2]

def test_poly_add(self):
    poly1 = [2.3, 4.7, 1.0]
    poly2 = [1.2, 2.1, -3.2]
    poly3 = poly.polyadd2(poly1, poly2)
    self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])

def test_poly_mult(self):
    poly1 = [2.3, 4.7, 1.0]
    poly2 = [1.2, 2.1, -3.2]
    poly3 = poly.polymult2(poly1, poly2)
    self.assertListAlmostEqual(poly3, [2.76, 9.87, -3.2])

def test_poly_square_all(self):
    poly1 = [2.3, 4.7, 1.0]
    poly3 = poly.polysquare_all2(poly1 + poly2)
    self.assertListAlmostEqual(poly3, [12.25, 46.24, 4.84])

def test_poly_all_n_all(self):
    poly1 = [2.3, 4.7, 1.0]
    poly2 = [1.2, 2.1, -3.2]
    poly3 = poly.polyall_n_all2(poly1, poly2)
    self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])

def test_poly_even_or_odd_all(self):
    poly1 = [2.3, 4.7, 1.0]
    poly2 = [1.2, 2.1, -3.2]
    if x % 2 == 0:
            return True
    if x % 2 == 1:
            return False
    self.assertListAlmostEqual(poly1, [True, False, False])
    self.assertListAlmostEqual(poly2, [False, True, False])