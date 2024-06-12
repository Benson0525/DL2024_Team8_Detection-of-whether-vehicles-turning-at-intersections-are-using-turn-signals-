# DL2024_Team8_Detection-of-whether-vehicles-turning-at-intersections-are-using-turn-signals-
* 創作目標:辨識車輛有無打方向燈的準確率達85
* 檔案說明:frames.py : 將影片切成好幾幀
           * data.yaml : 類別分成兩類，分別為no light和light
           * train.py  : 利用YOLO模型訊練
           * best.pt   : 利用YOLO訓練出有無打方向燈的最佳權重
           * turn.ipynb: 用滑鼠點擊來繪製邊界，並將車輛有無轉彎以及有無打方向燈print出來

* 使用方法:把要訓練的資料集放在./data/image/train，驗證集放在./data/image/val，執行train.py。訓練產出來的best.pt放在最外層的路徑，將要測試的影片路徑貼給turn.ipynb執行。
