import unittest     #unittest framework uses classes and inherritance
                    #to create tests we create a class that iherrits from test case class and the framework
                    #then we write methods inside that class for the actual tests
import boggle
"""
class test_boggle(unittest.TestCase):       #class that inherrits from TestCase
    def test_is_this_thing_on(self):        #method..starts with test_
        self.assertEqual(1, 1)       #method assertEqual..method inherrited from test_case class. is 1 = 0? 1=1?
                                    #test command python3 -m unittest((in the command line))
"""
class TestBoggle(unittest.TestCase):
    #Our test suite for boggle solver
    
    
    def test_can_create_an_empty_grid(self):
        
        #Test to see if we can create an empty grid
        grid = boggle.make_grid(0,0)        ##(0,0) height/with or row/column. (0,0)=no rows or columns
        self.assertEqual(len(grid),0)
        
    def test_grid_size_is_width_times_height(self):
        
        #test to ensure total size of grid = width x height
        
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
        
        
    def test_grid_coordinates(self):
        
        #test 2 ensure all coordinates inside grid can be accessed
        
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)     #assertIn method to check if (0,0) is in a 2x2 grid
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)  #assertNot in to check (2,2) is not in a 2x2 grid
        
        
        
        