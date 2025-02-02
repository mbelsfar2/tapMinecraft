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
        assert get_random_message(messages) in messages

    def test_perform_action(self):
        # Mock de mensajes de chat entrantes
        mock_message = MagicMock()
        mock_message.message = "oraclebot will I be rich?"
        self.bot.mc.events.pollChatPosts.return_value = [mock_message]
        
        # Ejecuta la acción del bot
        self.bot.perform_action()
        
        # Verifica si se publicó una respuesta en el chat
        assert self.bot.mc.postToChat.called

    def test_no_action_on_empty_chat(self):
        # Mock de mensajes de chat vacíos
        self.bot.mc.events.pollChatPosts.return_value = []
        
        # Resetea el mock antes de ejecutar la acción del bot
        self.bot.mc.postToChat.reset_mock()
        
        # Ejecuta la acción del bot
        self.bot.perform_action()
        
        # Verifica que no se publicó ninguna respuesta en el chat
        self.bot.mc.postToChat.assert_not_called()

    def test_handle_multiple_messages(self):
        # Mock de múltiples mensajes de chat entrantes
        mock_message1 = MagicMock()
        mock_message1.message = "oraclebot will I be happy?"
        mock_message2 = MagicMock()
        mock_message2.message = "oraclebot will it rain tomorrow?"
        self.bot.mc.events.pollChatPosts.return_value = [mock_message1, mock_message2]
        
        # Ejecuta la acción del bot
        self.bot.perform_action()
        
        # Verifica si se publicaron respuestas en el chat para ambos mensajes
        assert self.bot.mc.postToChat.call_count == 2

if __name__ == "__main__":
    unittest.main()
