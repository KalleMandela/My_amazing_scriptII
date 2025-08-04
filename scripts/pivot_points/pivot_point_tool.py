import os
from maya import cmds

'''
PIVOT POINTS TOOL version 2.0

Karl Holmqvist

Make it's possible to select a objects pivot point and connect to another object.
You call it using my amazing script or use the example bellow.
You can also reset the pivot point to it's original position if you not happy were it currently is.
I also have added a function that allow the user to typ in the coordinates of were they want their objects
pivot point to be.

Example of usage:
from imp import reload;
import pivot_points.pivot_point_tool;
reload(pivot_points.pivot_point_tool)
pivot = pivot_points.pivot_point_tool.PivotPoints()

# UI
pivot.interface()

# Command Line
pivot.update_pivot_position(pos_x=10, pos_y=10, pos_z=10)



'''

class PivotPoints:

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0



    # This function makes it possible that the interface designed in QT designer works
    def interface(self):
        # Here are we connecting QT designer with Pycharm
        #
        if not cmds.window('pivot_point_interface.ui', exists=True):
            root_path = os.path.dirname(os.path.abspath(__file__))
            ui_path = '%s/pivot_point_interface.ui' % (root_path)
            window = cmds.loadUI(f=ui_path)
            cmds.showWindow(window)

            cmds.button("set_pivot_point_button", e=True, c=self.change_pivot_to_other_mesh)
            cmds.button("rest_pivot_point_button", e=True, c=self.reset_pivot)

            cmds.button("update_pivot_position_button", e=True, c=self.update_pivot_position)


    # This function allow us to set the pivot point to other objects
    def change_pivot_to_other_mesh(self, *args):
        # Get the selected objects
        self.selected_objects = cmds.ls(selection=True)

        # This request tells us that if selection isn't equal to 2
        # it will give us an error command and write a string that says
        # Please select exactly two meshes.
        if len(self.selected_objects) != 2:
            cmds.error("Please select exactly two meshes.")
            return

        # Get the pivot point of the second selected object
        # selected_objects[1] means that we are selecting a second object
        # How counting works in programing is that you include 0 when you are counting
        # Which means that the first object is 0 and the second object is 1
        target_pivot = cmds.xform(self.selected_objects[1], query=True, worldSpace=True, rotatePivot=True)

        # Set the pivot point of the first selected object to the target pivot
        # So when you select the first object will set directly at second objects position
        cmds.xform(self.selected_objects[0], worldSpace=True, pivots=target_pivot)

        # This will print a text in the script editor that will tell you that first objects pivot point has
        # been moved to the second objects position
        print(f"Pivot of {self.selected_objects[0]} has been moved to the pivot of {self.selected_objects[1]}.")


    # This function allow us to reset the pivot to its original position
    def reset_pivot(self, *args):
        # Get the selected objects
        # By using the command ls the program will tell us what we have selected
        selected_objects = cmds.ls(selection=True)

        # Iterate through each selected object
        for obj in selected_objects:
            # Get the current pivot position
            current_pivot = cmds.xform(obj, query=True, worldSpace=True, rotatePivot=True)

            # Set the pivot to the current position
            cmds.xform(obj, worldSpace=True, pivots=current_pivot)

            # Freeze transformations to reset the pivot
            cmds.makeIdentity(obj, apply=True, translate=True, rotate=True, scale=True, normal=False)

            # Center the pivot to the object
            # By using centerPivots it center the pivot point on the objects bounding box
            cmds.xform(obj, centerPivots=True)

    # This function allows us to set position of the pivot point by typing in the textfields
    def update_pivot_position(self,pos_x=0, pos_y=0, pos_z=0):
        # Get the selected objects
        # By using the command ls the program will tell us what we have selected
        self.selected_objects = cmds.ls(selection=True)

        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0

        # If we have selected less then one object it will give us an error and print out a string that says
        # "Please select an object."
        # Then we exit the function with return
        if len(self.selected_objects) != 1:
            cmds.error("Please select an object.")
            return
        # This will set up the variable "pivot"
        self.pivot = self.selected_objects[0]
        # The try catch will make sure that what we type numeric values
        # and if type anything that isn't number it will give us a warning.
        # By doing this we avoid getting errors that will crash the function
        try:
            self.pos_x = float(cmds.textField('position_x_line', query=True, text=True))
            self.pos_y = float(cmds.textField('position_y_line', query=True, text=True))
            self.pos_z = float(cmds.textField('position_z_line', query=True, text=True))
        except ValueError:
            cmds.warning("Please ensure all position fields contain valid numeric values.")
            return
        # Here we update the position of the objects pivot point
        # It will give us warning if the value we have written is too much for the function
        try:
            cmds.xform(self.pivot, piv=(self.pos_x, self.pos_y, self.pos_z), ws=True)
            # Here we get a dialog box that tell us that the pivot point position has been updated
            # for the selected object
            cmds.confirmDialog(title='Success', message=f"Pivot updated for: {self.pivot}")
        except Exception as e:
            cmds.warning(f"Failed to update pivot: {e}")




# Run the function
pivot = PivotPoints()
# This make sure that the ui will work
pivot.interface()