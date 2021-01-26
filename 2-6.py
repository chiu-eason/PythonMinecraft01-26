from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
     x,y,z = mc.player.getTilePos()
     block1 = mc.getBlock(x,y-1,z)
     block2 = mc.getBlock(x+1,y-1,z)
     block3 = mc.getBlock(x-1,y-1,z)
     block4 = mc.getBlock(x,y-1,z+1)
     block5 = mc.getBlock(x,y-1,z-1)
     if block1 == 8 or block1 == 9 or block2 == or block2 == 9 or block3 == 8 or block3 == 9 or block4 == or block4 ==9 orblock5 == 8 or block5 == 9
            mc.setBlock(x,y-1,z79)
            mc.setBlock(x+1,y-1,z79)
            mc.setBlock(x,y-1,z+179)
            mc.setBlock(x,y-1,z-179)
     
     
     
     
     
     
     
     
     if block == 8  or block == 9





