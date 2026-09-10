# Week 04 - CUDA 기초 및 CPU/GPU 비교

## 학습목표
- GPU 병렬연산의 기본 개념을 이해한다.
- CUDA가 사용 가능한 Python 환경을 확인한다.
- 동일 연산의 CPU/GPU 실행시간을 비교한다.

## 실습
`cpu_gpu_benchmark.py`를 실행하고 행렬 크기를 변경하여 측정한다.

## 주의
GPU 연산은 초기화와 데이터 전송 오버헤드가 있으므로 작은 문제에서는 CPU가 더 빠를 수 있다. 측정 전 warm-up을 수행한다.

## 제출물
행렬 크기별 CPU/GPU 시간과 speed-up 그래프
