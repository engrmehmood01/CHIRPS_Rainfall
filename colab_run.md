
```python
!pip install earthengine-api geemap Pillow PyYAML
import ee
ee.Authenticate()
ee.Initialize()

!python scripts/01_make_monthly_gif.py
!python scripts/02_label_gif.py
```
