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

    """
        img: Image to apply filter
        r: Read value
        g: Green value
        b: Blue value
    """
    @staticmethod
    def addBgrFilter(img, r, g, b):
        filter = np.full(img.shape, (b, g, r), np.uint8)
        finalImg = cv.add(img, filter)
        finalImg = cv.addWeighted(finalImg, 0.8, filter, 0.2, 0)

        return finalImg

    """
        img: Image to apply filter
        filterAmount: Amount of filter applied to image (0 - 1)
        filterSaturation: 
        gamma: Add gamma to final (0 - 255)
    """
    @staticmethod
    def addEpicFilter(img, filterAmount, filterSaturation, gamma):
        redImg = cv.addWeighted(img, abs(filterSaturation - 1),
                                np.full((img.shape[0], img.shape[1], 3), (255, 0, 0), np.uint8),
                                filterSaturation, 0)
        blueImg = cv.addWeighted(img, abs(filterSaturation - 1),
                                 np.full((img.shape[0], img.shape[1], 3), (0, 0, 255), np.uint8),
                                 filterSaturation, 0)

        finalImg = cv.addWeighted(img, abs(filterAmount - 1) + .2, cv.addWeighted(redImg, 0.5, blueImg, 0.5, .5),
                                  filterAmount,
                                  gamma)

        return finalImg
