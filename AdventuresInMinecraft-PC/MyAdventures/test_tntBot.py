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
        assert self.bot.mc.setBlock.called
        assert self.bot.mc.setBlock.call_args[0] == (1, 2, 3, block.TNT.id)

    def test_detonate_tnt(self):
        # Prueba la detonación de TNT
        self.bot.detonate_tnt(4, 5, 6)
        assert self.bot.mc.setBlock.called
        assert self.bot.mc.setBlock.call_args[0] == (4, 5, 6, block.FIRE.id)

    @patch("time.sleep", return_value=None)  # Mock sleep para acelerar las pruebas
    def test_deploy_and_detonate_tnt(self, mock_sleep):
        # Mock de las llamadas a funciones
        self.bot.apply_to_coordinates = MagicMock()
        
        self.bot.deploy_and_detonate_tnt(7, 8, 9)
        
        assert self.bot.apply_to_coordinates.call_count == 2
        assert mock_sleep.called
        assert mock_sleep.call_args[0] == (5,)
        assert self.bot.apply_to_coordinates.call_args_list[0][0] == (self.bot.place_tnt, 7, 8, 9)
        assert self.bot.apply_to_coordinates.call_args_list[1][0] == (self.bot.detonate_tnt, 7, 8, 9)

if __name__ == "__main__":
    unittest.main()
