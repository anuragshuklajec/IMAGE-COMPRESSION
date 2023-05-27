import cv2
import numpy as np
import json
class ConvertToBinary():
    def __init__(self,path):
        self.path = path
    def showConvertion(self):
        # load the input image
        path = self.path
        img = cv2.imread(path)

        # convert the input image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # apply thresholding to convert grayscale to binary image
        ret, binary = cv2.threshold(gray, 70, 255, 0)

        # save Image
        cv2.imwrite(r"C:\Users\Asus\OneDrive\Desktop\Major\Assets\rose.jpeg", binary)

        # convert BGR to RGB to display using matplotlib
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


        array = binary
        my_list = np.array(array).astype(int).tolist()


        binary_json = json.dumps(my_list)

        # create file
        with open("original.json", "w") as file:
            file.write(binary_json)
            file.close()


        # convert the array into a binary image
        binary_image = np.uint8(array)

        # display the binary image
        cv2.imshow("Original Image", binary_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return binary