import unittest
from src.Settings import ASSISTANT_SETTINGS
from .wake_triggers import check_for_wake_word


class TestWakeTriggers(unittest.TestCase):
    def test_default_wake_word(self):
        wake_word = ASSISTANT_SETTINGS.get("Wake Word")
        command = 'Assistant, test the default wake word'
        self.assertTrue(check_for_wake_word(wake_word, command))

        command = 'This doesn\'t start with the wake word'
        self.assertFalse(check_for_wake_word(wake_word, command))


if __name__ == '__main__':
    unittest.main()
