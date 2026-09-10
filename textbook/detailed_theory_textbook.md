# Jetson Orin 14주 상세 이론교재

## 교재 목표
본 교재는 Jetson Orin을 단순 AI 보드가 아니라 Edge AI 기반 자율이동체 플랫폼으로 이해하도록 구성한다. 학생은 Linux, Python, 카메라, CUDA, PyTorch, TensorRT, ROS 2, LiDAR/RealSense, SLAM, Nav2, AMR 통합 구조를 단계적으로 학습한다.

## Week 01. Jetson Orin과 JetPack 환경
Jetson Orin은 CPU, NVIDIA GPU, 메모리, 카메라 인터페이스, GPIO, 고속 I/O가 하나의 임베디드 플랫폼에 통합된 Edge AI 컴퓨터이다. 데스크톱 GPU와 달리 전력, 발열, 저장장치, 실시간성 제약을 동시에 고려해야 한다. JetPack은 Ubuntu 기반 OS, L4T, CUDA, cuDNN, TensorRT, Multimedia API, 카메라 드라이버를 묶은 소프트웨어 스택이다. 실습의 핵심은 성능 자체보다 장비의 버전과 재현성을 정확히 기록하는 것이다. 동일 코드라도 JetPack, CUDA, TensorRT, PyTorch 버전에 따라 실행 결과가 달라질 수 있다.

## Week 02. Linux, Python, GPIO
Jetson 개발의 기본은 터미널, 파일 권한, 프로세스, 패키지 관리이다. Python은 하드웨어 제어와 AI 모델 실행을 연결하는 접착 언어 역할을 한다. GPIO 실습에서는 BOARD 번호와 BCM/SoC 번호의 차이를 이해해야 하며, Jetson GPIO는 3.3V 로직이므로 5V 센서 신호를 직접 입력하면 보드가 손상될 수 있다. PWM은 디지털 출력의 듀티비를 조절해 LED 밝기나 모터 속도를 근사적으로 제어하는 방식이다.

## Week 03. Camera와 OpenCV
카메라는 자율주행·로봇 인지의 가장 기본 센서이다. USB 카메라는 간단하지만 지연과 대역폭 제약이 있고, CSI 카메라는 성능은 좋지만 드라이버와 GStreamer 설정이 중요하다. OpenCV의 프레임 획득, 색공간 변환, 엣지 검출, FPS 측정은 이후 YOLO와 SLAM의 기초가 된다. 영상처리에서는 해상도, 프레임율, 조명, 노출, 렌즈 왜곡이 결과에 큰 영향을 준다.

## Week 04. CUDA 기초
CUDA는 GPU의 많은 코어를 이용해 병렬 연산을 수행하는 프로그래밍 모델이다. GPU는 큰 행렬 연산이나 영상처리에 강하지만, 작은 연산에서는 데이터 전송과 초기화 오버헤드 때문에 CPU보다 느릴 수 있다. 정확한 측정을 위해 warm-up, 동기화, 반복 측정, 평균·표준편차 계산이 필요하다. 학생은 단순히 GPU가 빠르다고 외우는 것이 아니라 어떤 조건에서 빠른지 설명할 수 있어야 한다.

## Week 05. PyTorch on Jetson
PyTorch는 텐서 연산과 딥러닝 모델 추론을 쉽게 구현하게 해준다. Jetson에서는 CUDA device 확인, 모델과 입력 텐서의 device 일치, 배치 크기, 입력 해상도, 메모리 사용량을 관리해야 한다. 추론 latency는 첫 실행과 반복 실행이 다르므로 warm-up 후 측정한다. Edge AI에서는 정확도뿐 아니라 FPS, latency, 전력, 온도가 동등하게 중요하다.

## Week 06. ONNX와 TensorRT
ONNX는 프레임워크 간 모델 교환 형식이고 TensorRT는 NVIDIA GPU에서 추론을 최적화하는 엔진이다. PyTorch 모델을 ONNX로 내보낸 뒤 TensorRT engine으로 변환하면 layer fusion, precision 변경, 메모리 최적화가 수행된다. FP16은 속도를 높이지만 모델에 따라 정확도 차이가 발생할 수 있다. 실습에서는 FP32/FP16 latency, throughput, engine 크기, 정확도 변화를 비교한다.

