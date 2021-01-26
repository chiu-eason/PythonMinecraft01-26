from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos
mc.setBlack(x,y,z+1,7)
mc.setBlack(x,y,z-1,7)
mc.setBlack(x-1,y,z,7)
mc.setBlack(x-1,y,z,7)
mc.setBlack(x+1,y,z+1,7)
mc.setBlack(x-1,y,z+1,7)
mc.setBlack(x+1,y,z-1,7)
mc.setBlack(x-1,y,z-1,7)







