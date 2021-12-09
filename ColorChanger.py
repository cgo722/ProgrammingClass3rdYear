import maya.cmds as cmds

window = cmds.window(title = "Auto Rigger", widthHeight = (200,50))
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='Auto Rig', command=('autoRig') )
cmds.button( label='ChangeColor', command=(lambda colorIndex: colorChangerer(13)) )
cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.showWindow(window)
sl = cmds.ls(sl=1)

def autoRig():
    if bool(sl):
        for s in sl:
            ctrlName = s + "_ctrl"
            ctrl = cmds.circle( nr=(0, 1, 0), r=3,  n=ctrlName)[0]
            cmds.matchTransform(ctrl, s)
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            group = cmds.group(ctrl, n=ctrl + "_auto")
            offset = cmds.group(group, n=ctrl + "_offset")
            cmds.parentConstraint(s, offset, mo=0)
            cmds.delete(cmds.parentConstraint(s, offset))
            cmds.parentConstraint(ctrl, s, mo=0)
    else:
        ctrlName = "_ctrl"
        ctrl = cmds.circle( nr=(0, 1, 0), r=3,  n=ctrlName)[0]

def colorChangerer(colorIndex):
    if colorIndex < 32 and colorIndex > -1:
        if bool(sl):
            for s in sl:
                cmds.listRelatives(s, s = True)
                cmds.setAttr(s + ".overrideEnabled", 1)
                cmds.setAttr(s + ".overrideColor", colorIndex)
        else:
            return "select something buddy"
    else:
        return "try agian buddy"