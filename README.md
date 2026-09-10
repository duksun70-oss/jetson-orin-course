# Jetson Orin 14-Week University Laboratory Course

NVIDIA Jetson Orin을 활용해 Edge AI, Computer Vision, ROS 2, 센서 융합, SLAM/Nav2, AI 기반 AMR 통합까지 학습하는 정규 대학 실습교재형 저장소입니다.

## 교재 구성
- `syllabus/`: 교과목 개요, 학습성과, 주차별 계획
- `instructor/`: 교수자 운영가이드, 정답/해설, 장비 체크리스트
- `safety/`: 실습실 안전 및 하드웨어 주의사항
- `assessment/`: 중간/기말 프로젝트 명세와 평가 루브릭
- `assignments/`: 실습보고서와 팀 프로젝트 템플릿
- `week01_...` ~ `week14_...`: 주차별 Lecture Note, Lab Manual, Quiz
- `setup/`: 환경 점검 및 공통 실행 스크립트
- `references/`: 오픈소스 참고자료 및 라이선스 가이드

## 권장 수업 운영
주 3시간 기준: 이론 40분 → 실습 준비 20분 → 실습 90분 → 결과 분석 및 토론 30분.

## 학습 성과
수강생은 수업 종료 시 다음을 수행할 수 있어야 합니다.
1. Jetson Orin/JetPack/CUDA/TensorRT 환경을 점검하고 재현 가능하게 기록한다.
2. OpenCV·PyTorch·TensorRT 기반 Edge AI 추론 파이프라인을 구현한다.
3. ROS 2 Node/Topic/TF를 이용해 카메라·센서·로봇 기능을 통합한다.
4. LiDAR/Depth Camera를 이용해 SLAM과 Navigation을 구성한다.
5. AI 인지와 AMR 주행을 통합하고 성능·안전·한계를 정량적으로 분석한다.

## 14주 로드맵
01 환경 구축 · 02 Linux/Python/GPIO · 03 Camera/OpenCV · 04 CUDA · 05 PyTorch · 06 ONNX/TensorRT · 07 YOLO · 08 중간 프로젝트 · 09 ROS 2 · 10 ROS 2 센서 · 11 LiDAR/RealSense · 12 SLAM/Nav2 · 13 AI-AMR · 14 최종 프로젝트

> JetPack/CUDA/TensorRT/ROS 2 세부 버전은 장비 이미지에 따라 달라질 수 있으므로 학기 시작 시 `instructor/environment_baseline.md`를 작성해 고정합니다.