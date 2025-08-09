from imp import reload
import maya.cmds as cmds


cmds.joint(p=(0,8,-1))
cmds.joint(p=(0,4,0))
cmds.joint('joint1', e=True, zso=True, oj='xyz')
cmds.joint(p=(0,0,0))
cmds.joint('joint2', e=True, zso=True, oj='xyz')

# Will create a handle from Joint-1 to an end-effector at
# the location of Joint-5 with a priority of 2 and a
# weight of 0.5
#
cmds.ikHandle( sj='joint1', ee='joint3', p=2, w=.5 )

# Create a handle called leg from the start joint
# named hip to the end-effector named Ankle.
#
cmds.ikHandle( n='Leg', sj='Hip', ee='Ankle' )