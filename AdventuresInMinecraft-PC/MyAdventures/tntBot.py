from agentFramework import BaseAgent
import mcpi.block as block
import time

class TNTBot(BaseAgent):
    def perform_action(self):
        # Obtiene la posición actual del jugador
        pos = self.get_position()
        # Despliega y detona TNT en las coordenadas especificadas
        self.deploy_and_detonate_tnt(pos.x + 1, pos.y, pos.z)

    def deploy_and_detonate_tnt(self, x, y, z):
        # Aplica la función place_tnt a las coordenadas
        self.apply_to_coordinates(self.place_tnt, x, y, z)
        time.sleep(5)  # Espera 5 segundos antes de detonar
        # Aplica la función detonate_tnt a las coordenadas
        self.apply_to_coordinates(self.detonate_tnt, x, y, z)

    def place_tnt(self, x, y, z):
        # Coloca un bloque de TNT en las coordenadas especificadas
        self.place_block(x, y, z, block.TNT.id)

    def detonate_tnt(self, x, y, z):
        # Coloca un bloque de fuego en las coordenadas especificadas para detonar el TNT
        self.place_block(x, y, z, block.FIRE.id)

    def apply_to_coordinates(self, func, x, y, z):
        # Aplica la función dada a las coordenadas especificadas
        func(x, y, z)