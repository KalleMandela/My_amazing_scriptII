import maya.cmds as cmds

#cmds.pointLight(rot=(90,0,10))

window = cmds.window(title='Tool rool')

# Layouts
main_layout = cmds.rowColumnLayout(numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)])
side_row = cmds.rowLayout(adj=True, numberOfColumns=2, parent=main_layout)

# Create a text field
text_field = cmds.textField(parent=side_row)


cmds.showWindow(window)



'''
cmds.spotLight(pos=(0.3,0,0), rot=(0,90,0))

#cmds.spotLight(pos=(-0.2,0,0), rot=(0,-90,0))
'''