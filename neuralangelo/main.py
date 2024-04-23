import subprocess
import os
import time

while True:
    directory = "Downloads"
    file_extension = ".mp4"
    all_files = os.listdir(directory)

    matching_files = [file for file in all_files if file.endswith(file_extension)]
    

    if (len(matching_files) > 0):
        base_name, file_extension = os.path.splitext(matching_files[0])
        
        SEQUENCE=str(matching_files[0])
        PATH_TO_VIDEO = "Downloads/" + str(matching_files[0])
        DOWNSAMPLE_RATE = 5
        SCENE_TYPE = "indoor"


        command = [
            "bash",
            "projects/neuralangelo/scripts/preprocess.sh",
            SEQUENCE,
            PATH_TO_VIDEO,
            str(DOWNSAMPLE_RATE),
            SCENE_TYPE
        ]

        subprocess.run(command, check=True)

        EXPERIMENT = str(matching_files[0])
        GROUP = str(base_name)+"_group"
        NAME = str(base_name)+"_name"
        CONFIG = f"projects/neuralangelo/configs/custom/{EXPERIMENT}.yaml"
        GPUS = 1

        command = [
            "torchrun",
            f"--nproc_per_node={GPUS}",
            "train.py",
            f"--logdir=logs/{GROUP}/{NAME}",
            f"--config={CONFIG}",
            "--show_pbar"
        ]

        result = subprocess.run(command, check=True)

        if result.returncode == 0:
            print("Training script executed successfully.")
        else:
            print("Training script execution failed.")

        """
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
            f"--block_res={BLOCK_RES}",
            "--textured"
        ]

        result = subprocess.run(command, check=True)

        # Check the command's return code to confirm successful execution
        if result.returncode == 0:
            print("Mesh extraction script executed successfully.")
        else:
            print("Mesh extraction script execution failed.")

        """
    else:
        print("No file found")
        time.sleep(15)