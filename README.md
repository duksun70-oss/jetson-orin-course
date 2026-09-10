# Jetson Orin 14-Week Hands-on Course

NVIDIA Jetson Orin을 활용하여 Linux/Python 기초부터 CUDA, TensorRT, Computer Vision, ROS 2, 센서, SLAM, AI 기반 AMR 통합까지 단계적으로 학습하는 14주 실습 플랫폼입니다.

## 교육 목표
- Jetson Orin 하드웨어와 JetPack 소프트웨어 스택 이해
- Python/OpenCV/CUDA/PyTorch/TensorRT 기반 Edge AI 구현
- ROS 2 기반 센서·카메라·로봇 소프트웨어 구성
- LiDAR/RealSense와 SLAM/Nav2 실습
- 최종적으로 AI 인지 기능을 포함한 AMR/자율주행 미니 프로젝트 구현

## 권장 장비
- Jetson Orin Nano 또는 Orin NX
- USB 또는 CSI 카메라
- Intel RealSense(선택)
- 2D LiDAR(선택)
- Arduino 및 모터 드라이버/센서(통합 실습용)

## 14주 과정
| 주차 | 주제 | 핵심 결과물 |
|---|---|---|
| 01 | Orin 및 JetPack 환경 구축 | 시스템 점검 리포트 |
| 02 | Linux/Python/GPIO | GPIO·PWM 제어 |
| 03 | Camera + OpenCV | 실시간 영상 처리 |
| 04 | CUDA 기초 | CPU/GPU 성능 비교 |
| 05 | PyTorch on Jetson | GPU 추론 실습 |
| 06 | ONNX + TensorRT | 모델 최적화 및 FPS 비교 |
| 07 | YOLO 객체 인식 | 실시간 객체 검출 |
| 08 | 중간 통합 실습 | Camera+YOLO+성능 측정 |
| 09 | ROS 2 기초 | Publisher/Subscriber |
| 10 | ROS 2 + Camera/Sensor | 센서 토픽 구성 |
| 11 | LiDAR/RealSense | Point Cloud/Depth 처리 |
| 12 | SLAM + Nav2 | 지도 작성 및 자율주행 |
| 13 | AI 기반 AMR | 인지+주행 통합 |
| 14 | 최종 프로젝트 | Jetson Orin 기반 AMR 데모 |

## 수업 운영 권장 방식
각 주차는 `이론 30~40분 → 환경/코드 설명 20분 → 실습 80~100분 → 결과 정리 20분` 구조를 권장합니다. 각 폴더의 README에는 학습목표, 준비물, 실습 절차, 제출물, 심화과제가 포함됩니다.

## 저장소 구조
- `syllabus/`: 14주 강의계획 및 평가 기준
- `setup/`: Jetson 환경 점검 스크립트
- `week01_...` ~ `week14_...`: 주차별 실습 자료
- `assignments/`: 과제/보고서 템플릿
- `references/`: 참고 오픈소스 저장소와 라이선스 확인 가이드

> 실제 JetPack, CUDA, TensorRT, ROS 2 버전은 사용하는 Jetson 이미지에 따라 달라질 수 있으므로 수업 시작 전에 장비 환경을 고정하고 기록하세요.
