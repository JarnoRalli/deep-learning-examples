# This script plots the sigmoid function and its derivative
import numpy as np
import matplotlib.pyplot as plt
import torch

x = torch.linspace(-8.0, 8.0, 100, requires_grad=True)

sigmoid = 1.0 / (1.0 + torch.exp(-x))
sigmoid.backward(torch.ones_like(x))

plt.plot(x.detach().numpy(), sigmoid.detach().numpy(), "b", label="Sigmoid")
plt.plot(x.detach().numpy(), x.grad.detach().numpy(), "r", label="Derivative of Sigmoid")
plt.xlabel("z")
plt.axvspan(-4, 4, alpha=0.25, color="green")
plt.grid()
plt.legend()
plt.show()
