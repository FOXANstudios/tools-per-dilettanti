import arpWireless
import sys


def main():
    arpWireless.run_batch_file(batch_file_path)


if __name__ == "__main__":
    main()

batch_file_path = sys.argv[1]