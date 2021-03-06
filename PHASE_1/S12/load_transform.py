import torch
import torchvision



def load(trainset,testset,seed=1,batch_size=128,num_workers=4,pin_memory=True):
	

	#Get the Train and Test Set
	# trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=train_transform)
	# testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=test_transform)


	SEED = 1

	# CUDA?
	cuda = torch.cuda.is_available()


	# For reproducibility
	torch.manual_seed(SEED)

	if cuda:
			torch.cuda.manual_seed(SEED)

	# dataloader arguments - something you'll fetch these from cmdprmt
	dataloader_args = dict(shuffle=True, batch_size=batch_size, num_workers=num_workers, pin_memory=pin_memory) if cuda else dict(shuffle=True, batch_size=64)

	trainloader = torch.utils.data.DataLoader(trainset, **dataloader_args)
	testloader = torch.utils.data.DataLoader(testset, **dataloader_args)


	return  trainloader, testloader