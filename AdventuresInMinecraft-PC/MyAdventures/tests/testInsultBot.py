import unittest
from unittest.mock import patch, MagicMock
from insultBot import InsultBot, get_random_message

class TestInsultBot(unittest.TestCase):
    @patch("insultBot.BaseAgent.__init__", return_value=None)
    def setUp(self, mock_base_init):
        # Configura el bot y la conexión mock de Minecraft
        self.bot = InsultBot()
        self.bot.mc = MagicMock()

    def test_get_random_message(self):
        # Prueba la función que obtiene un mensaje aleatorio
        messages = ["Hello", "Hi", "Hey"]
        self.assertIn(get_random_message(messages), messages)

    def test_perform_action(self):
        # Ejecuta la acción del bot y verifica si se publicó un mensaje en el chat
        self.bot.perform_action()
        self.bot.mc.postToChat.assert_called()

if __name__ == "__main__":
    unittest.main()
