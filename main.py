import sys
from module.config_utils import find_region_cfg, get_abs_parent_folder

def main():

    if len(sys.argv) != 3:
        print("Usage: python main.py <path/to/snapshots> <config_file_name>")
        sys.exit(1)

    snapshots_root = sys.argv[1]    # first argument after script name
    config_file_name = sys.argv[2]  # second argument after script name
    all_cfgs = find_region_cfg(snapshots_root, config_file_name)
    for path in all_cfgs:
        print(path)
        print(get_abs_parent_folder(path))

if __name__ == "__main__":
    main()