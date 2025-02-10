import unittest
from copyonwrite import cow

class TestCoWSet(unittest.TestCase):
    def setUp(self):
        """Initialize a shared set for testing."""
        self.original_set = {1, 2, 3}
        self.cow_set = cow(self.original_set)

    def test_initialization(self):
        """Test if the CoW set initializes correctly."""
        self.assertEqual(self.cow_set, {1, 2, 3})
        self.assertEqual(self.original_set, {1, 2, 3})  # Ensure original is unchanged

    def test_add_triggers_cow(self):
        """Test if adding an element triggers Copy-on-Write."""
        self.cow_set.add(4)
        self.assertEqual(self.cow_set, {1, 2, 3, 4})
        self.assertEqual(self.original_set, {1, 2, 3})  # Ensure original is unchanged

    def test_remove_triggers_cow(self):
        """Test if removing an element triggers Copy-on-Write."""
        self.cow_set.remove(2)
        self.assertEqual(self.cow_set, {1, 3})
        self.assertEqual(self.original_set, {1, 2, 3})  # Ensure original is unchanged

    def test_discard_triggers_cow(self):
        """Test if discard triggers Copy-on-Write (no error for missing elements)."""
        self.cow_set.discard(2)
        self.assertEqual(self.cow_set, {1, 3})
        self.assertEqual(self.original_set, {1, 2, 3})  # Ensure original is unchanged

    def test_pop_triggers_cow(self):
        """Test if popping an element triggers Copy-on-Write."""
        popped_element = self.cow_set.pop()
        self.assertNotIn(popped_element, self.cow_set)
        self.assertEqual(self.original_set, {1, 2, 3})  # Ensure original is unchanged

    def test_union_does_not_trigger_cow(self):
        """Test if union (read-only) does NOT trigger Copy-on-Write."""
        new_set = self.cow_set.union({4, 5})
        self.assertEqual(new_set, {1, 2, 3, 4, 5})
        self.assertEqual(self.cow_set, {1, 2, 3})  # Ensure original remains unchanged
        self.assertIs(self.cow_set.data, self.original_set)  # No copy should occur

    def test_intersection_does_not_trigger_cow(self):
        """Test if intersection (read-only) does NOT trigger Copy-on-Write."""
        new_set = self.cow_set.intersection({2, 3})
        self.assertEqual(new_set, {2, 3})
        self.assertEqual(self.cow_set, {1, 2, 3})  # Ensure original remains unchanged

    def test_len_functionality(self):
        """Test if len() returns correct values."""
        self.assertEqual(len(self.cow_set), 3)
        self.cow_set.add(4)
        self.assertEqual(len(self.cow_set), 4)

    def test_iteration(self):
        """Test if iteration works correctly."""
        self.assertEqual(set(x for x in self.cow_set), {1, 2, 3})

    def test_contains(self):
        """Test if the contains (`in`) operator works correctly."""
        self.assertTrue(2 in self.cow_set)
        self.assertFalse(99 in self.cow_set)

    def test_clear_triggers_cow(self):
        """Test if clearing the set triggers Copy-on-Write."""
        self.cow_set.clear()
        self.assertEqual(self.cow_set, set())
        self.assertEqual(self.original_set, {1, 2, 3})  # Ensure original is unchanged

if __name__ == "__main__":
    unittest.main()
