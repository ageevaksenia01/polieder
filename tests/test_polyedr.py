import unittest
from unittest.mock import patch, mock_open
from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """10.0	30.0	0.0	20.0
8 2 8
-10 -10 10
-10 10 10
10 10 10
10 -10 10
4 2 0
4 -2 0
0 -2 0
0 2 0
4 1 2 3 4
4 5 6 7 8"""
        fake_file_path = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 2)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 8)

    def test_num_area_ob(self):
        self.assertEqual(self.polyedr.area_ob, 16)

