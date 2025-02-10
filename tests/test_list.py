import unittest
from copyonwrite import cow

class TestCoWList(unittest.TestCase):
    def setUp(self):
        """Initialize a shared list for testing."""
        self.original_list = [1, 2, 3, 4]
        self.cow_list = cow(self.original_list)

    def test_initialization(self):
        """Test if the CoW list initializes correctly."""
        self.assertEqual(self.cow_list, [1, 2, 3, 4])
        self.assertEqual(self.original_list, [1, 2, 3, 4])  # Ensure original is unchanged

    def test_append_triggers_cow(self):
        """Test if append triggers Copy-on-Write."""
        self.cow_list.append(5)
        self.assertEqual(self.cow_list, [1, 2, 3, 4, 5])
        self.assertEqual(self.original_list, [1, 2, 3, 4])  # Ensure original is unchanged

    def test_extend_triggers_cow(self):
        """Test if extend triggers Copy-on-Write."""
        self.cow_list.extend([5, 6])
        self.assertEqual(self.cow_list, [1, 2, 3, 4, 5, 6])
        self.assertEqual(self.original_list, [1, 2, 3, 4])  # Ensure original is unchanged

    def test_pop_triggers_cow(self):
        """Test if pop triggers Copy-on-Write."""
        popped_item = self.cow_list.pop()
        self.assertEqual(popped_item, 4)
        self.assertEqual(self.cow_list, [1, 2, 3])
        self.assertEqual(self.original_list, [1, 2, 3, 4])

    def test_getitem_does_not_trigger_cow(self):
        """Test if getting an item does NOT trigger Copy-on-Write."""
        value = self.cow_list[2]
        self.assertEqual(value, 3)
        self.assertEqual(self.cow_list, [1, 2, 3, 4])
        self.assertIs(self.cow_list.data, self.original_list)  # No copy should occur

    def test_setitem_triggers_cow(self):
        """Test if modifying an index triggers Copy-on-Write."""
        self.cow_list[1] = 99
        self.assertEqual(self.cow_list, [1, 99, 3, 4])
        self.assertEqual(self.original_list, [1, 2, 3, 4])  # Ensure original is unchanged

    def test_deep_copy_on_modification(self):
        """Ensure that CoW creates a deep copy upon modification."""
        self.cow_list.append([10, 20])  # Add a nested list
        self.cow_list[-1].append(30)  # Modify the nested list
        self.assertEqual(self.cow_list, [1, 2, 3, 4, [10, 20, 30]])
        self.assertEqual(self.original_list, [1, 2, 3, 4])  # Ensure original is unchanged

    def test_len_functionality(self):
        """Test if len() returns correct values."""
        self.assertEqual(len(self.cow_list), 4)
        self.cow_list.append(5)
        self.assertEqual(len(self.cow_list), 5)

    def test_iteration(self):
        """Test if iteration works correctly."""
        self.assertEqual([x for x in self.cow_list], [1, 2, 3, 4])

    def test_contains(self):
        """Test if the contains (`in`) operator works correctly."""
        self.assertTrue(3 in self.cow_list)
        self.assertFalse(99 in self.cow_list)

if __name__ == "__main__":
    unittest.main()
