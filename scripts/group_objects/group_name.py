from maya import cmds


'''
GROUP OBJECTS TOOL

Karl Holmqvist

Group objects tool will make it easier for the user to group objects.
This is done by writtening the name of the group in the textfield and then press the button labled "Name group".
By doing this action the user will create a group with the name that user has inserted in the texfield.

Example of usage:
from imp import reload; 
import group_objects; 
reload(group_objects); 
group_objects.GroupObjects().ui()



# UI
group_objects.ui()

# Command Line

'''



class GroupObjects:
    def __init__(self):
        # When the class is initiated, declare main_window to not exist.
        self.main_window = None

    def ui(self):
        # Spawn the floating window
        self.main_window = cmds.window(title='Group name tool', widthHeight=(300, 100))

        # Create main layout
        main_layout = cmds.columnLayout(adj=True)


        # Object ui elements
        object_row = cmds.rowLayout(adj=True, numberOfColumns=3, p=main_layout)
        cmds.text(label='Name:', p=object_row, w=50, align='left')
        self.object_name = cmds.textField(p=object_row, w=150)

        # Group objects button
        cmds.button(p=main_layout, label='Name group', w=250, c=self.group_and_name_selected)

        cmds.showWindow()
        self.ui_created = True

    def group_and_name_selected(self, *args):
        # Check if any objects are selected
        selected_objects = cmds.ls(selection=True)
        if not selected_objects:
            cmds.warning("No objects selected.")
            return

        # Create a group with the selected objects and assign a name based on the user input
        group_name = cmds.textField(self.object_name, query=True, text=True)
        cmds.group(selected_objects, name=group_name)
        print(f"Group '{group_name}' created with objects: {selected_objects}")

# Create an instance of the GroupObjects class and call the ui() method to create the interface
group_objects_tool = GroupObjects()
group_objects_tool.ui()