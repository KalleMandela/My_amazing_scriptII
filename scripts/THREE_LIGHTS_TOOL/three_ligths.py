import os
import maya.cmds as cmds

class Lights():

    def __init__(self):
        pass

    def interface(self):
        if cmds.window('threeLightsWin', exists=True):
            cmds.deleteUI('threeLightsWin')

        root_path = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(root_path, '3_lights_tool_interface.ui')

        window = cmds.loadUI(f=ui_path)
        cmds.renameUI(window, 'threeLightsWin')
        cmds.showWindow('threeLightsWin')

        cmds.button('three_lights_button', e=True, c=self.lights)

    def lights(self, *args):
        try:
            rot_1 = float(cmds.textField('light_1_rot_line', q=True, text=True))
            dist_1 = float(cmds.textField('light_1_dist_line', q=True, text=True))

            rot_2 = float(cmds.textField('light_2_rot_line', q=True, text=True))
            dist_2 = float(cmds.textField('light_2_dist_line', q=True, text=True))

            rot_3 = float(cmds.textField('light_3_rot_line', q=True, text=True))
            dist_3 = float(cmds.textField('light_3_dist_line', q=True, text=True))

            for i, (rot, dist) in enumerate([(rot_1, dist_1), (rot_2, dist_2), (rot_3, dist_3)], start=1):
                light = cmds.spotLight()
                light_transform = cmds.listRelatives(light, parent=True)[0]
                cmds.setAttr(f"{light_transform}.rotateY", rot)
                cmds.setAttr(f"{light_transform}.translateZ", dist)

        except ValueError:
            cmds.warning('Enter valid numbers in all fields')

