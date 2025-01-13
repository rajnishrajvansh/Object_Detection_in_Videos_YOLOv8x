<a href="https://www.linkedin.com/posts/rajnish-singh-5320_objectdetection-yolov8-computervision-activity-7284520180985090049-NkdG?utm_source=share&utm_medium=member_android">
Linked Demo Video</a>    
<h2>Overview</h2>
<p>This repository provides step by step guidance to run this object detection in videos using the YOLOv8x model. YOLO (You Only Look Once) is a state-of-the-art, real-time object detection system. YOLOv8x is one of the latest versions, offering enhanced accuracy and speed.</p>

<h2>Features</h2>
<ul>
    <li>Real-time object detection in videos</li>
    <li>High accuracy with YOLOv8x</li>
    <li>Cropping and saving detected objects as images</li>
    <li>JSON output of detection details</li>
</ul>

<h3>Prerequisites</h3>
<ul>
    <li>Python 3.7 or higher</li>
    <li>pip (Python package manager)</li>
</ul>

<h3>Dependencies</h3>
<p>Install the required Python packages using the following command:</p>
<pre><code>pip install torch torchvision numpy opencv-python json5 </code>
<code>pip install ultralytics  # For YOLOv8
</code></pre>

<h3>2. Add a Video File</h3>
<p>Place the video file you want to process in the directory. Ensure the filename is correct.</p>

<h3>3. Run the Object Detection Script</h3>
<pre><code>python object_detection.py </code></pre>

<h3>4. View the Results</h3>
<p>The processed video with detected objects will be saved in the same directory with the file name <code> output_video_with_boxes.mp4.</code> Cropped images of detected objects will be saved in the <code>cropped_images/</code> directory, and detection details will be saved in <code>detection_output_video3.json</code>.</p>

<h3>Output Video</h3>
<video width="640" height="480" controls>
    <source src="output_video_with_boxes3.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

<h2>Script Details</h2>

<h3><code>object_detection.py</code></h3>
<p>This script handles the object detection process. It reads the input video, applies the YOLOv8x model, and saves the output video with bounding boxes around detected objects. Additionally, it saves cropped images of each detected object and outputs detection details in a JSON file.</p>

<h2>Contributing</h2>
<p>Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.</p>

<h2>Acknowledgments</h2>
<ul>
    <li><a href="https://github.com/ultralytics/yolov8">YOLOv8 Documentation</a></li>
    <li><a href="https://pytorch.org/">PyTorch</a></li>
    <li><a href="https://opencv.org/">OpenCV</a></li>
</ul>

<hr>

<p>For any queries or support, feel free to contact <a href="mailto:kumar.rajnish6587@gmail.com">kumar.rajnish6587@gmail.com</a> or open an issue on this repository.</p>
