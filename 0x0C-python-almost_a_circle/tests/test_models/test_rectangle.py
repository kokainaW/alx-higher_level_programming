#!/usr/bin/python3
""" In this module, testing related to Base class will be done. """
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base
# Check message or just exception raised?


class TestRectangle(unittest.TestCase):
    """ Test the Rectangle class that inherits from Base. """

    def tearDown(self):
        """ Create environment. """
        Base.reset_nb()

    def test_1init(self):
        """ Test cases of normal initialization """

        # 5 parameters
        r2 = Rectangle(1, 2, 3, 4, 10)
        self.assertEqual(r2.id, 10)

        # 4 parameters
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.id, 1)

        # 3 parameters
        r4 = Rectangle(1, 2, 3)
        self.assertEqual(r4.id, 2)

        # 2 parameters
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.id, 3)

        # 5 parameters - Initialize in 0 x and y
        r2 = Rectangle(1, 2, 0, 0)
        self.assertEqual(r2.id, 4)

    def test_failure_parameters(self):
        """ Cases additional, none or less parameters are passed. """

        # MESSAGE OR JUST RAISE?
        # None parameters
        with self.assertRaises(TypeError):
            r5 = Rectangle()

        # Less than required
        with self.assertRaises(TypeError):
            r6 = Rectangle(1)

        # More than required
        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 2, 3, 4, 5, 6)

    def test_failure_value_args(self):
        """ Test cases invalid value of args, negatives or zeros. """

        # Negatives values in dimensions or id
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r8 = Rectangle(-1, 1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r9 = Rectangle(1, -1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r10 = Rectangle(1, 1, -1, 2)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r11 = Rectangle(1, 1, 1, -2)

        # Value zero in dimensions
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r12 = Rectangle(0, 1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r13 = Rectangle(1, 0)

    def test_failure_type_args(self):
        """ Test cases invalid args are passed, types of data. """

        # LIST
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r14 = Rectangle([1], 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r15 = Rectangle(1, [1])

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r16 = Rectangle(1, 1, [1])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r17 = Rectangle(1, 1, 2, [0])

        # FLOAT
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r18 = Rectangle(1.1, 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r19 = Rectangle(1, 1.1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r20 = Rectangle(1, 1, 1.2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r21 = Rectangle(1, 1, 2, 1.3)

        # STRING
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r22 = Rectangle("1", 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r23 = Rectangle(1, "1")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r24 = Rectangle(1, 1, "1")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r25 = Rectangle(1, 1, 2, "1")

        # DICTIONARY
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r26 = Rectangle({1: 1}, 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r27 = Rectangle(1, {1: 1})

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r28 = Rectangle(1, 1, {1: 1})

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r29 = Rectangle(1, 1, 2, {1: 1})

    def test_setter_getter(self):
        """ Test setting and getting a new value. """

        # Check if I can do this
        r29 = Rectangle(7, 8)  # 5
        self.assertEqual(r29.width, 7)

        # set width
        r29.width = 3
        # get width
        self.assertEqual(r29.width, 3)

        # set height
        r29.height = 3
        # get height
        self.assertEqual(r29.height, 3)

        # set x
        r29.x = 8
        # get x
        self.assertEqual(r29.x, 8)

        # set y
        r29.y = 8
        # get y
        self.assertEqual(r29.y, 8)

        # EXCEPTIONS when setting - value errors
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r29.width = -1

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r29.width = 0

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r29.height = -1

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r29.height = 0

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r29.x = -1

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r29.y = -1

        # EXCEPTIONS when setting - type errors
        # width
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r29.width = {1}

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r29.width = [1]

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r29.width = 1.1

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r29.width = "1"

        # height
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r29.height = {1}

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r29.height = [1]

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r29.height = 1.1

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r29.height = "1"

        # x
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r29.x = {1}

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r29.x = [1]

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r29.x = 1.1

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r29.x = "1"

        # y
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r29.y = {1}

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r29.y = [1]

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r29.y = 1.1

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r29.y = "1"

    def test_area(self):
        """ Test cases of normal use of area method. """

        # 2 parameters
        r30 = Rectangle(3, 2)
        self.assertEqual(r30.area(), 6)

        # 3 parameters
        r31 = Rectangle(3, 4, 2)
        self.assertEqual(r31.area(), 12)

        # 4 parameters
        r32 = Rectangle(3, 5, 2, 1)
        self.assertEqual(r32.area(), 15)

        # 5 parameters
        r33 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r33.area(), 56)

    def test_display(self):
        """ Test case to display the rectangle. """
        stdout_line = sys.stdout

        # 2 parameters
        out = StringIO()
        sys.stdout = out
        r34 = Rectangle(3, 2)
        r34.display()
        output = out.getvalue()
        self.assertEqual(output, "###\n###\n")

        # 3 parameters
        out = StringIO()
        sys.stdout = out
        r35 = Rectangle(2, 3, 2)
        r35.display()
        output = out.getvalue()
        self.assertEqual(output, "  ##\n  ##\n  ##\n")

        # 4 parameters
        out = StringIO()
        sys.stdout = out
        r36 = Rectangle(3, 5, 2, 1)
        r36.display()
        output = out.getvalue()
        self.assertEqual(output, "\n  ###\n  ###\n  ###\n  ###\n  ###\n")

        # 5 parameters
        out = StringIO()
        sys.stdout = out
        r37 = Rectangle(1, 2, 0, 0, 12)
        r37.display()
        output = out.getvalue()
        self.assertEqual(output, "#\n#\n")

    def test_print_object(self):
        """ Test case to print rectangle info. """

        # 2 parameters
        out = StringIO()
        sys.stdout = out
        r38 = Rectangle(3, 2)
        print(r38)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (1) 0/0 - 3/2\n")

        # 3 parameters
        out = StringIO()
        sys.stdout = out
        r39 = Rectangle(2, 3, 2)
        print(r39)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (2) 2/0 - 2/3\n")

        # 4 parameters
        out = StringIO()
        sys.stdout = out
        r40 = Rectangle(3, 5, 2, 1)
        print(r40)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (3) 2/1 - 3/5\n")

        # 5 parameters
        out = StringIO()
        sys.stdout = out
        r41 = Rectangle(1, 2, 0, 0, 20)
        print(r41)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (20) 0/0 - 1/2\n")

    def test_update(self):
        """ Test case to update rectangles attributes. """

        # UPDATE NONE
        out = StringIO()
        sys.stdout = out
        r42 = Rectangle(10, 10, 10, 10)
        r42.update()
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (1) 10/10 - 10/10\n")

        # UPDATE ARGS
        # update 1 parameter (id)
        out = StringIO()
        sys.stdout = out
        r42.update(89)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (89) 10/10 - 10/10\n")

        # update 2 parameter (id, width)
        out = StringIO()
        sys.stdout = out
        r42.update(89, 2)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (89) 10/10 - 2/10\n")

        # update 3 parameter (id, width, height)
        out = StringIO()
        sys.stdout = out
        r42.update(89, 2, 3)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (89) 10/10 - 2/3\n")

        # update 4 parameter (id, width, height, x)
        out = StringIO()
        sys.stdout = out
        r42.update(89, 2, 3, 4)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (89) 4/10 - 2/3\n")

        # update 5 parameter (id, width, height, x, y)
        out = StringIO()
        sys.stdout = out
        r42.update(89, 2, 3, 4, 5)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (89) 4/5 - 2/3\n")

        # more than 5 parameters passed
        out = StringIO()
        sys.stdout = out
        r42.update(89, 2, 3, 4, 5, 6)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (89) 4/5 - 2/3\n")

        # UPDATE KWARGS
        # update 2 parameter
        out = StringIO()
        sys.stdout = out
        r42.update(height=1)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (89) 4/5 - 2/1\n")

        # update 2 parameters
        out = StringIO()
        sys.stdout = out
        r42.update(height=1, width=1)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (89) 4/5 - 1/1\n")

        # update 3 parameters
        out = StringIO()
        sys.stdout = out
        r42.update(height=1, width=1, x=2)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (89) 2/5 - 1/1\n")

        # update 4 parameters
        out = StringIO()
        sys.stdout = out
        r42.update(height=1, width=1, x=2, y=3)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (89) 2/3 - 1/1\n")

        # update 5 parameters
        out = StringIO()
        sys.stdout = out
        r42.update(height=1, width=1, x=2, y=3, id=90)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (90) 2/3 - 1/1\n")

        # update more tha 5 parameters
        out = StringIO()
        sys.stdout = out
        r42.update(height=1, width=1, x=2, y=3, id=90, depth=90)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (90) 2/3 - 1/1\n")

        # UPDATE having both cases
        out = StringIO()
        sys.stdout = out
        r42.update(201, height=3, width=2, x=4, y=7, id=98)
        print(r42)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (201) 2/3 - 1/1\n")

        # UPDATE with errors
        # error with size (id, width)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r42.update(500, 3.1)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r42.update(500, -1)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r42.update(500, 0)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r42.update(width=3.1)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r42.update(width=-1)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r42.update(width=0)

        # error with height (id, width, height)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r42.update(500, 3, 3.1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r42.update(500, 3, -1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r42.update(500, 3, 0)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r42.update(height=3.1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r42.update(height=-1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r42.update(height=0)

        # error with x (id, width, height, x)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r42.update(500, 10, 3, 3.1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r42.update(500, 10, 3, -1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r42.update(x=3.1)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r42.update(x=-1)

        # error with y (id, width, height, x, y)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r42.update(500, 10, 10, 10, 3.1)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r42.update(500, 10, 10, 10, -1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r42.update(y=3.1)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r42.update(y=-1)

    def test_to_dictionary(self):
        """ Test to_dictionary function is addecuate. """
        r1 = Rectangle(1, 2, 3, 4, 12)
        dictionary = {"id": 12, "width": 1, "height": 2, "x": 3, "y": 4}
        self.assertEqual(r1.to_dictionary(), dictionary)

        r2 = Rectangle(1, 2)
        dictionary = {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}
        self.assertEqual(r2.to_dictionary(), dictionary)

        r3 = Rectangle(1, 2, 3)
        dictionary = {"id": 2, "width": 1, "height": 2, "x": 3, "y": 0}
        self.assertEqual(r3.to_dictionary(), dictionary)

        r4 = Rectangle(1, 2, 3, 4)
        dictionary = {"id": 3, "width": 1, "height": 2, "x": 3, "y": 4}
        self.assertEqual(r4.to_dictionary(), dictionary)

    def test_to_json_string(self):
        """ Test to JSON string method """

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            out = StringIO()
            sys.stdout = out
            print(file.read())
            output = out.getvalue()
            self.assertIn("\"y\": 8", output)
            self.assertIn("\"x\": 2", output)
            self.assertIn("\"id\": 1", output)
            self.assertIn("\"width\": 10", output)
            self.assertIn("\"height\": 7", output)
            self.assertIn("\"y\": 0", output)
            self.assertIn("\"x\": 0", output)
            self.assertIn("\"id\": 2", output)
            self.assertIn("\"width\": 2", output)
            self.assertIn("\"height\": 4", output)

    def test_save_to_file(self):
        """ Test save to file empty list """
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            out = StringIO()
            sys.stdout = out
            print(file.read())
            output = out.getvalue()
            self.assertEqual(output, "[]\n")

        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            out = StringIO()
            sys.stdout = out
            print(file.read())
            output = out.getvalue()
            self.assertEqual(output, "[]\n")

    def test_create(self):
        """ Test the create class method. """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)
        # Try empty

    def test_load_from_file(self):
        """ Tests load from file json """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        i = 0
        for rect in list_rectangles_output:
            list_rect = ["[Rectangle] (1) 2/8 - 10/7\n", "[Rectangle] (2) 0/0 - 2/4\n"]
            out = StringIO()
            sys.stdout = out
            print(rect)
            output = out.getvalue()
            self.assertEqual(output, list_rect[i])
            i += 1
