from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

a=0
while a<20:
    mc.setBlocks(x+30)


