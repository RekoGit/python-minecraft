from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos=mc.player.getTilePos()
mc.setBlocks(pos.x,pos.y,pos.z, pos.x+10, pos.y+30, pos.z+2, STAINED_GLASS_PURPLE)
mc.setBlocks(pos.x+15,pos.y,pos.z, pos.x+25, pos.y+30, pos.z+2, STAINED_GLASS_BLUE)
mc.setBlocks(pos.x+30,pos.y,pos.z, pos.x+40, pos.y+30,pos.z+2, STAINED_GLASS_RED)
#上の部分だけシーランタン
mc.setBlocks(pos.x-5,pos.y+31,pos.z-11, pos.x+43, pos.y+34,pos.z+11, SEA_LANTERN)
#木の葉っぱ
mc.setBlocks(pos.x-5,pos.y+35,pos.z-11, pos.x-5, pos.y+38,pos.z-11, DARK_OAK_WOOD)
mc.setBlocks(pos.x-5,pos.y+39,pos.z-11, pos.x-5, pos.y+40,pos.z-11, LEAVES_DARK_OAK_PERMANENT)



#（下のプログラムが囲いプログラム）
mc.setBlocks(pos.x+10,pos.y+35,pos.z-11, pos.x+10, pos.y+36,pos.z-3, STONE)
mc.setBlocks(pos.x+10,pos.y+35,pos.z-11, pos.x+43, pos.y+36,pos.z-11, STONE)
mc.setBlocks(pos.x+43,pos.y+35,pos.z-11, pos.x+43, pos.y+36,pos.z-3, STONE)
mc.setBlocks(pos.x+10,pos.y+35,pos.z-3, pos.x+43, pos.y+36,pos.z-3, STONE)
#水プログラム
mc.setBlocks(pos.x+12,pos.y+35,pos.z-8, pos.x+42 , pos.y+36,pos.z-9, WATER_STATIONARY)
