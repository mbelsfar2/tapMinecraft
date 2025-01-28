import time
import mcpi.minecraft as minecraft

class AgentFramework:
    def __init__(self):
        self.agents = []

    def register_agent(self, agent_class, *args, **kwargs):
        agent = agent_class(*args, **kwargs)
        self.agents.append(agent)

    def run(self):
        while True:
            for agent in self.agents:
                agent.perform_action()
            time.sleep(2)

class BaseAgent:
    def __init__(self, address="localhost", port=4711):
        self.mc = minecraft.Minecraft.create(address, port)
        
    def place_block(self, x, y, z, block_type):
        self.mc.setBlock(x, y, z, block_type)

    def get_position(self):
        return self.mc.player.getTilePos()

    def move_to(self, x, y, z):
        self.mc.player.setTilePos(x, y, z)

    def perform_action(self):
        raise NotImplementedError("Subclasses should implement this method")