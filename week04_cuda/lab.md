# Week 04 Lab — CPU/GPU Benchmark

## 절차
1. `cpu_gpu_benchmark.py` 실행.
2. N=500,1000,2000,3000 등으로 반복.
3. 각 조건 5회 이상 측정 후 평균/표준편차 계산.
4. GPU는 warm-up 후 `torch.cuda.synchronize()` 사용.
5. 문제 크기별 speed-up 그래프 작성.

## 토론
작은 행렬에서 GPU가 느릴 수 있는 이유를 측정값으로 설명한다.