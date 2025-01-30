import time
import mcpi.minecraft as minecraft

class AgentFramework:
    def __init__(self):
        # Inicializa una lista vacía para guardar los agentes registrados
        self.agents = []

    def register_agent(self, agent_class, *args, **kwargs):
        # Crea una instancia de la clase del agente y la añade a la lista de agentes
        agent = agent_class(*args, **kwargs)
        self.agents.append(agent)

    def run(self):
        # Ejecuta continuamente el método perform_action de cada agente registrado
        while True:
            for agent in self.agents:
                agent.perform_action()
            time.sleep(2)  # Ajusta el intervalo según sea necesario

class BaseAgent:
    def __init__(self, address="localhost", port=4711):
        # Conecta al servidor de Minecraft
        self.mc = minecraft.Minecraft.create(address, port)
        
    def place_block(self, x, y, z, block_type):
        # Coloca un bloque en las coordenadas especificadas
        self.mc.setBlock(x, y, z, block_type)

    def get_position(self):
        # Obtiene la posición actual del jugador
        return self.mc.player.getTilePos()

    def move_to(self, x, y, z):
        # Mueve al jugador a las coordenadas especificadas
        self.mc.player.setTilePos(x, y, z)

    def perform_action(self):
        # Este método debe ser implementado por todas las subclases
        raise NotImplementedError("Este método debe ser implementado por todas las subclases")