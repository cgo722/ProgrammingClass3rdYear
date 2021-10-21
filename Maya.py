import maya.cmds as cmds

cmds.polySphere(r=5)
cmds.move(2, y=True)
cmds.polySphere(r=3)
cmds.move(9, y=True)
cmds.polySphere(r=1.5)
cmds.move(13, y=True)
#main body of the snowman

cmds.polyCylinder(h=0.2, r=4)
cmds.move(14, y=True)
cmds.polyCylinder(h=6, r=2)
cmds.move(17, y=True)