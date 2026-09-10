import torch

print('PyTorch:', torch.__version__)
print('CUDA available:', torch.cuda.is_available())
if torch.cuda.is_available():
    print('Device:', torch.cuda.get_device_name(0))
    x = torch.randn(1000, 1000, device='cuda')
    y = torch.mm(x, x)
    print('GPU tensor test:', y.shape)
