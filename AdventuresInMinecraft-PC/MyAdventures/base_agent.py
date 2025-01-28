import mcpi.minecraft as minecraft
import mcpi.block as block

class BaseAgent:
    def __init__(self, address="localhost", port=4711):
        self.mc = minecraft.Minecraft.create(address, port)

    def place_block(self, x, y, z, block_type):
        self.mc.setBlock(x, y, z, block_type)

    def get_position(self):
        return self.mc.player.getTilePos()

    def move_to(self, x, y, z):
        self.mc.player.setTilePos(x, y, z)