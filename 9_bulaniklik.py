import cv2
import matplotlib.pyplot as plt

#  blurring and smooting - bulanıklaştırma ve düzgünleşstime
img = cv2.imread("images/maviTren.jpg")
cv2.imshow("Orijinal", img)


def p(blurred, title):
    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(12 ,17))

    for i in range(len(axes)):
        for j in range(len(axes[i])):
            axes[i][j].axis("off")
            axes[i][j].imshow(cv2.cvtColor(blurred[i][j], cv2.COLOR_BGR2RGB), aspect="auto")

            if j==1:
                axes[i][j].set_title(title[i])

    plt.tight_layout()


def plotBlurring(img, title):
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(6, 2))
    fig.suptitle(title)
    for i in range(len(axes)):
        axes[i].axis("off")
        axes[i].imshow(cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB), aspect="auto")

    plt.tight_layout()

#  ortalama
blurred1 = [
    cv2.blur(img, (3, 3)),
    cv2.blur(img, (5, 5)),
    cv2.blur(img, (27,27))
]
#plotBlurring(blurred1, "Averaged")

#  Gaussian
blurred2 = [
    cv2.GaussianBlur(img, (3, 3), 0),
    cv2.GaussianBlur(img, (5, 5), 0),
    cv2.GaussianBlur(img, (7,7), 0)
]
#plotBlurring(blurred2, "Gaussian")

#  Median
blurred3 = [
    cv2.medianBlur(img, 3),
    cv2.medianBlur(img, 5),
    cv2.medianBlur(img, 7)
]
#plotBlurring(blurred3, "Median")

#  Bilateral
blurred4 = [
    cv2.bilateralFilter(img, 5, 21, 21),
    cv2.bilateralFilter(img, 7, 31, 31),
    cv2.bilateralFilter(img, 9, 41, 41)
]
#plotBlurring(blurred4, "Bilateral")

blurred = [blurred1, blurred2, blurred3, blurred4]
title = ["Averaged", "Gaussian", "Median", "Bilateral"]

p(blurred, title)

plt.show()
cv2.waitKey(0)
