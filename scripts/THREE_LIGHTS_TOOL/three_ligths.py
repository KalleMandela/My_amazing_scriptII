import os
import maya.cmds as cmds


'''
THREE LIGTHS TOOL version 2.0

Karl Holmqvist

This make it possible for the user to spawn three lights 
while being able to control the rotation and distance of the lights
so the user can automatically spawn lights for their mesh
without need to constantly check the rendering menu and selected 
light and then fix the rotation and distance manuel, which can take
a lot of time, but this fixes it.

Example of usage:
from imp import reload;
import THREE_LIGHTS_TOOL.three_ligths;
reload(THREE_LIGHTS_TOOL.three_ligths)
lights = THREE_LIGHTS_TOOL.three_ligths.Lights()

# UI
lights.interface()


'''

class Lights():

    def __init__(self):
        pass

    def interface(self):
        if cmds.window('threeLightsWin', exists=True):
            cmds.deleteUI('threeLightsWin')

        root_path = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(root_path, '3_lights_tool_interface.ui')

        if not os.path.exists(ui_path):
            cmds.warning(f"UI file not found: {ui_path}")
            return

        window = cmds.loadUI(f=ui_path)
        cmds.renameUI(window, 'threeLightsWin')
        cmds.showWindow('threeLightsWin')

        cmds.button('three_lights_button', e=True, c=self.lights)

    def get_float_from_field(self, field_name):
        """Safely get float value from a textField"""
        text = cmds.textField(field_name, q=True, text=True)
        try:
            return float(text)
        except (ValueError, TypeError):
            cmds.warning(f"Invalid input in field: {field_name}")
            raise

    def lights(self, *args):
        try:
            # Light 1 values
            rot_x1 = self.get_float_from_field('light_1_rot_x_line')
            rot_y1 = self.get_float_from_field('light_1_rot_y_line')
            rot_z1 = self.get_float_from_field('light_1_rot_z_line')
            dist_x1 = self.get_float_from_field('light_1_dist_x_line')
            dist_y1 = self.get_float_from_field('light_1_dist_y_line')
            dist_z1 = self.get_float_from_field('light_1_dist_z_line')

            # Light 2 values
            rot_x2 = self.get_float_from_field('light_2_rot_x_line')
            rot_y2 = self.get_float_from_field('light_2_rot_y_line')
            rot_z2 = self.get_float_from_field('light_2_rot_z_line')
            dist_x2 = self.get_float_from_field('light_2_dist_x_line')
            dist_y2 = self.get_float_from_field('light_2_dist_y_line')
            dist_z2 = self.get_float_from_field('light_2_dist_z_line')

            # Light 3 values
            rot_x3 = self.get_float_from_field('light_3_rot_x_line')
            rot_y3 = self.get_float_from_field('light_3_rot_y_line')
            rot_z3 = self.get_float_from_field('light_3_rot_z_line')
            dist_x3 = self.get_float_from_field('light_3_dist_x_line')
            dist_y3 = self.get_float_from_field('light_3_dist_y_line')
            dist_z3 = self.get_float_from_field('light_3_dist_z_line')

            # Bundle light data
            light_data = [
                (rot_x1, rot_y1, rot_z1, dist_x1, dist_y1, dist_z1),
                (rot_x2, rot_y2, rot_z2, dist_x2, dist_y2, dist_z2),
                (rot_x3, rot_y3, rot_z3, dist_x3, dist_y3, dist_z3)
            ]

            # Create lights
            for i, (rot_x, rot_y, rot_z, dist_x, dist_y, dist_z) in enumerate(light_data, start=1):
                light = cmds.spotLight(name=f"light_{i}")
                light_transform = cmds.listRelatives(light, parent=True)[0]
                cmds.setAttr(f"{light_transform}.rotateX", rot_x)
                cmds.setAttr(f"{light_transform}.rotateY", rot_y)
                cmds.setAttr(f"{light_transform}.rotateZ", rot_z)
                cmds.setAttr(f"{light_transform}.translateX", dist_x)
                cmds.setAttr(f"{light_transform}.translateY", dist_y)
                cmds.setAttr(f"{light_transform}.translateZ", dist_z)

        except ValueError:
            cmds.warning('Enter valid numbers in all fields')

