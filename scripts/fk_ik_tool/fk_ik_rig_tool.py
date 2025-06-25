import os
import maya.cmds as cmds

"""
FK Rig controls
Kalle Holmqvist

This tool will help make FK controls by typing in the radius
in the textfield by giving it a valid numeric value. It also possible to
reset the position of the selected objects by hitting the reset button.
You can also change color of the FK control to blue, to yellow, to red.
It will make it easier to difference the controllers.

example of usage:

from imp import reload;
import FKControls.fk_rig as riggingset;
reload(riggingset)

rig = riggingset.FKRig()

# UI
rig.interface()


"""


class FKRig():

    def __init__(self):
        pass


    # This function calls forth the interface
    def interface(self):
        if not cmds.window('fk_ik_rig_tool_interface.ui', exists=True):
            root_path = os.path.dirname(os.path.abspath(__file__))
            ui_path = '%s/fk_ik_rig_tool_interface.ui' % (root_path)
            window = cmds.loadUI(f=ui_path)
            cmds.showWindow(window)

            # This connects the window in QT designer
            cmds.window('fk_ik_rig_tool_interface.ui', exists=True)

            # This connects the button called Control_radius_button in QT designer
            cmds.button('control_radius_button',e=True, c=self.set_radius)

            # This connects the button called Reset_button in QT designer
            cmds.button('reset_button', e=True, c=self.reset_obj)

            # This connects the button called red button in QT designer
            # To the function color_red here in Pycharm
            cmds.button('red_button', e=True, c=self.color_red)

            # This connects the button called blue button in QT designer
            # To the function color_blue here in Pycharm
            cmds.button('blue_button', e=True, c=self.color_blue)

            # This connects the button called yellow button in QT designer
            # To the function color_yellow here in Pycharm
            cmds.button('yellow_button', e=True, c=self.color_yellow)

            # This connects the button called green button in QT designer
            # To the function color_green here in Pycharm
            cmds.button('green_button', e=True, c=self.color_green)

            # This connects the button called pink button in QT designer
            # To the function color_pink here in Pycharm
            cmds.button('pink_button', e=True, c=self.color_pink)

            # This connects the button called purple button in QT designer
            # To the function color_purple here in Pycharm
            cmds.button('purple_button', e=True,c=self.color_purple)



    # This function will create a circle if you type in it's
    # radius value
    def set_radius(self, *args):
        try:
            # Creates a textfield called radius that is connected to
            # the edit line in QT designer
            radius = float(cmds.textField("rigging_settings_line", q=True, text=True))
            # Create a circle and get its transform and shape nodes
            circle_transform, circle_shape = cmds.circle(n='circle', nr=(0, 0, 1), c=(0, 0, 0), r=radius)

        # This will give the user a warning if they don't enter a
        # valid value
        except ValueError:
            cmds.warning("Invalid radius value. Please enter a number.")


    # This function will set the selected objects
    # to its original position
    def reset_obj(self, *args):
        controls = cmds.ls(sl=True)
        cmds.select(controls)
        cmds.xform(ro=[0, 0, 0], t=[0, 0, 0])

    # Function color_yellow will change the selected object color to yellow
    def color_yellow(self, *args):
        shp = cmds.ls(sl=True)
        if shp:
            cmds.setAttr(shp[0] + '.overrideEnabled', 1)
            cmds.setAttr(shp[0] + '.overrideColor', 17)

    # Function color_blue will change the selected object's color to blue
    def color_blue(self, *args):
        shp = cmds.ls(sl=True)
        if shp:
            cmds.setAttr(shp[0] + '.overrideEnabled', 1)
            cmds.setAttr(shp[0] + '.overrideColor', 6)

    # Function color_red will change the selected object's color to red
    def color_red(self, *args):
        shp = cmds.ls(sl=True)
        if shp:
            cmds.setAttr(shp[0] + '.overrideEnabled', 1)
            cmds.setAttr(shp[0] + '.overrideColor', 4)

    # Function color_green will change the selected object's color to green
    def color_green(self, *args):
        shp = cmds.ls(sl=True)
        if shp:
            cmds.setAttr(shp[0] + '.overrideEnabled', 1)
            cmds.setAttr(shp[0] + '.overrideColor', 14)

    # Function color_pink will change the selected object's color to pink
    def color_pink(self, *args):
        shp = cmds.ls(sl=True)
        if shp:
            cmds.setAttr(shp[0] + '.overrideEnabled', 1)
            cmds.setAttr(shp[0] + '.overrideColor', 9)

    # Function color_purple will change the selected object's color to purple
    def color_purple(self, *args):
        shp = cmds.ls(sl=True)
        if shp:
            cmds.setAttr(shp[0] + '.overrideEnabled', 1)
            cmds.setAttr(shp[0] + '.overrideColor', 31)



fkradius = FKRig()
fkradius.interface()