import torch
from ultralytics import YOLO


# 加载模型
if __name__ == '__main__':
    # 从头开始构建新模型
    #model = YOLO("yolov8n.yaml")
    # 加载预训练模型（建议用于训练）
    model = YOLO("best.pt")
    #model = YOLO("yolov8x.pt")
    # 对图像进行预测
    results = model.track("C:\\Users\\USER\\Desktop\\ultralytics-main\\ultralytics-main\\ultralytics\\cfg\\models\\v8\\data\\train\\20230110_124742_0731_A.mp4", save=True, save_txt=True, project="C:\\Users\\USER\\Desktop\\ultralytics-main\\ultralytics-main\\ultralytics\\cfg\\models\\v8\\data\\image")
    print(results)