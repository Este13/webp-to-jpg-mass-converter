import os
import subprocess

# Retrieve the path to the folder containing the script
folder_path = os.path.dirname(os.path.abspath(__file__))

# Loop over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.webp'):
        # Build complete path for source and destination file
        source_path = os.path.join(folder_path, filename)
        dest_path = os.path.join(folder_path, os.path.splitext(filename)[0] + '.jpg')

        # Run the FFmpeg command to convert the file
        subprocess.run(['ffmpeg', '-i', source_path, dest_path])

        # Delete source file if correctly converted
        if os.path.exists(dest_path):
            os.remove(source_path)

