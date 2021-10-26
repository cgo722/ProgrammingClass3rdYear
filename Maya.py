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
#Hat model

cmds.polySphere(r=0.1, n='Eye1')
cmds.move(1, 13, 1)
cmds.duplicate('Eye1')
cmds.select('Eye1')
cmds.move(1, 13, -1)
#Eyes

cmds.polyCone(h=1, r=.2)
cmds.move(1.5, 13, 0)
cmds.rotate(90, z=True)
#nose

cmds.polyCylinder(h=10, r=0.2, n='Arm1')
cmds.move(0, 9, 5)
cmds.rotate(90, x=True)
cmds.duplicate('Arm1')
cmds.move(0, 9, -5)
#arms