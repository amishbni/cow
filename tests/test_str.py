import unittest
from copyonwrite import cow

class TestCoWString(unittest.TestCase):
    def setUp(self):
        """Initialize a shared string for testing."""
        self.original_string = "hello"
        self.cow_string = cow(self.original_string)

    def test_initialization(self):
        """Test if the CoW string initializes correctly."""
        self.assertEqual(self.cow_string, "hello")
        self.assertEqual(self.original_string, "hello")  # Ensure original is unchanged

    def test_getitem_does_not_trigger_cow(self):
        """Test if indexing (read operation) does NOT trigger Copy-on-Write."""
        char = self.cow_string[1]
        self.assertEqual(char, "e")
        self.assertIs(self.cow_string.data, self.original_string)  # No copy should occur

    def test_slicing_does_not_trigger_cow(self):
        """Test if slicing (read operation) does NOT trigger Copy-on-Write."""
        sliced = self.cow_string[:3]
        self.assertEqual(sliced, "hel")
        self.assertIs(self.cow_string.data, self.original_string)  # No copy should occur

    def test_len_functionality(self):
        """Test if len() returns correct value."""
        self.assertEqual(len(self.cow_string), 5)

    def test_iteration(self):
        """Test if iteration over string works correctly."""
        self.assertEqual("".join([char for char in self.cow_string]), "hello")

    def test_contains(self):
        """Test if the contains (`in`) operator works correctly."""
        self.assertTrue("ell" in self.cow_string)
        self.assertFalse("xyz" in self.cow_string)

    def test_upper_does_not_modify_original(self):
        """Test if upper() creates a new string and does not modify the original."""
        upper_string = self.cow_string.upper()
        self.assertEqual(upper_string, "HELLO")
        self.assertEqual(self.cow_string, "hello")  # Original string remains unchanged

    def test_replace_does_not_modify_original(self):
        """Test if replace() creates a new string and does not modify the original."""
        replaced = self.cow_string.replace("h", "H")
        self.assertEqual(replaced, "Hello")
        self.assertEqual(self.cow_string, "hello")  # Original remains unchanged

    def test_assignment_not_allowed(self):
        """Test that modifying a string using index assignment raises an error."""
        with self.assertRaises(TypeError):
            self.cow_string[0] = "H"  # Strings are immutable in Python

    def test_modification_creates_new_string(self):
        """Test if modifying the string results in a new object (CoW behavior)."""
        new_cow_string = cow(self.cow_string + " world")
        self.assertEqual(new_cow_string, "hello world")
        self.assertEqual(self.cow_string, "hello")  # Ensure original is unchanged

if __name__ == "__main__":
    unittest.main()
