from ultralytics import YOLO
from api import print_recipes
model = YOLO("best.onnx", task="detect")

results = model("image.jpg")
ingredients = ""

for result in results:
    boxes = result.boxes
    names = result.names
    list = [0] * 100
    for i in boxes.cls:
        list[int(i.item())] += 1
    for j in range(0, 100):
        if list[j] != 0:
            print(list[j]," ", names[j])
            ingredients += names[j] + ",+"

print_recipes(ingredients[:-2])