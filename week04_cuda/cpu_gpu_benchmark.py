import time
import torch

N = 3000

a = torch.randn(N, N)
b = torch.randn(N, N)

t0 = time.perf_counter()
c = a @ b
cpu_time = time.perf_counter() - t0
print(f'CPU: {cpu_time:.4f}s')

if torch.cuda.is_available():
    ag = a.cuda(); bg = b.cuda()
    for _ in range(2):
        _ = ag @ bg
    torch.cuda.synchronize()
    t0 = time.perf_counter()
    cg = ag @ bg
    torch.cuda.synchronize()
    gpu_time = time.perf_counter() - t0
    print(f'GPU: {gpu_time:.4f}s')
    print(f'Speed-up: {cpu_time/gpu_time:.2f}x')
else:
    print('CUDA not available')
