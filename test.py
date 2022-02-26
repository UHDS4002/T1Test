import unittest
import os.path


class TestA1(unittest.TestCase):
    def test_module_exists(self):
        self.assertTrue(os.path.exists('a1.py'))

    def test_core_exists(self):
        import a1
        self.assertTrue(hasattr(a1, 'Core'))
        self.assertIsInstance(a1.Core, type)

    def test_core_has_methods(self):
        from a1 import Core
        self.assertTrue(hasattr(Core, 'add_stu'))
        self.assertTrue(hasattr(Core, 'find_stu'))

    def test_one_stu(self):
        from a1 import Core
        obj = Core()
        self.assertIsNone(obj.add_stu("28", "Esmail", 20))
        self.assertEqual(obj.find_stu("28"), ("Esmail", 20))

    def test_empty_not_found(self):
        from a1 import Core
        obj = Core()
        self.assertIsNone(obj.find_stu("20"))

    def test_multiple_students(self):
        from a1 import Core
        obj = Core()
        for i in range(10):
            obj.add_stu(f'100{i}', f"Stu {i}", i)

        for i in range(10):
            self.assertEqual(obj.find_stu(f'100{i}'), (f'Stu {i}', i))

        self.assertIsNone(obj.find_stu("205"))


if __name__ == '__main__':
    unittest.main()
