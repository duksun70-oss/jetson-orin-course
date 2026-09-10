# Week 05 - PyTorch on Jetson

## 학습목표
- Tensor와 GPU device 개념을 이해한다.
- 사전학습 모델을 이용한 이미지 추론 흐름을 이해한다.
- CPU/GPU inference time을 비교한다.

## 실습
1. `torch.cuda.is_available()` 확인
2. Tensor CPU→GPU 이동
3. torchvision 사전학습 모델 또는 강사가 제공한 경량 모델 실행
4. warm-up 후 30회 이상 반복 측정

## 제출물
모델명, 입력 크기, CPU/GPU 평균 latency, 메모리 사용량
