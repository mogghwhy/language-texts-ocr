import sys
from module.config_utils import get_configs_and_snapshots

def main():

    if len(sys.argv) != 3:
        print("Usage: python main.py <path/to/snapshots> <config_file_name>")
        sys.exit(1)

    snapshots_root = sys.argv[1]    # first argument after script name
    config_file_name = sys.argv[2]  # second argument after script name
    configs_and_snapshots = get_configs_and_snapshots(snapshots_root, config_file_name)
    for item in configs_and_snapshots:
        print(f"Config: {item['config']}")
        print(f"Snapshot base dir: {item['snapshot_base_dir']}")
        print("Snapshots:")
        for snapshot in item['snapshots']:
            print(f"  - {snapshot}")
    # all_cfgs = find_region_cfg(snapshots_root, config_file_name)
    # for path in all_cfgs:
    #     print(path)
    #     print(get_abs_parent_folder(path))

if __name__ == "__main__":
    main()