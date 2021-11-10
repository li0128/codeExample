# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import os
#from PIL import Image

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def gray2rgb(img):
    gray = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    gray_three = cv2.merge([gray, gray, gray])
    return gray_three
    #cv2.imshow("img", gray_three)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    for root, dirs, files in os.walk("./", topdown=False):
        for name in files:
            #print(os.path.splitext(name)[0])
            if (os.path.splitext(name)[-1]==".jpg"):
                path_name=os.path.join(root, name)
                rgb=gray2rgb(path_name)
                cv2.imwrite(name,rgb)
                print(path_name)
        for name in dirs:
            if (os.path.splitext(name)[-1]==".jpg"):
                path_name = os.path.join(root, name)
                rgb=gray2rgb(path_name)
                cv2.imwrite(name,rgb)
                print(path_name)

    #gray2rgb("1.jpg")

    cv2.waitKey()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
