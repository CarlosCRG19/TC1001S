import numpy as np
import cv2 as cv


def epicFilter(img, filterAmount, filterSaturation, gamma):
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
