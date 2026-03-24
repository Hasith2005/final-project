import os
import argparse

# DIR = "/home/hasi/projects/Feynman_with_units/Feynman_with_units"
def remove_spaces(dir):
    if not os.path.isdir(dir):
        print(f"Error: The directory '{dir}' does not exist.")
        return
    print(f"scanning {dir}")
    
    for file in os.listdir(dir):
        fname = os.fsdecode(file)
        fpath=os.path.join(dir,fname)
        print(f"editing {fname}")
        with open(fpath,"r") as f:
            lines=f.readlines()
        with open(fpath,"w") as f:
            for line in lines:
                f.write(line.rstrip() + "\n")
        print(f"modified file {fname}")
    

if __name__=='__main__':
    parser = argparse.ArgumentParser(
        description="strip trailing spaces/tabs from all lines in a dataset's files."
    )
    parser.add_argument(
        "directory", 
        type=str, 
        help="Path to the target directory containing the files"
    )
    args = parser.parse_args()
    remove_spaces(args.directory)

