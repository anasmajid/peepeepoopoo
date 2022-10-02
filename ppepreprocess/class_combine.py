import argparse
import glob 

parser = argparse.ArgumentParser()
parser.add_argument('--labelinput', help='txt directory', required=True)

args = parser.parse_args()

path = args.labelinput

for files in glob.glob(path +"/*.txt"):
    edited = []
    with open(files, 'r+') as f:
        for line in f:
            cls_id = line.split(' ')
            if cls_id[0] == '0':
                cls_id[0] = '6'
            elif cls_id[0] == '1':
                cls_id[0] = '7
            elif cls_id[0] == '2':
                cls_id[0] = '8
            elif cls_id[0] == '3':
                cls_id[0] = '9
            elif cls_id[0] == '4':
                cls_id[0] = '10
            elif cls_id[0] == '5':
                cls_id[0] = '4'
            edited.append(cls_id)
    with open(files, "r+") as f:
        for m in edited:
            f.write(" ".join([str(x) for x in m]))    

# 0 laptop
# 1 monitor
# 2 mouse
# 3 phone
# 4 keyboard
# 5 plastic

# 0 cardboard
# 1 glass
# 2 metal
# 3 paper
# 4 plastic
# 5 trash 
# 6 laptop
# 7 monitor
# 8 mouse
# 9 phone
# 10 keyboard