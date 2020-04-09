import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

model_name = "hmdb51-mv "#"model-1570499409" # grab whichever model name you want here. We could also just reference the MODEL_NAME if you're in a notebook still.


def create_acc_loss_graph(model_name):
    contents = open("gen_flow_train_lr0.01.log", "r").read().split("\n")

    epochs = []
    accuracies1 = []
    accuracies5 = []
    losses = []

    val_accs1 = []
    val_accs5 = []
    val_losses = []

    for c in contents:
        if len(c)>10:
            epoch, acc1, acc5, val_acc1, val_acc5, loss, val_loss, _,_,_,_,_ = c.split(" ")

            epochs.append(int(epoch[6:]))
            accuracies1.append(float(acc1[7:]))
            accuracies5.append(float(acc5[7:]))
            losses.append(float(loss[9:]))

            val_accs1.append(float(val_acc1[12:]))
            val_accs5.append(float(val_acc5[12:]))
            val_losses.append(float(val_loss[13:]))

    fig = plt.figure()

    ax1 = plt.subplot2grid((2,1), (0,0))
    ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)


    ax1.plot(epochs, accuracies1, label="prec@1")
    ax1.plot(epochs, val_accs1, label="test_prec@1")
    ax1.plot(epochs, accuracies5, label="prec@5")
    ax1.plot(epochs, val_accs5, label="test_prec@5")
    ax1.legend(loc=2)
    ax2.plot(epochs,losses, label="loss")
    ax2.plot(epochs,val_losses, label="val_loss")
    ax2.legend(loc=2)
    plt.show()

create_acc_loss_graph(model_name)
