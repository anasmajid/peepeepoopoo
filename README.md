# An e-waste detector and seperator

Hardware components
Arduino Uno

Nano Jetso

MG 996R servo motor

Arduino connected to servo motors, and nano jetson with built in camera
Camera was used as input video feed into the custom trained yolov7 model for ouruse case
Conveyer belt was built using 2 toilet rolls and a cloth as a base with paper wrapping onto it
Conveyer belt flap was built using a cardboard and bamboo sticks


Software components
Model used: wongkinyiu-YOLOv7 object detection
Data used to train the model:
	1. Gary Thung Trashnet
	2. E-waste: ROBOFLOW ewaste-mx8fq
Both datasets were combined and converted into yolo format before fine-tuning
Model was finetuned using YOLOv7 COCO pretrained weights
The object detection model was fine-tuned on a 3090 GPU for 300 epochs with batch size of 32 with image size of 512
Training took total of about 3 to 4 hours

Process:
1. Video camera feed from the Nano Jetson as input to our customed trained yolov7 model
2. Prediction will be processed to ensure lower false positives detections
3. Predicted output of class will be sent to arduino
4. Arduino reads input from Nano Jetson
5. Arduino starts moving conveyer belt and flaps as necessary



