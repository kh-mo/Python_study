from PIL import Image
## 이미지 로드
img = Image.open("image.png")
## 이미지 보기
img.show()
## 이미지 저장(상대경로, 절대경로)
img.save("temp.png")
img.save("D:/github/Python_study/temp.png")
## 이미지 자르기
dim = (100,100,400,400) #좌상단,우하단 꼭지점 좌표값
crop_img = img.crop(dim)
crop_img.show()