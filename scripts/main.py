import sys
from lib.config_utils import find_region_cfg

def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py <path/to/snapshots>")
        sys.exit(1)

    snapshots_root = sys.argv[1]  # first argument after script name
    all_cfgs = find_region_cfg(snapshots_root, "region.cfg")
    for path in all_cfgs:
        print(path)

if __name__ == "__main__":
    main()