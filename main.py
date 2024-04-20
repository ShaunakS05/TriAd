import subprocess

SEQUENCE="lego"
PATH_TO_VIDEO = "lego.mp4"
DOWNSAMPLE_RATE = 2
SCENE_TYPE = "object"


command = [
    "bash",
    "projects/neuralangelo/scripts/preprocess.sh",
    SEQUENCE,
    PATH_TO_VIDEO,
    str(DOWNSAMPLE_RATE),
    SCENE_TYPE
]

subprocess.run(command, check=True)

EXPERIMENT = "toy_example"
GROUP = "example_group"
NAME = "example_name"
CONFIG = f"projects/neuralangelo/configs/custom/{EXPERIMENT}.yaml"
GPUS = 1

command = [
    "torchrun",
    f"--nproc_per_node={GPUS}",
    "train.py",
    "--logdir=f'logs/{GROUP}/{NAME}'",
    f"--config={CONFIG}",
    "--show_pbar"
]

result = subprocess.run(command, check=True)

if result.returncode == 0:
    print("Training script executed successfully.")
else:
    print("Training script execution failed.")

CHECKPOINT = f"logs/{GROUP}/{NAME}/xxx.pt"
OUTPUT_MESH = "xxx.ply"
RESOLUTION = 2048
BLOCK_RES = 128

command = [
    "torchrun",
    f"--nproc_per_node={GPUS}",
    "projects/neuralangelo/scripts/extract_mesh.py",
    f"--config={CONFIG}",
    f"--checkpoint={CHECKPOINT}",
    f"--output_file={OUTPUT_MESH}",
    f"--resolution={RESOLUTION}",
    f"--block_res={BLOCK_RES}"
]

result = subprocess.run(command, check=True)

# Check the command's return code to confirm successful execution
if result.returncode == 0:
    print("Mesh extraction script executed successfully.")
else:
    print("Mesh extraction script execution failed.")
