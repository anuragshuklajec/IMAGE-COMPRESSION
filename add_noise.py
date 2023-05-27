import numpy as np
import cv2  # Used only for testing

class AddNoise():
    def __init__(self,path) -> None:
        self.path = path
# path = r"C:\Users\Asus\OneDrive\Desktop\Major\Assets\rose_main.webp"

    def addNoise(self):

        im = cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)  # Read input image (for testing).
        im = cv2.threshold(im, 0, 1, cv2.THRESH_OTSU)[1]  # Convert image to binary (for testing).
        im = im.astype(np.int8)  # Convert to type int8 (8 bits singed)

        sigma = 1
        gauss = np.random.normal(0, sigma, im.shape)  # Create random normal (Gaussian) distribution image with mean=0 and sigma=1.
        binary_gauss = (gauss > 2*sigma).astype(np.int8)  # Convert to binary - assume pixels with value above 2 sigmas are "1".
        binary_gauss[gauss < -2*sigma] = -1 # Set all pixels below 2 sigma to "-1".

        noisey_im = (im + binary_gauss).clip(0, 1)  # Add noise image, and clip the result ot [0, 1].
        noisey_im = noisey_im.astype(np.uint8)  # Convert to type uint8

        cv2.imwrite(r"noisy.jpeg", noisey_im)

        # Show images (for testing).
        cv2.imshow('im', im*255)
        cv2.imshow('binary_gauss', (binary_gauss+1).astype(np.uint8)*127)
        cv2.imshow('noisey_im', noisey_im*255)
        cv2.waitKey()
        cv2.destroyAllWindows()
        return noisey_im






