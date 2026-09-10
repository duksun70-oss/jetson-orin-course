# Week 10 - ROS 2 + Camera/Sensor

## 학습목표
- 카메라/센서를 ROS 2 topic으로 다룬다.
- timestamp, frame_id, message rate 개념을 이해한다.
- 센서 데이터 지연과 drop을 관찰한다.

## 실습
- USB/CSI 카메라 ROS 2 node 실행
- `image_raw` 또는 해당 image topic 확인
- `ros2 topic hz`로 rate 측정
- Arduino/Serial 센서가 있으면 거리 또는 상태값을 custom/string topic으로 전달

## 제출물
ROS graph, topic rate, sensor-to-display latency 관찰 결과
