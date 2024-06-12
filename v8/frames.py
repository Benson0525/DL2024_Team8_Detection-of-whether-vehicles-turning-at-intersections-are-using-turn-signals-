import cv2
import os

def process_videos_in_folder(folder, output_folder, fps=1):
    count = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(('.avi', '.mp4')):
                video_path = os.path.join(root, file)
                cap = cv2.VideoCapture(video_path)

                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    if count % int(cap.get(cv2.CAP_PROP_FPS) // fps) == 0:
                        cv2.imwrite(f"{output_folder}/frames{count}.jpg", frame)
                    count += 1

                cap.release()

# 設置保存圖片的文件夾
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

# 讀取主資料夾
main_folder = r"C:\Users\USER\Desktop\ultralytics-main\ultralytics-main\ultralytics\cfg\models\v8\frames\民族路與民生北路口-20240520T080040Z-001"

# 處理所有資料夾中的視頻文件
process_videos_in_folder(main_folder, output_folder)