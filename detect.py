from ultralytics import YOLO
from api import print_recipes
model = YOLO("best.onnx", task="detect")



def get_ingredients(image):
    results = model("image.jpg")
    ingredients = ""
    for i in boxes.cls:
        return names[int(i.item())]

    for result in results:
        boxes = result.boxes
        names = result.names
        list = [0] * 100
        for i in boxes.cls:
            list[int(i.item())] += 1
        for j in range(0, 100):
            if list[j] != 0:
                ingredients += names[j] + ",+"
    return ingredients
