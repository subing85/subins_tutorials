# Maya abc exporter
This is a sciprt to export abc file with custom attribute in vertex scope for selected mesh in maya scene.
The exported abc file by default would save to current workspace directory.

### How to excute?

1. Select mesh in maya scene

2. Excute python command:
```
abc_exporter = MayaAbcExporter()
abc_exporter.export_selected_mesh()
```

### Document
* [about python alembic api](https://sylviechen.blogspot.com/2017/07/about-alembic-python-api.html) 

