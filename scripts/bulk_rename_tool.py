from maya import cmds

'''
BULK RENAME TOOL

Karl Holmqvist

Make selection within your viewport. Use the tool to quickly rename all of them at once!
Use the various options to make your ideal pick.
The window can be spawned at multiple instances.
Tool can be run at both Interface and Command Line.

Example of usage:
from imp import reload;
import bulk_rename;
reload(bulk_rename)
bulk_class = bulk_rename.BulkRename()


# UI
bulk_class.ui()


# Command Line
bulk_class.rename(name='cookies', side='l', suffix=True)

'''




class BulkRename():

    def __init__(self):
        # When the class is initiated, declare main_window to not exist. Used later in rename function.
        self.main_window = None


    def ui(self):

        # Spawn the floating window
        self.main_window = cmds.window(title='Bulk rename tool', widthHeight=(300, 100))

        # Create main layout
        main_layout = cmds.columnLayout(adj=True)

        # Side ui elements
        side_row = cmds.rowLayout(adj=True, numberOfColumns=5, p=main_layout)
        cmds.text(label='Side:',p=side_row, w=50, align='left')
        cmds.radioCollection()
        self.none_radio = cmds.radioButton(p=side_row, label='None', select=True)
        self.left_radio = cmds.radioButton(p=side_row, label='Left side')
        self.right_radio = cmds.radioButton(p=side_row, label='Right side')

        # Suffix ui elements
        suffix_row = cmds.rowLayout(adj=True, numberOfColumns=5, p=main_layout)
        cmds.text(label='Suffix:',p=suffix_row, w=50, align='left')
        self.suffix_node_check = cmds.checkBox(p=suffix_row, label='Suffix node type', align='left', value=True)


        # Object ui elements
        object_row = cmds.rowLayout(adj=True, numberOfColumns=3, p=main_layout)
        cmds.text(label='Name:', p=object_row, w=50, align='left')
        self.object_name = cmds.textField(p=object_row, w=150)

        # Rename bulk button
        cmds.button(p=main_layout, label='Bulk rename', w=250, c=self.rename)


        cmds.showWindow()
        self.ui = True

    def rename(self, name='', side=None, suffix=True):
        # Set side, if ui is open, overwrite new_name variable from the input argument
        new_name = '%s_' %(side)

        window_exists = False
        if self.main_window:
            # Figure out if the Interface window exits or not. This will determine how to use the name data.
            window_exists = cmds.window(self.main_window, q=True, ex=True)
            if window_exists:

                name = cmds.textField(self.object_name, q=True, text=True)
                new_name = ''
                if cmds.radioButton(self.left_radio, q=True, select=True):
                    new_name = 'l_'

                elif cmds.radioButton(self.right_radio, q=True, select=True):
                    new_name = 'r_'



        # Grab new core name
        name = cmds.textField(self.object_name, q=True, text=True)
        new_name = '%s%s' %(new_name, name)

        # Append suffix



        #print(new_name)


        # Find out what our active scene is


        # For each of those in your selection, rename to new_name


        selection = cmds.ls(sl=True)

        for node in selection:
            if window_exists and cmds.checkBox(self.suffix_node_check, q=True, value=True) or suffix:
                shape_name = cmds.listRelatives(node, shapes=True)

                # Finds the nodes shape and try to get it's node type
                # If shape is not found, use node instead
                if shape_name:
                    shape_name = shape_name[0]
                else:
                    shape_name = node
                suffix_name = cmds.nodeType(shape_name)
                name_with_suffix = '%s_%s' % (new_name, suffix_name)
                cmds.rename(node, name_with_suffix)
                print('# Renaming node', node, 'To', name_with_suffix)


            else:
                cmds.rename(node, new_name)
                print('# Renaming node', node, 'To', new_name)
