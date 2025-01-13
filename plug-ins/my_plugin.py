


def initializePlugin(obj):
    print("My custom menu is being loaded!")
    from imp import reload
    import interface
    reload(interface)
    interface.custom_menu()

def uninitializePlugin(obj):
    import maya.cmds as cmds
    menu_name = "my_amazing_menu"
    if cmds.menu(menu_name, exsits=True):
        cmds.deleteUI(menu_name)
    print("# The menu is no more")