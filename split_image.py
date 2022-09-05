# Imports

import cv2
from math import floor



# Configs


ext = "default" # override output format here if desired
path_to_img = "example.jpg" # target image (input)
prefix = 'scrsplit' # output filename will begin with this
split_width = 951 # width at which to split
split_height = 1366 # height at which to split
split_options = {"v": "vertical", "h": "horizontal", "b": "both"} #! todo: implement "both"
split_mode = split_options["v"] # Split along x or y axis



# Logic

def get_ext():
    if ext != "default":
        return ext
    if "." not in path_to_img:
        return "jpg"
    return path_to_img.split('.')[-1]


def start_points(sizes, split_sizes):
    size_x, size_y = sizes
    split_x, split_y = split_sizes
    return [[tuple([x*split_x, y*split_y]), tuple([(x+1)*split_x, (y+1)*split_y]), (x if split_mode.startswith("h") else y)] for x in range(floor(size_x/split_x)) for y in range(floor(size_y/split_y))]


def write_splits(points, img):
    ext = get_ext()
    for initial, final, itr in points:
        split = img[initial[1]:final[1], initial[0]:final[0]]
        cv2.imwrite(f"{prefix}_{itr}.{ext}", split)



# Start the show if running directly from command line, otherwise stop.

if __name__ == "__main__":
    img = cv2.imread(path_to_img)
    img_h, img_w, _ = img.shape
    points = start_points([img_w, img_h], [split_width, split_height])
    write_splits(points, img)
    # Todo: verification
    print(f"Done! {len(points)} files created.")

    
    
    
    
    
    
########################
#    DJ Stomp 2022     #
#  No Rights Reserved  #
########################
