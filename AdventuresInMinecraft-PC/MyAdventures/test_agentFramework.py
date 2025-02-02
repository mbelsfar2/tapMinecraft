import unittest
from unittest.mock import patch, MagicMock
from agentFramework import AgentFramework, BaseAgent

class TestBaseAgent(unittest.TestCase):
    @patch("agentFramework.minecraft.Minecraft.create")
    def setUp(self, mock_minecraft):
        # Configura la conexión mock de Minecraft y el agente
        self.mock_mc = MagicMock()
        mock_minecraft.return_value = self.mock_mc
        self.agent = BaseAgent()

    def test_place_block(self):
        # Prueba la colocación de un bloque
        self.agent.place_block(1, 2, 3, 4)
        assert self.mock_mc.setBlock.called
        assert self.mock_mc.setBlock.call_args[0] == (1, 2, 3, 4)

    def test_get_position(self):
        # Prueba la obtención de la posición del jugador
        mock_pos = MagicMock()
        mock_pos.x, mock_pos.y, mock_pos.z = 10, 20, 30
        self.mock_mc.player.getTilePos.return_value = mock_pos
        position = self.agent.get_position()
        assert (position.x, position.y, position.z) == (10, 20, 30)

    def test_move_to(self):
        # Prueba el movimiento del jugador a una nueva posición
        self.agent.move_to(5, 10, 15)
        assert self.mock_mc.player.setTilePos.called
        assert self.mock_mc.player.setTilePos.call_args[0] == (5, 10, 15)

class TestAgentFramework(unittest.TestCase):
    def test_register_agent(self):
        # Prueba el registro de un agente en el framework
        framework = AgentFramework()
        mock_agent = MagicMock()
        framework.register_agent(lambda: mock_agent)
        assert mock_agent in framework.agents

if __name__ == "__main__":
    unittest.main()
