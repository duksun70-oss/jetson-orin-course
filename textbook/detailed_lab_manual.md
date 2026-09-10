# Jetson Orin 14주 상세 실습매뉴얼

## 공통 실습 절차
1. 장비 모델, JetPack/L4T, CUDA, Python, OpenCV, PyTorch 버전을 기록한다.
2. 전원, 냉각, 저장장치, 네트워크, 카메라, 센서 연결 상태를 확인한다.
3. 실습 코드를 실행하기 전 예상 결과를 먼저 작성한다.
4. 실행 로그, 화면 캡처, FPS/latency/CPU/GPU/메모리/온도 값을 저장한다.
5. 오류가 발생하면 명령어, 오류 메시지, 원인 가설, 해결 조치를 기록한다.

## 공통 시스템 구성도
```text
[Camera / LiDAR / RealSense / Arduino]
                 |
                 v
        [Jetson Orin Sensor I/O]
                 |
        +--------+---------+
        |                  |
 [AI Perception]     [ROS 2 Middleware]
        |                  |
        +--------+---------+
                 v
        [Decision / Planner]
                 |
                 v
        [Motor Controller / AMR]
```

## Week 01 Lab. 환경 점검
실습: `setup/system_check.sh`를 실행하고 OS, L4T, CUDA, Python, OpenCV를 기록한다. `jtop`으로 CPU/GPU/온도/전력 상태를 캡처한다.
Troubleshooting: `nvcc not found`는 CUDA path 또는 JetPack 설치 문제일 수 있다. `jtop`이 실행되지 않으면 `sudo -H pip3 install -U jetson-stats` 후 재부팅한다.

## Week 02 Lab. GPIO/PWM
회로: GPIO 출력핀 → 330Ω 저항 → LED → GND. Jetson GPIO는 3.3V 기준이며 5V 입력 금지.
실습: LED blink 후 PWM duty 20/50/80%를 비교한다.
Troubleshooting: 권한 오류는 gpio group 또는 sudo 실행을 확인한다. 핀 동작이 없으면 BOARD 번호와 실제 핀 위치를 재확인한다.

## Week 03 Lab. Camera/OpenCV
시스템: USB/CSI Camera → OpenCV VideoCapture/GStreamer → frame processing → display/FPS log.
실습: 원본, grayscale, Canny edge를 표시하고 해상도별 FPS를 측정한다.
Troubleshooting: 카메라가 열리지 않으면 `/dev/video*`, 권한, 케이블, 다른 프로세스 점유 여부를 확인한다.

## Week 04 Lab. CUDA 성능 비교
실습: 행렬 크기 500, 1000, 3000에서 CPU/GPU 시간을 반복 측정한다. GPU 측정 전 warm-up과 synchronize를 수행한다.
Troubleshooting: CUDA unavailable은 PyTorch CUDA 빌드, JetPack 버전, 환경변수를 확인한다.

## Week 05 Lab. PyTorch 추론
실습: 경량 모델을 CPU/GPU에서 각각 실행하고 latency 평균을 비교한다. batch size와 input size를 변경한다.
Troubleshooting: out of memory 발생 시 batch size를 줄이고 불필요한 프로세스를 종료한다.

## Week 06 Lab. TensorRT
실습: ONNX export 후 `trtexec --fp16`으로 engine을 생성하고 latency/throughput을 기록한다.
Troubleshooting: unsupported operator는 ONNX opset, 모델 구조, TensorRT plugin 필요성을 확인한다.

## Week 07 Lab. YOLO 실시간 검출
실습: 이미지 추론 → 카메라 추론 → 해상도별 FPS 비교 → 오검출/미검출 사례 분석.
Troubleshooting: FPS가 낮으면 모델 크기, 입력 해상도, TensorRT 변환, 화면 표시 비용을 점검한다.

## Week 08 Lab. 중간 통합
실습: 카메라 입력, YOLO 검출, FPS overlay, jtop 기록을 통합한다. 3분 이상 연속 실행 안정성을 검증한다.
Troubleshooting: 시간이 지날수록 느려지면 memory leak, 로그 저장량, 온도 throttling을 확인한다.

## Week 09 Lab. ROS 2 Publisher/Subscriber
실습: `sensor_msgs` 또는 `std_msgs`로 주기 메시지를 발행하고 `ros2 topic echo`, `ros2 topic hz`로 확인한다.
Troubleshooting: 토픽이 보이지 않으면 domain id, source setup.bash, 노드 namespace를 확인한다.

## Week 10 Lab. ROS 2 Camera/Sensor
실습: 이미지 토픽과 센서 토픽을 발행하고 RViz/rosbag으로 확인한다. frame_id와 timestamp를 기록한다.
Troubleshooting: 이미지 지연은 QoS, 압축, 해상도, 네트워크 대역폭을 확인한다.

## Week 11 Lab. LiDAR/RealSense
실습: depth image, point cloud, scan topic을 시각화한다. 거리별 노이즈와 결측을 측정한다.
Troubleshooting: TF 오류는 frame 이름, static transform, launch 순서를 확인한다.

## Week 12 Lab. SLAM/Nav2
실습: 저속으로 지도 작성, 저장, localization, goal navigation을 수행한다.
Troubleshooting: 지도 왜곡은 휠 오도메트리, LiDAR 높이, 속도, loop closure 실패를 점검한다.

## Week 13 Lab. AI-AMR 상태기반 제어
실습: YOLO 검출 결과를 ROS 2 message로 보내고 NORMAL/SLOW/STOP/FAULT 상태를 정의한다.
Troubleshooting: 오검출이 많으면 confidence threshold, NMS, 클래스 제한, 조명 조건을 조정한다.

## Week 14 Lab. 최종 프로젝트
실습: 요구사항 정의, 아키텍처, 데모 시나리오, 시험표, 안전계획, 발표자료를 완성한다.
Troubleshooting: 마지막 주에는 새 기능 추가보다 안정화, 재현성, 발표 스토리 정리에 집중한다.
