# PPT 강의자료 구성안

## 공통 슬라이드 흐름
각 주차 PPT는 10~12장 구성을 권장한다.
1. 주차 제목과 학습목표
2. 실제 응용 장면: Edge AI, AMR, 자율주행, 스마트물류
3. 핵심 이론 1
4. 핵심 이론 2
5. 시스템 구성도
6. 코드 구조 설명
7. 실습 절차
8. 성능 측정 방법
9. Troubleshooting
10. 제출물 및 평가 기준
11. 심화 과제
12. 다음 주차 연결

## 주차별 PPT 제목
01 Jetson Orin과 Edge AI 플랫폼
02 Linux, Python, GPIO와 하드웨어 안전
03 Camera Pipeline과 OpenCV 영상처리
04 CUDA 병렬연산과 성능 측정
05 PyTorch 기반 GPU 추론
06 ONNX와 TensorRT 최적화
07 YOLO 실시간 객체인식
08 중간 통합 프로젝트: Camera + YOLO + Monitoring
09 ROS 2 Node와 Topic 통신
10 ROS 2 Camera/Sensor 데이터 파이프라인
11 LiDAR/RealSense와 Point Cloud
12 SLAM, Localization, Nav2
13 AI 인지 기반 AMR 상태제어
14 최종 프로젝트 발표 및 데모

## 시각자료 권장
- Jetson Orin 하드웨어 블록도
- Camera → Preprocess → Inference → Decision 파이프라인
- ROS 2 Topic graph
- LiDAR/RealSense 좌표계와 TF tree
- AMR 상태도: NORMAL/SLOW/STOP/FAULT
- 평가 루브릭 표

## 교수자 메모
PPT는 모든 내용을 설명하는 문서가 아니라 실습 전 방향을 잡는 시각 자료이다. 자세한 절차와 채점 기준은 `detailed_lab_manual.md`, `student_workbook.md`, `instructor_solution_guide.md`를 함께 사용한다.
