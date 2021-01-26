
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
try:
   answer = int(input('你想放甚麼方塊:'))
   mc.setBlock(x+1,y,z,answer)
except:
    print('只能輸入數字')














