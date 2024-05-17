# DL2024_Team8_Detection-of-whether-vehicles-turning-at-intersections-are-using-turn-signals-
* 創作目標:辨識車輛有無打方向燈的準確率達85%
* 檔案說明:使用yolov7來辨識車輛。
* 使用方法:在terminal 輸入 python yolov7/train.py --device 0 --batch-size 16 --epochs 50 --data yolov7/data/DL.yaml --img 610 640 --cfg yolov7/cfg/training/yolov7-DL.yaml --name yolov7-DL --hyp data/hyp.scratch.custom.yaml
