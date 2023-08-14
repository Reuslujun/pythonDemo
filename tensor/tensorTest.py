import torch
import numpy as np

tensor_x  = torch.ones(5)
print(tensor_x)
print(tensor_x.shape)

numpy_a = [[1,2,3,4,5]]
np.array(numpy_a)

print(np.array(numpy_a).shape)
print(torch.tensor(numpy_a).shape)