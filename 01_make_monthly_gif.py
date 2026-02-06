
import ee, geemap, os
from utils import load_config, ensure_dir

ee.Initialize()
cfg = load_config()
roi = ee.FeatureCollection(cfg["roi_asset"])

rainfall = ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY").select("precipitation")

def make_month(ym):
    s = ee.Date(ym + "-01")
    e = s.advance(1, "month")
    return rainfall.filterDate(s, e).sum().clip(roi).rename("Rain_mm").set({
        "system:time_start": s.millis(),
        "label": ym
    })

monthly = ee.ImageCollection.fromImages([make_month(m) for m in cfg["months"]])

vis = cfg["viz"]
monthly_vis = monthly.map(lambda i: ee.Image(i).visualize(**vis))

ensure_dir(cfg["export"]["out_dir"])
out = os.path.join(cfg["export"]["out_dir"], cfg["export"]["out_gif"])

geemap.download_ee_video(monthly_vis, {
    "region": roi.geometry(),
    "dimensions": cfg["export"]["dimensions"],
    "framesPerSecond": cfg["export"]["fps"],
    "crs": cfg["export"]["crs"]
}, out)

print("Saved:", out)
