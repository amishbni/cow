import unittest
from copyonwrite import cow

class TestCoWDict(unittest.TestCase):
    def setUp(self):
        """Initialize a shared dictionary for testing."""
        self.original_dict = {"a": 1, "b": 2, "c": 3}
        self.cow_dict = cow(self.original_dict)

    def test_initialization(self):
        """Test if the CoW dictionary initializes correctly."""
        self.assertEqual(self.cow_dict, {"a": 1, "b": 2, "c": 3})
        self.assertEqual(self.original_dict, {"a": 1, "b": 2, "c": 3})  # Ensure original is unchanged

    def test_setitem_triggers_cow(self):
        """Test if setting a key triggers Copy-on-Write."""
        self.cow_dict["a"] = 42
        self.assertEqual(self.cow_dict, {"a": 42, "b": 2, "c": 3})
        self.assertEqual(self.original_dict, {"a": 1, "b": 2, "c": 3})  # Ensure original is unchanged

    def test_getitem_does_not_trigger_cow(self):
        """Test if getting a value does NOT trigger Copy-on-Write."""
        value = self.cow_dict["b"]
        self.assertEqual(value, 2)
        self.assertEqual(self.cow_dict, {"a": 1, "b": 2, "c": 3})
        self.assertIs(self.cow_dict.data, self.original_dict)  # No copy should occur

    def test_delitem_triggers_cow(self):
        """Test if deleting a key triggers Copy-on-Write."""
        del self.cow_dict["b"]
        self.assertEqual(self.cow_dict, {"a": 1, "c": 3})
        self.assertEqual(self.original_dict, {"a": 1, "b": 2, "c": 3})  # Ensure original is unchanged

    def test_len_functionality(self):
        """Test if len() returns correct values."""
        self.assertEqual(len(self.cow_dict), 3)
        self.cow_dict["d"] = 4
        self.assertEqual(len(self.cow_dict), 4)

    def test_iteration(self):
        """Test if iteration works correctly."""
        self.assertEqual([key for key in self.cow_dict], ["a", "b", "c"])

    def test_contains(self):
        """Test if the contains (`in`) operator works correctly."""
        self.assertTrue("b" in self.cow_dict)
        self.assertFalse("z" in self.cow_dict)

    def test_clear_triggers_cow(self):
        """Test if clearing the dictionary triggers Copy-on-Write."""
        self.cow_dict.clear()
        self.assertEqual(self.cow_dict, {})
        self.assertEqual(self.original_dict, {"a": 1, "b": 2, "c": 3})  # Ensure original is unchanged

    def test_update_triggers_cow(self):
        """Test if update triggers Copy-on-Write."""
        self.cow_dict.update({"d": 4, "e": 5})
        self.assertEqual(self.cow_dict, {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
        self.assertEqual(self.original_dict, {"a": 1, "b": 2, "c": 3})  # Ensure original is unchanged

    def test_pop_triggers_cow(self):
        """Test if pop triggers Copy-on-Write."""
        value = self.cow_dict.pop("b")
        self.assertEqual(value, 2)
        self.assertEqual(self.cow_dict, {"a": 1, "c": 3})
        self.assertEqual(self.original_dict, {"a": 1, "b": 2, "c": 3})  # Ensure original is unchanged

    def test_popitem_triggers_cow(self):
        """Test if popitem triggers Copy-on-Write."""
        key, value = self.cow_dict.popitem()
        self.assertNotIn(key, self.cow_dict)
        self.assertEqual(self.original_dict, {"a": 1, "b": 2, "c": 3})  # Ensure original is unchanged

if __name__ == "__main__":
    unittest.main()
