import cv2
import os
import numpy as np
import pandas as pd
from ultralytics import YOLO
from turn_signal import detect_turn_signal
from deep_sort_realtime.deepsort_tracker import DeepSort

def main():
    #video_path = "turning_car.mp4"
    output_dir = "video_frames"
    
    # 提取视频帧
    #extract_frames(video_path, output_dir)
    
    # 加载YOLOv8模型
    model = YOLO('yolov8n.pt')  # 替换为你自己的模型路径
    
    # 初始化DeepSORT跟踪器
    tracker = DeepSort(max_age=30, n_init=3)

    # 检测视频帧中的车辆和方向灯状态
    frame_files = sorted(os.listdir(output_dir))
    detections = []
    frames = []
    track_data = []

    for frame_file in frame_files:
        frame_path = os.path.join(output_dir, frame_file)
        frame = cv2.imread(frame_path)
        frames.append(frame)
        
        # 检测车辆和方向灯状态
        detected_objects = detect_turn_signal(frame, model)
        
        # 将检测结果转换为DeepSORT所需的格式
        bbox_xywh = []
        confidences = []
        class_ids = []
        
        for obj in detected_objects:
            x1, y1, x2, y2 = obj["box"]
            bbox_xywh.append([x1, y1, x2-x1, y2-y1])
            confidences.append(obj["confidence"])
            class_ids.append(obj["class_id"])
        
        # 更新跟踪器
        tracks = tracker.update_tracks(bbox_xywh, confidences, class_ids, frame)
        
        # 保存跟踪结果
        for track in tracks:
            if not track.is_confirmed() or track.time_since_update > 1:
                continue
            track_id = track.track_id
            bbox = track.to_tlbr()
            x1, y1, x2, y2 = map(int, bbox)
            class_id = track.get_det_class()
            direction_indicator = "None"
            if class_id == 0:  # 假设0是"left_indicator"
                direction_indicator = "no light"
            elif class_id == 1:  # 假设1是"right_indicator"
                direction_indicator = "light"
            
            track_data.append({
                "ID": track_id,
                "Direction Indicator": direction_indicator,
                "Turn": "Unknown",  # 后面分析轨迹时会更新
                "Frame": frame_file
            })
    
    # # 分析车辆轨迹
    # trajectory = analyze_trajectory(frames)
    
    # # 更新转弯状态
    # for data in track_data:
    #     frame_idx = int(data["Frame"].replace("frame", "").replace(".jpg", ""))
    #     turn_status = trajectory[frame_idx]
    #     data["Turn"] = "Yes" if turn_status == "turning" else "No"
    
    # 转换数据为DataFrame
    df = pd.DataFrame(track_data)
    
    # 保存DataFrame到Excel文件
    df.to_excel("car_data.xlsx", index=False)

if __name__ == "__main__":
    main()