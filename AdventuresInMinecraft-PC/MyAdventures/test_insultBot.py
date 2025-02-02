import unittest
from unittest.mock import patch, MagicMock
from insultBot import InsultBot, get_random_message

class TestInsultBot(unittest.TestCase):
    @patch("insultBot.BaseAgent.__init__", return_value=None)
    def setUp(self, mock_base_init):
        # Set up the bot and mock the Minecraft connection
        self.bot = InsultBot()
        self.bot.mc = MagicMock()

    def test_get_random_message(self):
        # Test the function that gets a random message
        messages = ["Hello", "Hi", "Hey"]
        result = get_random_message(messages)
        self.assertIn(result, messages)

    def test_perform_action(self):
        # Test the perform_action method
        self.bot.perform_action()

        # Verify that postToChat was called
        self.bot.mc.postToChat.assert_called_once()

        # Verify that the message sent to chat is from the list
        args, _ = self.bot.mc.postToChat.call_args
        message_sent = args[0]
        expected_messages = [
            "You're doing great!",
            "Keep up the good work!",
            "You're awesome!",
            "Believe in yourself!",
            "Stay positive and happy!",
            "You are amazing just the way you are!",
            "Keep smiling, the world needs your light!"
        ]
        self.assertIn(message_sent, expected_messages)

if __name__ == "__main__":
    unittest.main()