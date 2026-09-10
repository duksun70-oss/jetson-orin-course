# Week 06 - ONNX + TensorRT

## 학습목표
- PyTorch → ONNX → TensorRT 최적화 흐름을 이해한다.
- FP32/FP16의 정확도와 속도 trade-off를 설명한다.
- TensorRT 실행 성능을 측정한다.

## 실습 흐름
1. 학습된 모델을 ONNX로 export
2. ONNX 구조/입출력 shape 확인
3. `trtexec`로 TensorRT engine 생성
4. latency/throughput 측정

## 예시 명령
```bash
trtexec --onnx=model.onnx --saveEngine=model_fp16.engine --fp16
trtexec --loadEngine=model_fp16.engine
```

## 제출물
FP32/FP16 빌드 로그, latency, throughput, engine 크기 비교
