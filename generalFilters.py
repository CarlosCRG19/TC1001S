import numpy as np
import cv2 as cv


class Filters:
    """
        img: Image to apply filter
        size: Vignette size (min: 1)
    """
    @staticmethod
    def addVignette(img, size=1):
        rows, cols = img.shape[:2]
        finalImg = np.copy(img)
        finalImg[:, :, :] = 0
        x = cv.getGaussianKernel(cols, cols / size)
        y = cv.getGaussianKernel(rows, rows / size)
        c = y * x.T
        d = c / c.max()
        finalImg[:, :, 0] = img[:, :, 0] * d
        finalImg[:, :, 1] = img[:, :, 1] * d
        finalImg[:, :, 2] = img[:, :, 2] * d

        return finalImg
