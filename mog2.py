import numpy as np
import cv2

cap = cv2.VideoCapture(0)

## Creates a MOG2 background subtractor
subtractor = cv2.createBackgroundSubtractorMOG2(
    history=75,         # Length of the history (def 500)
    varThreshold=10,    # Decide wheather a pixel is well described by the background (def 16)
    detectShadows=True  # Detects shadows and mark them (def True)
    )

## Sets the shadow threshold
# The shadow is detected specifying how many times the pixel is
# darker than its previous value. 1/2=0.5 -> will detect pixels
# # 2x darker as shadows
subtractor.setShadowThreshold(0.5) # (def 0.5)
#print(f"Shadow threshold: : {subtractor.getShadowThreshold()}")

## Sets the shadow value
# The bg subtractor will change the value of pixels detected
# as shadows to the value defined here
subtractor.setShadowValue(127)    # (def 127)
#print(f"Shadow Value: {subtractor.getShadowValue()}")

## Sets the background ratio
# If a pixel is semi-constant for BackgroudRatio*history frames
# it is defined as center of a new component
subtractor.setBackgroundRatio(0.9) # (def 0.9)
#print(f"Background ratio: {subtractor.getBackgroundRatio()}")

## Set the complexity reduction threshold
# Set the number of samples needed to accept that
# the component exists
subtractor.setComplexityReductionThreshold(0.05)   # (def 0.05)
#print(f"Complexity: {subtractor.getComplexityReductionThreshold()}")

## Initial variance of each gaussian component
subtractor.setVarInit(15)    # (def 15)
#print(f"Initial variance: {subtractor.getVarInit()}")

## Max variance of each gaussian component
subtractor.setVarMax(75) # (def 75)
#print(f"Maximum variance: {subtractor.getVarMax()}")

## Min variance of each gaussian component
subtractor.setVarMin(4) # (def 4)
#print(f"Minimum variance: {subtractor.getVarMin()}")

## Variance threshold for the pixel-model match
# Decide if the sample is well described by the background model.
subtractor.setVarThreshold(10)   # (def 10)
#print(f"Threshhold variance: {subtractor.getVarThreshold()}")

## Variance threshold for the pixel-model match used for new
# mixture component generation
# Helps decide if a sample is close to the existing components. If a
# pixel is not close to any component, is considered foreground or added
# as a new component. A smaller value generates more components. A larger
# number may generate a small number  of components but they can grow
# too large.
subtractor.setVarThresholdGen(9)    # (def 9)
#print(f"Threshhold generation variance: {subtractor.getVarThresholdGen()}")

while True:
    ## Wait 0.1 sec
    #time.sleep(0.1)

    ## Read frame from video
    ret, frame = cap.read()

    ## Convert frame to black and white
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    ## Blurs an image with a gaussian filter
    blurred = cv2.GaussianBlur(
        src=frame,                      # Source image
        ksize=(35,35),                  # Kernel size, must be odd positive number (def (1,1))
        sigmaX=0,                       # Kernel deviation in X direction (def 0)
        sigmaY=0,                       # Kernel deviation in Y direction (def 0)
        borderType=cv2.BORDER_DEFAULT  # Pixel extrapolation method (def BORDER_DEFAULT)
        )

    ## Apply background subtractor
    bgmask = subtractor.apply(blurred)

    ## Display the frames
    hstack=np.hstack((frame,bgmask))
    cv2.imshow("Frame",hstack)

    ## Capture user input
    k=cv2.waitKey(30)&0xFF

    ## Stop execution case esc
    if k == 27:
        break

## Release the capture device and
# closes all windows
cap.release()
cv2.destroyAllWindows()
