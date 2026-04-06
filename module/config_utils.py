from pathlib import Path

def find_region_cfg(root_dir, region_config_name):
    return find_files(root_dir, region_config_name)

def find_files(root_dir, file_name, search_recursive=True):
    root = Path(root_dir).resolve()
    if search_recursive:
        return [p.resolve() for p in root.rglob(file_name)]
    else:
        return [p.resolve() for p in root.glob(file_name)]