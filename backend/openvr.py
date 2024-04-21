import bpy

# Clear existing data
bpy.ops.wm.read_homefile(use_empty=True)

# Import the FBX file
fbx_file_path = r"C:\Users\17035\Documents\VRCard\backend\outPutFbx.fbx"
bpy.ops.import_scene.fbx(filepath=fbx_file_path)

# Set up a VR camera rig
bpy.ops.object.camera_add(location=(0, 0, 10), rotation=(0, 0, 0))
camera = bpy.context.active_object
camera.name = "VR_Camera"

# Set up the camera to work with VR
bpy.context.scene.camera = camera

# Additional scene setup (optional)
# Add lighting, background, etc.
