import maya.cmds as m


def renameFunc(objName, objNodeType):
    listObj = m.ls(selection=True)
    numberPadding = "##"
    listCount = len(listObj)
    for count, object in enumerate(listObj):
        m.rename(object, objName + numberPadding + objNodeType)
        numberPadding.replace("##", str(listCount))


renameFunc("sphere_", "_Cheese")
