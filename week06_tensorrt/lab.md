# Week 06 Lab — ONNX→TensorRT

## 절차
1. 제공 모델을 ONNX export.
2. 입력/출력 shape 검증.
3. `trtexec --onnx=model.onnx --saveEngine=model_fp16.engine --fp16` 실행.
4. FP32/FP16 latency와 throughput 측정.
5. engine 파일 크기와 출력 차이 확인.

## 제출
빌드 로그, 성능표, FP16 사용 장단점.