import sys
import glob
import cv2

model = sys.argv[1]

imgs = []
g = glob.glob(f"./detect/{model}/*.png")
g.sort(key = lambda x: int(x[-10:-4]))
for f in g:
    img = cv2.imread(f)
    imgs.append(img)

height, width, _ = imgs[0].shape
size = (width, height)

out = cv2.VideoWriter(f"./detect/{model}.avi", cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for img in imgs:
    out.write(img)
out.release()
