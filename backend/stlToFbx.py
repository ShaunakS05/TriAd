import bpy
import sys

# Using Blender to prepare the 3D model
# Loads STL file and exports as FBX

# Retrieve the file paths from the command line arguments
input_stl_path = sys.argv[-2]
output_fbx_path = sys.argv[-1]

# Clear existing objects in the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Import the STL file
bpy.ops.import_mesh.stl(filepath=input_stl_path)

# Select all objects (the imported STL should be the only object in the scene)
bpy.ops.object.select_all(action='SELECT')

# Export to FBX
bpy.ops.export_scene.fbx(filepath=output_fbx_path, use_selection=True)

print(f"Converted {input_stl_path} to {output_fbx_path}")
