import maya.cmds as cmds


def custom_menu():
    does_menu_exists = cmds.menu('my_amazing_menu', exists=True)
    if does_menu_exists:
        print('Menu does exists, please go ahead and delete')
        cmds.deleteUI('my_amazing_menu')

    custom_menu = cmds.menu('my_amazing_menu', parent='MayaWindow', label='My amazing scripts', tearOff=True)
    cmds.menuItem(parent=custom_menu, label='Hello world', c='from imp import reload; import hello_world; reload(hello_world); hello_world.menu_tester()')
    cmds.menuItem(parent=custom_menu, label='Group objects tool', c='from imp import reload; import group_objects.group_name; reload(group_objects.group_name); group_objects.group_name.GroupObjects().ui()')
    cmds.menuItem(parent=custom_menu, label='Bulk rename tool', c='from imp import reload; import bulk_rename_tool; reload(bulk_rename_tool); bulk_rename_tool.BulkRename().ui()')

custom_menu()