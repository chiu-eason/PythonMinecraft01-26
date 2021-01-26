from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlocks(x,y,z-1,38)
    color = random.randrange(0,8)
    mc.setBlock(x,y,z,38,ecolor)
    
    
    




