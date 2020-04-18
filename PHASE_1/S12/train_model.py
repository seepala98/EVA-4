import torch

#Training & Testing Loops
from tqdm.notebook import tqdm
from tqdm import tqdm_notebook

test_loss = []
test_acc = []
train_loss = []
train_loss = []
LR = []
train_scheduler = False

def train_model(model,device,trainloader,testloader,optimizer,criterion,EPOCHS,scheduler = False,batch_scheduler = False ,best_acc = 0,path = "/content/gdrive/My Drive/API/bestmodel.pt"):
  for epoch in range(EPOCHS):
      print("EPOCH:", epoch+1,'LR:',optimizer.param_groups[0]['lr'])
      LR.append(optimizer.param_groups[0]['lr'])
      train_scheduler = False

      if(batch_scheduler):
        train_scheduler = scheduler
      train_loss, train_acc = train(model, device, trainloader, optimizer, criterion, epoch,train_scheduler)
      
      test_loss , test_acc = test(model, device, criterion, testloader)
      if(scheduler and not batch_scheduler and not isinstance(scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau)): 
        scheduler.step()

      elif(scheduler and not batch_scheduler and  isinstance(scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau)):
        scheduler.step(test_loss[-1])
      
      
      if(test_acc[-1]>best_acc):
        print("accuracy increased, Saving model....")
        best_acc = test_acc[-1]
        torch.save({
              'epoch': epoch,
              'model_state_dict': model.state_dict(),
              'optimizer_state_dict': optimizer.state_dict(),
              'loss': test_loss[-1],
              }, path)