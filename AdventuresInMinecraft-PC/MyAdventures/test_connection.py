import mcpi.minecraft as minecraft

def test_connection():
    try:
        mc = minecraft.Minecraft.create("localhost", 4711)
        pos = mc.player.getTilePos()
        print(f"Player position: x={pos.x}, y={pos.y}, z={pos.z}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_connection()