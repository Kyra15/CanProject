# import packages
import cv2
import numpy as np

# load image
pic = cv2.imread('sodacan.jpeg')

# convert to grayscale and gaussian blur
bw_pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
gauss_bw_pic = cv2.GaussianBlur(bw_pic, (15, 15), 0)


cv2.imshow("OG Circle", gauss_bw_pic)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# use the cv function called HoughCircles to detect circles and output those lines
detected_circles = cv2.HoughCircles(gauss_bw_pic, cv2.HOUGH_GRADIENT, 1, 20,
                                    param1=50, param2=100, minRadius=800,
                                    maxRadius=1000)

# make sure at least some circles were detected
if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))

    # get the first parameters from the circle that is detected
    first_circle = detected_circles[0][0]

    # get the parameters for the center coordinates
    # and the radius of the first circle detected
    x, y, r = first_circle[0], first_circle[1], first_circle[2]

    # draw the circle for the circumference of the can
    cv2.circle(pic, (x, y), r, (70, 255, 133), 24)

    # draw the smaller circle for the center of the circle
    cv2.circle(pic, (x, y), 1, (70, 255, 133), 32)

    # display the final image
    cv2.imshow("Final Circle", pic)
    cv2.waitKey(0)


