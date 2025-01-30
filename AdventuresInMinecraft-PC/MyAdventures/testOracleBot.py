import unittest
from unittest.mock import patch, MagicMock
from oracleBot import OracleBot, get_random_message

class TestOracleBot(unittest.TestCase):
    @patch("oracleBot.BaseAgent.__init__", return_value=None)
    def setUp(self, mock_base_init):
        # Configura el bot y la conexión mock de Minecraft
        self.bot = OracleBot()
        self.bot.mc = MagicMock()

    def test_get_random_message(self):
        # Prueba la función que obtiene un mensaje aleatorio
        messages = ["Yes", "No", "Maybe"]
        self.assertIn(get_random_message(messages), messages)

    def test_perform_action(self):
        # Mock de mensajes de chat entrantes
        mock_message = MagicMock()
        mock_message.message = "oraclebot will I be rich?"
        self.bot.mc.events.pollChatPosts.return_value = [mock_message]
        
        # Ejecuta la acción del bot
        self.bot.perform_action()
        
        # Verifica si se publicó una respuesta en el chat
        self.bot.mc.postToChat.assert_called()

if __name__ == "__main__":
    unittest.main()
