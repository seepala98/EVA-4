import torch
import torch.nn as nn
import torch.nn.functional as F
from tqdm import tqdm

def val(model, val_loader, device):
    model.eval()
    correct = 0
    val_loss = 0
    losses = []
    with torch.no_grad():
        for data, target in val_loader:
            img_batch = data  # This is done to keep data in CPU
            data, target = data.to(device), target.to(device)  # Get samples
            output = model(data)  # Get trained model output
            val_loss += F.nll_loss(output, target, reduction='sum').item()  # Sum up batch loss
            pred = output.argmax(dim=1, keepdim=False)  # Get the index of the max log-probability

            correct += pred.eq(target).sum().item()
    
    val_loss /= len(val_loader.dataset)
    losses.append(val_loss)
    accuracies.append(100. * correct / len(val_loader.dataset))
    print(f'\nValidation set: Average loss: {val_loss:.4f}, Accuracy: {correct}/{len(val_loader.dataset)} ({accuracies[-1]:.2f}%)\n')
    test_acc = (100 * correct / len(val_loader.dataset))  

    return test_acc, val_loss
