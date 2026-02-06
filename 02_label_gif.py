
from PIL import Image, ImageDraw, ImageFont
import os
from utils import load_config

cfg = load_config()
in_gif = os.path.join(cfg["export"]["out_dir"], cfg["export"]["out_gif"])
out_gif = os.path.join(cfg["export"]["out_dir"], cfg["labeling"]["out_gif_labeled"])

im = Image.open(in_gif)
font = ImageFont.load_default()

frames = []
for i, label in enumerate(cfg["months"]):
    im.seek(i)
    frame = im.convert("RGBA")
    d = ImageDraw.Draw(frame)
    d.rectangle([10,10,180,40], fill=(0,0,0,160))
    d.text((20,18), label, fill=(255,255,255), font=font)
    frames.append(frame)

frames[0].save(out_gif, save_all=True, append_images=frames[1:], duration=1000, loop=0)
print("Saved:", out_gif)
