#!/usr/bin/env bash
set -e

echo '=== Jetson Orin System Check ==='
echo '[OS]'
cat /etc/os-release | grep -E 'PRETTY_NAME|VERSION='
echo '[Kernel]'
uname -a
echo '[L4T]'
dpkg-query --show nvidia-l4t-core 2>/dev/null || true
echo '[CUDA]'
nvcc --version 2>/dev/null || echo 'nvcc not found'
echo '[GPU]'
nvidia-smi 2>/dev/null || true
echo '[Python]'
python3 --version
echo '[OpenCV]'
python3 - <<'PY'
try:
 import cv2
 print(cv2.__version__)
 print('CUDA devices:', cv2.cuda.getCudaEnabledDeviceCount() if hasattr(cv2,'cuda') else 'N/A')
except Exception as e:
 print('OpenCV check failed:', e)
PY
