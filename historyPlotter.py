def valHistoryPlotter(historyDicts, title):
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    mpl.style.use('seaborn')

    epochsRange = range(1, len(historyDicts['local']['val_binary_accuracy']) + 1)
    
    for i in historyDicts:
        plt.plot(epochsRange, historyDicts[i]['val_binary_accuracy'], label=i+' (train time: ' + str(historyDicts[i]['trainTime']) + ')')

    plt.title(title)
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()