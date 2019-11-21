import bpy
import numpy as np


frame =0

position_vector = np.array([[0, 0, 0]])
rotation_vector = np.array([[0, 0, 0]])

def translate_object( object_name, translation_tensor):
    global frame
    obj = bpy.data.objects[object_name]
    obj.location = tuple(translation_tensor[0][:])
    obj.keyframe_insert(data_path='location')
    bpy.context.scene.frame_set(frame)
    frame+=1

def rotate_object( object_name, rotation_tensor):
    global frame
    obj = bpy.data.objects[object_name]
    obj.rotation_euler.x = rotation_tensor[0][0]
    obj.rotation_euler.y = rotation_tensor[0][1]
    obj.rotation_euler.z = rotation_tensor[0][2]
    obj.keyframe_insert(data_path='rotation_euler')
    bpy.context.scene.frame_set(frame)
    frame+=1

# -- X

def roll(object_name, power): 
    global rotation_vector, position_vector
    
    rotation_vector = rotation_vector + np.array([[power, 0, 0]])
    
    rotate_object(object_name, rotation_vector)
    translate_object(object_name, position_vector)

def surge(object_name, power):
    global rotation_vector, position_vector
    
    position_vector = position_vector + np.array([[power, 0, 0]])

    rotate_object(object_name, rotation_vector)
    translate_object(object_name, position_vector)

# -- Y
def pitch(object_name, power):
    global rotation_vector, position_vector
    
    rotation_vector = rotation_vector + np.array([[0, power, 0]])
    
    rotate_object(object_name, rotation_vector)
    translate_object(object_name, position_vector)

def sway(object_name, power):
    global rotation_vector, position_vector
    
    position_vector = position_vector + np.array([[0,power,0]])
    
    rotate_object(object_name, rotation_vector)
    translate_object(object_name, position_vector)

# -- Z
def yaw(object_name, power):
    global rotation_vector, position_vector
    
    rotation_vector = rotation_vector + np.array([[0, 0, power]])
    
    rotate_object(object_name, rotation_vector)
    translate_object(object_name, position_vector)

def heave(object_name, power):
    global rotation_vector, position_vector
    
    position_vector = position_vector + np.array([[0, 0, power]])

    rotate_object(object_name, rotation_vector)
    translate_object(object_name, position_vector)


if __name__=="__main__":
    #for object_name in bpy.data.objects:
    #    print(object_name)

    # Initial Position


    translate_object("Cube", position_vector)
    rotate_object("Cube", rotation_vector)
    print("SIMULATION TIME...")

    move_stepsize = .1
    rotation_stepsize = .08
    
    print(np.arange(0, 2*np.pi, move_stepsize))


    for mvmnt in np.arange(0, 1+move_stepsize, move_stepsize):
        surge("Cube", move_stepsize)
    for mvmnt in np.arange(0, 1+move_stepsize, move_stepsize):
        heave("Cube", move_stepsize)
    for mvmnt in np.arange(0, 1+move_stepsize, move_stepsize):
        sway("Cube",  move_stepsize)

    print(rotation_vector)
    for mvmnt in np.arange(0, 1+move_stepsize, move_stepsize):
        sway("Cube",  -move_stepsize)
    for mvmnt in np.arange(0, 1+move_stepsize, move_stepsize):
        heave("Cube", -move_stepsize)
    for mvmnt in np.arange(0, 1+move_stepsize, move_stepsize):
        surge("Cube", -move_stepsize)

    # One Roll
    for rot in np.arange(0, (np.pi/4) , rotation_stepsize):
        roll("Cube", rotation_stepsize)
    # One Roll Back
    for rot in np.arange(0, (np.pi/2) , rotation_stepsize):
        roll("Cube", -rotation_stepsize)
    # Roll To Correct
    for rot in np.arange(0, (np.pi/4) , rotation_stepsize):
        roll("Cube", rotation_stepsize)

    h = rotation_stepsize
    for rot in np.arange(0, (2*np.pi), h):
        yaw("Cube", h)
        print(rotation_vector)
    
