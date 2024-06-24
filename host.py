try:
        from flask import Flask, render_template, request, jsonify
        import subprocess
        import os
        import time
        import cv2
        import base64
        from tkinter.filedialog import askopenfilename
        import tkinter as tk
        import requests
        from ultralytics import YOLO
        import base64
        import pyuac
        import webbrowser
        import threading
        from threading import Timer

        if not pyuac.isUserAdmin():
            Timer(1,pyuac.runAsAdmin()).start()
            exit(0)
except ModuleNotFoundError:
    import os
    print("Installing necessary modules....")
    os.system("pip install flask")
    os.system("pip install ultralytics")
    os.system("pip install opencv-python")
    os.system("pip install pyuac")
    os.system("pip install requests")
    print("Modules installed!")
    
    time.sleep(1.5)

app = Flask(__name__)
mode = 'image'
model = YOLO("best.onnx", task="detect")

def open_browser():
    webbrowser.open_new("http://127.0.0.1:2010")

def http_server():
    os.system("cd %userprofile% & python -m http.server")
def get_recipes_by_ingredients(ingredients, number = "9", api_key = "804caf8927fb46e88c6334ef4c298e98", rank = "1"):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number={number}&apiKey={api_key}&ranking={rank}"
    response = requests.get(url)
    data = response.json()
    return data

def get_nutrion_by_id(id, api_key):
    url = f"https://api.spoonacular.com/recipes/{id}/nutritionWidget.json?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def get_recipes_information(ids, api_key):
    url = f"https://api.spoonacular.com/recipes/informationBulk?ids={ids}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def get_ingredients(imagedata):
    if len(imagedata) % 4 != 0:
        imagedata += '=' * (4 - len(imagedata) % 4)
    img = base64.b64decode(imagedata)
    filename = 'image.jpg'
    with open(filename, 'wb') as f:
        f.write(img)
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
                ingredients += names[j] + ",+"
    return ingredients
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/takeselectphoto', methods=['POST'])
def process_photo():
    if mode == "image":
        root = tk.Tk()
        root.attributes("-topmost", True)
        filename = askopenfilename()
        parts = filename.split('/')
        result = '/'.join(parts[3:])
        print(result)
        root.destroy()
        return jsonify({'success': True, 'file_location': result})
    elif mode == "webcam":
        return jsonify({'success': True, 'file_location': "webcam"})
@app.route('/modeselect', methods=['POST'])
def process_mode():
    global mode
    mode = request.json.get('mode')
    print(mode)
    return jsonify({'success': True})

@app.route('/incredients', methods=['POST'])
def getincredients():
    mode = request.json.get('mode')
    base64_image = request.json.get('image')
    if mode == "webcam":
        encoded_image = base64_image
        if base64_image.startswith("data:image/png;base64,"):
            encoded_image = base64_image[len("data:image/png;base64,"):]
        file_path = "example.txt"
        with open(file_path, 'w') as file:
            file.write(encoded_image)

        ingredients = get_ingredients(encoded_image)
        print(ingredients)

        return jsonify({'success': True, 'data': ingredients})
    elif mode == "image":
        user = os.path.expandvars('%userprofile%')
        with open(user + '\\' + base64_image, 'rb') as file:
            image_data = file.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')
        ingredients = get_ingredients(encoded_image)
        return jsonify({'success': True, 'data': ingredients})

@app.route('/recipes', methods=['POST'])
def getricipes():
    ingredients = request.json.get('ingredients')
    data = get_recipes_by_ingredients(ingredients, 9, "804caf8927fb46e88c6334ef4c298e98", 1)

    #print(data)
    ids = ""
    srcs = []
    links = []
    for id in data:
        ids += str(id["id"]) + ","
    information = get_recipes_information(ids, "804caf8927fb46e88c6334ef4c298e98")
    for src in data:
        srcs.append(src["image"])

    for link in information:
        links.append(link["sourceUrl"])

    #print (srcs)
    #print(information)
    return jsonify({'success': True, 'srcs': srcs, 'links': links})

if __name__ == '__main__':
    Timer(3, open_browser).start()
    Timer(3, http_server).start()
    app.run(host="127.0.0.1", port=2010, debug=False)
