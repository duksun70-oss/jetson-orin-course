# 퀴즈 정답 요약

1주: L4T는 Jetson Linux 기반 배포 스택, CUDA는 GPU 병렬 컴퓨팅 플랫폼. Baseline 기록은 재현성을 위해 필요.
2주: Jetson GPIO는 3.3V 로직. 5V 직접 입력 금지. PWM duty는 평균 출력 비율을 바꿈.
3주: FPS는 초당 처리 프레임 수. 해상도 증가 시 처리량과 메모리 요구가 증가.
4주: GPU 측정 시 warm-up과 `torch.cuda.synchronize()`가 중요.
5주: `eval()`은 추론 모드, `no_grad()`는 gradient 기록을 비활성화.
6주: ONNX는 모델 교환 형식, TensorRT engine은 특정 플랫폼/설정에 최적화된 실행 산출물.
7주: NMS는 중복 bbox 억제. confidence threshold 조정은 precision/recall trade-off를 유발.
8주: 평균 FPS만이 아니라 latency, GPU load, memory와 오류 사례를 함께 평가.
9주: Node는 실행 단위, Topic은 메시지 채널, QoS는 전달 정책.
10주: Timestamp와 frame_id는 센서 융합/TF에 중요.
11주: Depth는 픽셀별 거리, PointCloud는 3D 점 집합.
12주: SLAM은 지도작성+자기위치추정, Nav2는 경로계획/제어 스택.
13주: 인지 결과를 즉시 모터명령으로 연결하기보다 상태/안전계층을 둬야 함.
14주: 성공률·latency·안전정지·재현성으로 종합 검증.