## Week 07. YOLO 객체인식
YOLO는 영상을 격자 또는 앵커/디코딩 구조로 처리해 객체 위치와 class를 실시간으로 추정한다. Bounding box, confidence, NMS, IoU를 이해해야 오검출과 미검출을 분석할 수 있다. Jetson에서 실시간 구동하려면 모델 크기, 입력 해상도, TensorRT 변환, 카메라 파이프라인, 화면 표시 비용까지 고려해야 한다.

## Week 08. 중간 통합 프로젝트
중간 프로젝트는 카메라 입력, 객체검출, FPS 표시, 시스템 모니터링을 하나의 파이프라인으로 통합한다. 학생은 기능 구현뿐 아니라 성능 병목을 찾아야 한다. 병목은 카메라 입력, 전처리, 모델 추론, 후처리, 디스플레이, 저장장치 I/O에서 발생한다. 결과 보고서는 정량 지표와 개선 실험을 반드시 포함한다.

## Week 09. ROS 2 기초
ROS 2는 로봇 소프트웨어를 노드와 토픽 중심으로 분리한다. Publisher는 데이터를 발행하고 Subscriber는 이를 구독한다. QoS는 신뢰성, 지연, history를 제어하여 센서 데이터와 제어 명령의 특성에 맞게 통신을 조절한다. ROS 2를 배우는 목적은 단일 Python 스크립트에서 벗어나 복수 센서와 제어 모듈을 확장 가능한 구조로 설계하는 것이다.

## Week 10. ROS 2 Camera/Sensor
카메라와 센서를 ROS 2 토픽으로 발행하면 perception, logging, visualization, control 모듈이 독립적으로 연결된다. frame_id와 timestamp는 센서 융합의 핵심이다. 잘못된 timestamp나 frame 설정은 SLAM, 장애물 인식, 좌표 변환 오류로 이어진다. rosbag은 실험 재현성을 확보하는 중요한 도구이다.

## Week 11. LiDAR와 RealSense
LiDAR는 거리 기반 2D/3D 공간 정보를 제공하고 RealSense는 depth와 RGB 정보를 제공한다. Point cloud는 3차원 점들의 집합이며 좌표계와 필터링이 중요하다. 센서 융합에서는 extrinsic calibration, TF tree, timestamp 동기화가 필수이다. 실습은 단순 시각화에서 끝나지 않고 데이터 품질, 결측, 노이즈, 거리 한계를 분석해야 한다.

## Week 12. SLAM과 Nav2
SLAM은 로봇이 미지 환경에서 위치를 추정하면서 지도를 작성하는 기술이다. Nav2는 지도, localization, costmap, planner, controller, behavior tree를 이용해 목표점까지 이동한다. 지도 품질은 센서 노이즈, 주행 속도, 환경 구조, loop closure에 영향을 받는다. 안전한 자율주행 실습을 위해 저속, 넓은 공간, 비상정지, 보호구역 설정이 필요하다.

## Week 13. AI 기반 AMR
AMR 통합은 perception, decision, control의 결합이다. 객체 인식 결과를 바로 모터 명령으로 연결하면 위험하므로 NORMAL, SLOW, STOP, FAULT와 같은 상태기반 의사결정 구조가 필요하다. confidence, detection timeout, sensor fault, emergency stop 조건을 명확히 정의해야 한다. AI가 불확실할 때 안전하게 정지하는 fail-safe 설계가 핵심이다.

## Week 14. 최종 프로젝트
최종 프로젝트는 문제정의, 요구사항, 시스템 아키텍처, 구현, 시험, 시연, 보고서를 포함한다. 좋은 프로젝트는 단순히 동작하는 코드가 아니라 재현 가능한 실험 절차와 실패 분석을 가진다. 평가에서는 완성도뿐 아니라 안전성, 정량 성능, 팀 역할, 발표 논리, 개선 가능성을 함께 본다.
