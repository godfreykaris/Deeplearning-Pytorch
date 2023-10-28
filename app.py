import torch

# Create a random tensor of size (3,4)
# random_tensor = torch.rand(3,4)
# print(random_tensor)
# Output
# tensor([[0.1710, 0.1178, 0.0496, 0.1588],
#         [0.7165, 0.3322, 0.6542, 0.2513],
#         [0.2263, 0.2810, 0.5147, 0.9881]])

# print(random_tensor.shape) #torch.Size([3, 4])
# print(random_tensor.ndim) #2

# Create a tensor of all zeros
### Useful when masking some of the values in one tensor with zeros to let a model know not to learn them
# zeros = torch.zeros(size=(3, 4))
# print(zeros)
# Output
# tensor([[0., 0., 0., 0.],
#         [0., 0., 0., 0.],
#         [0., 0., 0., 0.]])
# print(zeros.dtype) # torch.float32