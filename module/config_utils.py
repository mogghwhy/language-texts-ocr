from pathlib import Path

def find_region_cfg(root_dir, region_config_name):
    root = Path(root_dir).resolve()
    return [p.resolve() for p in root.rglob(region_config_name)]
