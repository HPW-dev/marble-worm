import sys
import os
from pathlib import Path

folder = Path(sys.argv[1])
print(f'folder: {folder}')

n = 0
for file in folder.iterdir():
  if not file.is_file():
    continue  
  output_folder = Path(str(folder) + '-out')
  prev_folder = Path(str(folder) + '-prev')
  output_folder.mkdir(parents=True, exist_ok=True)
  prev_folder.mkdir(parents=True, exist_ok=True)
  os.system(f'ffmpeg -hide_banner -y -i \"{str(file)}\" -vframes 1 -vcodec libwebp -preset drawing -qscale 80 \"{output_folder}\\{n}.webp\"')
  os.system(f'ffmpeg -hide_banner -y -i \"{str(file)}\" -vframes 1 -vcodec libwebp -preset drawing -qscale 25 -lavfi \"scale=-1:160:flags=lanczos\" \"{prev_folder}\\{n}.webp\"')
  n += 1
