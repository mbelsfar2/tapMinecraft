import unittest
from unittest.mock import patch, MagicMock
from tntBot import TNTBot
import mcpi.block as block

class TestTNTBot(unittest.TestCase):
    @patch("tntBot.BaseAgent.__init__", return_value=None)
    def setUp(self, mock_base_init):
        # Configura el bot y la conexión mock de Minecraft
        self.bot = TNTBot()
        self.bot.mc = MagicMock()

    def test_place_tnt(self):
        # Prueba la colocación de TNT
        self.bot.place_tnt(1, 2, 3)
        self.bot.mc.setBlock.assert_called_with(1, 2, 3, block.TNT.id)

    def test_detonate_tnt(self):
        # Prueba la detonación de TNT
        self.bot.detonate_tnt(4, 5, 6)
        self.bot.mc.setBlock.assert_called_with(4, 5, 6, block.FIRE.id)

    @patch("time.sleep", return_value=None)  # Mock sleep para acelerar las pruebas
    def test_deploy_and_detonate_tnt(self, mock_sleep):
        # Mock de las llamadas a funciones
        self.bot.apply_to_coordinates = MagicMock()
        
        self.bot.deploy_and_detonate_tnt(7, 8, 9)
        
        self.bot.apply_to_coordinates.assert_any_call(self.bot.place_tnt, 7, 8, 9)
        mock_sleep.assert_called_with(5)
        self.bot.apply_to_coordinates.assert_any_call(self.bot.detonate_tnt, 7, 8, 9)

if __name__ == "__main__":
    unittest.main()
