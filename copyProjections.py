import os
import shutil

source_file = r"pc_083K04SE06.prj"
source_dir = r"E:\GIS Data\FoxCreek_LiDAR\FoxCreek_58-25-W5\point_cloud_las"

las_files = [
    f
    for f in os.listdir(source_dir)
    if f.endswith(".las") and f.split(".")[0] != source_file.split(".")[0]
]

src = os.path.join(source_dir, source_file)

for file in las_files:
    file_name = file.split(".")[0]
    output_file = file_name + ".prj"
    dest = os.path.join(source_dir, output_file)
    shutil.copyfile(src, dest)
    print(f"Copied {output_file}")
