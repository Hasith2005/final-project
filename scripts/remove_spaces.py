import os

DIR = "/home/hasi/projects/Feynman_with_units/Feynman_with_units"
def remove_spaces():
    for file in os.listdir(DIR):
        fname = os.fsdecode(file)
        fpath=os.path.join(DIR,fname)
        print(f"editing {fname}")
        with open(fpath,"r") as f:
            lines=f.readlines()
        with open(fpath,"w") as f:
            for line in lines:
                f.write(line.rstrip() + "\n")
        print(f"modified file {fname}")
    

if __name__=='__main__':
    remove_spaces()

