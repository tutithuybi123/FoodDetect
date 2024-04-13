from ultralytics import YOLO

model = YOLO("best.onnx", task="detect")

results = model("image.jpg")

for result in results:
    boxes = result.boxes
    names = result.names
    for i in boxes.cls:
        print(names[int(i.item())])
