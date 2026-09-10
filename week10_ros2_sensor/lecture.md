# Week 10 Lecture — ROS 2 Camera/Sensor Integration

## 핵심 개념
센서 메시지는 값뿐 아니라 timestamp와 frame 정보를 함께 관리해야 다중 센서 융합이 가능하다.

## 학습 포인트
- `sensor_msgs/Image`, `LaserScan`, `Imu`
- Header timestamp
- frame_id와 TF
- 센서 주기와 QoS
- Camera image transport 개념