import torch
from tqdm import tqdm

def val(model, val_loader, device, criterion, losses, accuracies):
    model.eval()
    correct = 0
    val_loss = 0
    with torch.no_grad():
        pbar1 = tqdm(testloader)
        for i, (data, target) in enumerate(pbar1):
           data, target = data.to(device), target.to(device)
           outputs = model(data)
           _, predicted = torch.max(outputs.data, 1)
           loss = criterion(outputs, target)
           total += target.size(0)
           correct += (predicted == target).sum().item()
        
        print("Test Loss=", loss.cpu().numpy(), "Test Accuracy=",100*correct/total)
        #pbar1.update(1)  
        #print('Loss %0.2f Accuracy of the network on the 10000 test images: %0.2f', loss, (100 * correct / total))
    test_acc = (100 * correct / total)  

    return test_acc, loss.cpu().numpy()
