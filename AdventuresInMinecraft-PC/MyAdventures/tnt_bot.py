from base_agent import BaseAgent
import mcpi.block as block
import time

class TNTBot(BaseAgent):
    def place_tnt(self, x, y, z):
        self.place_block(x, y, z, block.TNT.id)

    def detonate_tnt(self, x, y, z):
        self.place_block(x, y, z, block.FIRE.id)

    def deploy_and_detonate_tnt(self, x, y, z):
        self.place_tnt(x, y, z)
        time.sleep(5)  # Wait for 3 seconds before detonation
        self.detonate_tnt(x, y, z)

if __name__ == "__main__":
    bot = TNTBot()
    pos = bot.get_position()
    bot.deploy_and_detonate_tnt(pos.x + 1, pos.y, pos.z)