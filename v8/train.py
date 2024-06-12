import torch
from ultralytics import YOLO


# 加载模型
if __name__ == '__main__':
    # 从头开始构建新模型
    model = YOLO("yolov8n.yaml")
    # 加载预训练模型（建议用于训练）
    model = YOLO("yolov8n.pt")

    #model = YOLO("data.yaml")
    # 加载预训练模型（建议用于训练）
    #model = YOLO("C:\\Users\\USER\\Desktop\\ultralytics-main\\ultralytics-main\\ultralytics\\cfg\models\\v8\\runs\\detect\\train56\\weights\\best.pt")
    # 使用模型
    ## 训练模型
    model.train(data="data.yaml", epochs=300)
    # 在验证集上评估模型性能
    metrics = model.val()
    # 对图像进行预测
    # results = model.track("C:\\Users\\USER\\Desktop\\ultralytics-main\\ultralytics-main\\ultralytics\\cfg\\models\\v8\\data\\train\\20230110_071722_0916_A.mp4", save=True, save_txt=True, project="C:\\Users\\USER\\Desktop\\ultralytics-main\\ultralytics-main\\ultralytics\\cfg\\models\\v8\\data\\image")
    # 将模型导出为 ONNX 格式
    success = model.export(format="onnx")
