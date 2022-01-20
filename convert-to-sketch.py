import cv2

img = cv2.imread("./isle.jpg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_img = 255 - grey_img

blurred_img = cv2.GaussianBlur(inverted_img, (3, 3), 0)
inverted_blurred_img = 255 - blurred_img
pencil_sketch = cv2.divide(inverted_img, inverted_blurred_img, scale=256.0)

cv2.imshow("Original Image", img)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)
