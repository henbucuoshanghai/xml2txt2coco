import cv2
import numpy as np

a=cv2.imread("0079.jpg",0)
_,contours, hierarchy = cv2.findContours(a,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print (len(contours))
#cnt = contours[0]
#bounding_boxes = [cv2.boundingRect(cnt) for cnt in contours]

height, width = a.shape
img = np.zeros([height, width, 3], dtype=np.uint8)
for cnt in contours:
    #bounding_boxes = cv2.boundingRect(cnt)
    x, y, w, h = cv2.boundingRect(cnt)
    print (x, y, w, h)
    cv2.drawContours(a, cnt, -1, (255,255,255), thickness=-1)
    cv2.rectangle(a, (x, y), (x + w, y + h), (255,0, 0), 2)
#cv2.imshow ("img.png", img)
#cv2.waitKey(0)
cv2.imwrite("img.jpg",a)


'''
for i in range(len(data['shapes'])):  # 遍历每一个shape   #读取一个图片的所有边界
    m_name = data['shapes'][i]['label']    #对于一个边界
    m_xmin, m_ymin = m_width, m_height
    m_xmax, m_ymax = 0, 0
    for j in range(0, len(data['shapes'][i]['points'])):  #对于一个边界,遍历所有点，比大小
        m_xmin = min(m_xmin, int(data['shapes'][i]['points'][j][0]))   #得到边界bbox
        m_xmax = max(m_xmax, int(data['shapes'][i]['points'][j][0]))
        m_ymin = min(m_ymin, int(data['shapes'][i]['points'][j][1]))
        m_ymax = max(m_ymax, int(data['shapes'][i]['points'][j][1]))
'''
