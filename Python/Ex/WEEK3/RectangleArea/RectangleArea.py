'''RectangleArea'''
def main():
    '''main'''
    rec1 = input().split(" ")
    rec2 = input().split(" ")
    x1 = int(rec1[0])
    y1 = int(rec1[1])
    w1 = int(rec1[2])
    h1 = int(rec1[3])
    x2 = int(rec2[0])
    y2 = int(rec2[1])
    w2 = int(rec2[2])
    h2 = int(rec2[3])
    rect1 = (x1, y1, x1 + w1, y1 + h1) # x,y แรกกับหลัง
    rect2 = (x2, y2, x2 + w2, y2 + h2) # x,y แรกกับหลัง
    overlap_w = min(rect1[2], rect2[2]) - max(rect1[0], rect2[0]) # หา x ว่า overlap มั้ย
    overlap_h = min(rect1[3], rect2[3]) - max(rect1[1], rect2[1]) # หา y ว่า overlap มั้ย
    if overlap_w <= 0 or overlap_h <= 0:
        print("no overlapping")
    else:
        print(overlap_w * overlap_h)
main()
