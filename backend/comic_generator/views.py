from django.shortcuts import render

# Create your views here.



def hello():
    return "hoge"



def send_image():
    # curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/home/pi/Desktop/image.jpg" 100.64.1.11:5000/send_image
    # 上記コマンドでraspberry piから送信
    # https://stackoverflow.com/questions/47515243/reading-image-file-file-storage-object-using-cv2
    # read methodが必要
    image = request.files["file"].read()
    # https://teratail.com/questions/222843
    img = Image.open(BytesIO(image))
    # flipped_img = ImageOps.flip(img)
    # flipped_img.save("image.jpg")
    img.save("image.jpg")
    return "image received!"
