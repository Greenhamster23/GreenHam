from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
# set player to 0,0,0
mc.player.setPos(0,0,0)
# CLEAR AN AREA WITH AIR TO BUILD
#256 x 256 x 128 blocks.
air = 0
#mc.setBlocks(start x, start y,start z , end x ,end y, end z,air) # clear some air        
mc.setBlocks(48.5,0.0 ,8.9,-47.6,-5,116.9,98) # clear some air                                               
x, y, z = mc.player.getPos()
mc.setBlocks(0,62,0,35,3)
mc.player.setPos(-10.5,1,69.7)     #Player Postion

mc.setBlocks(-9.4,1, 75.3,-10.5,55,76.7,155)
mc.setBlocks(-12.6,0, 70.4,23.7,0,39.3,155)
mc.setBlocks(22.6,1, 32.4,21.7,55,33.3,155)
mc.setBlocks(23.3,1, 68.7,25,55,67.3,155)        #mc.setBlocks( x, y, z, x, y, z, ID)
mc.setBlocks(19.6,1, 64,-12,55,69,air)
mc.setBlocks(-14.3,1,64.5,-15.5,55,30.3,155)
mc.setBlocks(-13.6,1,65.4,-18.5,55,57.5,155)
mc.setBlocks(-20.5,1,58.6,-14.4,55,65.3,155)
mc.setBlocks(22.5, 56, 58,-13.0,55,65,155)
mc.setBlocks(-14.7, 56, 32.7,18.7,0,25.4,155)
mc.setBlocks(-13.5, 56, 65.6,-22.4,1,58.3,155)
mc.setBlocks(18.3, 0, 23.7,-18.4,56,25.7,155)
mc.setBlocks(-14.5, 0, 52.3,-19.5,56,64.6,155)
mc.setBlocks(-18.4, 0, 16.6,24.5,56,63.3,155)
mc.setBlocks(-14.5, 0, 52.3,-19.5,56,64.6,155)
mc.setBlocks( 20.5 , 55, 55.5, -18.3, 1 , 10.7 ,air)
mc.setBlocks( -20.5 , 55, 44.7, -20.5 , 1 , 8.5 ,155)
mc.setBlocks( -20.6 , 55 , 8.6, 20.6 , 1 , 8.7 ,air)
mc.setBlocks( 20.5 , 55 , 8.5, -20.7 , 1 , 8.5 ,155)
mc.setBlocks( 24.3 , 55 , 8.4, 20.4 , 1 , 1.4 ,155)
mc.setBlocks( -19.7 , 0 , 48.7 , 19.7 , 0 , 2.3 ,89)
mc.setBlocks( -21.7 , 1 , 38.3 , -21.3 , 56 , 51.7 ,155)
mc.setBlocks( -18.7 , 49 , 1.5 , 13.7 , 9 , 1.6 , 20)

mc.setBlocks( -21.4 , 1 , 1.5 , -21.4 , 3 , 20.3 , air)