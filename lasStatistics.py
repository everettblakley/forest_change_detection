import os
import subprocess

src_dir = r"E:\GIS Data\FoxCreek_LiDAR\FoxCreek_58-25-W5\point_cloud_las"
las_files = [f for f in os.listdir(src_dir) if f.split(".")[1] == "las"]
src_files = [
    os.path.join(src_dir, f) for f in os.listdir(src_dir) 
]

las_tools_bin = r"C:\Program Files\LAStools\bin"
las_info = os.path.join(las_tools_bin, "lasinfo.exe")

def compute_las_info():
  for file in src_files:
      cmd = [
          las_info,
          "-i",
          file,
          "-otxt",
          "-odir",
          src_dir,
          "-cd",
          "-histo",
          "classification",
          "1",
      ]
      subprocess.run(cmd)
      name = file.split("\\")[-1]
      print(f"Done with {name}")

def parse_las_statistics():
  info_files = []

if __name__==__main:
  # compute_las_info()