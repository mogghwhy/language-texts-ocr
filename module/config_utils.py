from pathlib import Path
import logging

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)

def find_region_cfg(root_dir, region_config_name):
    return find_files(root_dir, region_config_name)

def find_snapshot_files(root_dir, snapshot_file_extension=".jpg"):
    return find_files(root_dir, f"*{snapshot_file_extension}", search_recursive=False)

def find_files(root_dir, file_name, search_recursive=True):
    root = Path(root_dir).resolve()
    if search_recursive:
        return [p.resolve() for p in root.rglob(file_name)]
    else:
        return [p.resolve() for p in root.glob(file_name)]
    
def get_abs_parent_folder(abs_path):
    root = Path(abs_path)
    return root.parent.absolute()

def get_configs_and_snapshots(root_dir, config_file_name, snapshot_file_extension=".jpg"):
    configs = find_region_cfg(root_dir, config_file_name)
    result = []
    for config in configs:
        config_root_dir = get_abs_parent_folder(config)
        snapshots = find_snapshot_files(config_root_dir, snapshot_file_extension)
        count = len(snapshots)
        logger.info(f"Found {count} snapshot files in {config_root_dir} for config {config}")
        if count:
            dictionary = {
                "config": config,
                "snapshots": snapshots,
                "snapshot_base_dir": config_root_dir
            }
            result.append(dictionary)
    return result