import unittest     #unittest framework uses classes and inherritance
                    #to create tests we create a class that iherrits from test case class and the framework
                    #then we write methods inside that class for the actual tests
class test_boggle(unittest.TestCase):       #class that inherrits from TestCase
    def test_is_this_thing_on(self):        #method..starts with test_
        self.assertEqual(1, 1)       #method assertEqual..method inherrited from test_case class. is 1 = 0? 1=1?
                                    #test command python3 -m unittest((in the command line))