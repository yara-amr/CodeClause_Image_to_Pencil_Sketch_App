from google.colab.patches import cv2_imshow
import cv2

def convert_to_pencil(photo_name):
  img = cv2.imread(photo_name,1)
  cv2_imshow(img)

  grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  grey_invert = 255 - grey_img

  blurred_img = cv2.GaussianBlur(grey_invert, (21,21),0)
  blurred_invert = 255 - blurred_img

  pencil_sketch = cv2.divide(grey_img, blurred_invert, scale = 256.0)
  cv2_imshow(pencil_sketch)
  
photo = input('enter photo name: ')
convert_to_pencil(photo)
