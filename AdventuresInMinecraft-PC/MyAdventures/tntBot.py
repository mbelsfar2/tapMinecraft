from agentFramework import BaseAgent
import mcpi.block as block
import time

class TNTBot(BaseAgent):
    def place_tnt(self, x, y, z):
        self.place_block(x, y, z, block.TNT.id)

    def detonate_tnt(self, x, y, z):
        self.place_block(x, y, z, block.FIRE.id)

    def perform_action(self):
        pos = self.get_position()
        self.deploy_and_detonate_tnt(pos.x + 1, pos.y, pos.z)

    def deploy_and_detonate_tnt(self, x, y, z):
        self.place_tnt(x, y, z)
        time.sleep(5)
        self.detonate_tnt(x, y, z)