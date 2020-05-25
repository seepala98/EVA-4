def train_net(net, device,train_loader, epochs , lr):
    import datetime
    global_step = 0
    #optimizer = optim.RMSprop(net.parameters(), lr=lr, weight_decay=1e-8, momentum=0.9)
    optimizer = optim.SGD(net.parameters(), lr=lr, weight_decay=1e-8, momentum=0.9)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer,  patience=2)
    #scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.01)
    #criterion = nn.BCEWithLogitsLoss()
    criterion = DiceLoss()
    #criterion = smp.utils.losses.DiceLoss()
    #criterion = CompoundLoss()
    #criterion = SSIM(3)
    n_train =len(train_loader)
    init = datetime.datetime.now()
    for epoch in range(epochs):
        start =  datetime.datetime.now()
        model.train()
        epoch_loss = 0  
        pbar = tqdm(train_loader)
        #with tqdm(total=n_train, desc=f'Epoch {epoch + 1}/{epochs}', unit='img') as pbar:

        for i,data in enumerate(pbar):
            data['bg'] = data['bg'].to(device, dtype = torch.float32) #, dtype = torch.float32
            data['fg_bg'] = data['fg_bg'].to(device, dtype = torch.float32)
            data['depth_fg_bg'] = data['depth_fg_bg'].to(device, dtype = torch.float32)
            data['fg_bg_mask'] = data['fg_bg_mask'].to(device, dtype = torch.float32)

            #depth_pred, masks_pred
            x = torch.cat([data['bg'], data['fg_bg']], dim=1)
            
            d_out, s_out = model(x)

            loss1 = criterion(s_out, data['fg_bg_mask'])
            loss2 = criterion(d_out, data['depth_fg_bg']) 

            loss = 2 * loss1 +  loss2 
            epoch_loss += loss.item()
            pbar.set_postfix(desc  = f'Epoch : {epoch+1}  Loss : {loss.item()}  l1: {loss1.item()} l2 = {loss2.item()}')
            optimizer.zero_grad()
            loss.backward()
            nn.utils.clip_grad_value_(net.parameters(), 0.1)
            optimizer.step()

            if i % 200 == 0:
                print("ground truth")
                show(data['depth_fg_bg'] .detach().cpu(),nrow=8)
                print("Depth")
                show(d_out.detach().cpu(),nrow=8) # depth
                print("mask")
                show(s_out.detach().cpu(),nrow=8) #mask
                
        scheduler.step() #loss
        end=  datetime.datetime.now()
        print("Time taken for epoch is: ", end-start)
        print(" Total time taken is : ", end -init)
        print("ground truth")
        show(data['depth_fg_bg'] .detach().cpu(),nrow=8)
        print("Depth")
        show(d_out.detach().cpu(),nrow=8) # depth
        print("mask")
        show(s_out.detach().cpu(),nrow=8) #mask