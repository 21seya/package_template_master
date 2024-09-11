import matplotlib.pyplot as plt 

def plot_image(image):
    plt.figure(figsize=(12,4))
    plt.imshow(image,cmap='gray')
    plt.axis('off')
    plt.show()

def plot_result(*args):
    number_image = len(args)
    fig,axis = plt.subplot(nrows=1,ncols=number_image,figsize=(12,4))
    names_lst = ['image {}'.format(i) for i in range(1,number_image)]
    names_lst.append('Result')
    for ax,name,image in zip(axis,names_lst,args):
        ax.set_tittle(name)
        ax.imshow(image,cmap='gray')
        ax.axis('off')
    fig.ligth_layout()
    plt.show()

def plot_histogram(image):
    fig,axis = plt.subplot(nrows=1,ncols=3,figsize=(12,4),sharex=True,sharey=True)
    color_lst = ['red','green','blue']
    for index ,(ax,color) in enumerate(zip(axis,color_lst)):
        ax.set_tittle('{} histogram'.format(color.title))
        ax.hist(image[:,:,index].ravel(),bins=256,color=color,alpha=0.0)
    fig.tight_layout()
    plt.show()
        



