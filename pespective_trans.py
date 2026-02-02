import cv2
import numpy as np

def perspective_trans(points,img_path):  #(左上, 右上, 右下, 左下)
    img = cv2.imread(img_path)
    img = cv2.resize(img, (640, 480))
    h, w = img.shape[:2]
    # 將縮圖座標還原回原圖真實座標
    pts_display = np.array(points, dtype="float32")


    # 自動排序座標 (左上, 右上, 右下, 左下)

    (tl, tr, br, bl) = pts_display

    # 定義目標座標 (正上方視角)
    left = min(tr[0],tl[0])
    right = max(tr[0],tl[0])
    top = min(tr[1],tl[1])
    bottom = max(br[1],bl[1])

    dst = np.array([
        [left, top],
        [right, top],
        [right, bottom],
        [left, bottom]], dtype="float32")

    M = cv2.getPerspectiveTransform(pts_display, dst)
    result = cv2.warpPerspective(img, M, (w, h))
    return result
