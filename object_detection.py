import cv2
import json
import time
from ultralytics import YOLO
import os

model = YOLO('yolov8x.pt')  

video_path = 'street.mp4'  
output_video_path = 'output_video_with_boxes3.mp4' 
output_dir = "cropped_images"  
os.makedirs(output_dir, exist_ok=True)  

cap = cv2.VideoCapture(video_path)
frame_width, frame_height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

frame_count, total_time = 0, 0
detection_output = []  

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: 
        break

    start_time = time.time() 
    results = model.predict(frame) 

    frame_data = []  
    for idx, box in enumerate(results[0].boxes, start=1):
        bbox = list(map(int, box.xyxy[0].cpu().numpy())) 
        label = model.names[int(box.cls.cpu().item())]  
        conf = box.conf.cpu().item()  

        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cropped_img = frame[y1:y2, x1:x2]
        cv2.imwrite(os.path.join(output_dir, f"{label}_{frame_count}_{idx}.jpg"), cropped_img)

        frame_data.append({"object": label, "confidence": round(conf, 2), "bbox": [x1, y1, x2, y2]})

    detection_output.append({"frame": frame_count, "detections": frame_data})  
    total_time += time.time() - start_time 
    frame_count += 1 

    out.write(frame) 

with open("detection_output_video3.json", "w") as json_file:
    json.dump(detection_output, json_file, indent=4)

cap.release()
out.release()

average_fps = frame_count / total_time
print(f"Processed {frame_count} frames in {total_time:.2f} seconds. Average FPS: {average_fps:.2f}")
print(f"Detections saved to 'detection_output_video.json'")
print(f"Video with detections saved to '{output_video_path}'")
