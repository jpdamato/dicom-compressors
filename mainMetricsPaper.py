import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
import os
from scipy.interpolate import make_interp_spline

import numpy as np
import pandas as pd
from numpy import asarray
from numpy import savetxt
import matplotlib.pyplot as plt
import unicodedata
from unidecode import unidecode
import csv
from pylab import cm
from texttable import Texttable

import latextable

###################################################################################3
def createDeCompressionPlot(data, methods, outfile = '', useResidual = False):
    # 0: plane, 1:method,2: operation,3: elapsedTime, 4:ppOrig,5 :ppRes
    
    dataPNG = data[(data.iloc[:,2] == methods[0])]

    dataZIP = data[(data.iloc[:,2] == methods[1])]

    dataZSTD = data[(data.iloc[:,2] == methods[2])]

    # Generate 2 colors from the 'tab10' colormap
    colors = cm.get_cmap('tab10', 10)
    # Create figure and add axes object
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Plot and show our data
    # Without residual
    ax.plot(dataPNG.iloc[:, 1], dataPNG.iloc[:, 4], label =methods[0], color = colors(0))
    ax.plot(dataZIP.iloc[:, 1], dataZIP.iloc[:, 4], label =methods[1], color = colors(1))
    ax.plot(dataZSTD.iloc[:,1], dataZSTD.iloc[:,4] , label =methods[2], color = colors(3))

    if useResidual:
        ax2.plot(dataPNG.iloc[:, 1], dataPNG.iloc[:, 6], label =methods[0], color = colors(0))
        ax2.plot(dataZIP.iloc[:, 1], dataZIP.iloc[:, 6], label =methods[1], color = colors(1))
        ax2.plot(dataZSTD.iloc[:,1], dataZSTD.iloc[:,6] , label =methods[2], color = colors(3))
    else:
        ax2.plot(dataPNG.iloc[:, 1], dataPNG.iloc[:, 5], label =methods[0], color = colors(0))
        ax2.plot(dataZIP.iloc[:, 1], dataZIP.iloc[:, 5], label =methods[1], color = colors(1))
        ax2.plot(dataZSTD.iloc[:, 1], dataZSTD.iloc[:, 5], label=methods[2], color=colors(3))
        
    # Edit the major and minor ticks of the x and y axes
    ax.xaxis.set_tick_params(which='major', size=10, width=2, direction='in', top='on')
    ax.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in', top='on')
    ax.yaxis.set_tick_params(which='major', size=10, width=2, direction='in', right='on')
    ax.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in', right='on')
    # Add the x and y-axis labels
    ax.set_xlabel('#frame', labelpad=10)
    ax.set_ylabel('Decoding time (ms)', labelpad=10)
    # Add legend to plot
    ax.legend(bbox_to_anchor=(1, 1), loc=1, frameon=False, fontsize=16)
    ax2.legend(bbox_to_anchor=(1, 1), loc=1, frameon=False, fontsize=16)

    # Add the x and y-axis labels
    ax2.set_xlabel('#frame', labelpad=10)
    ax2.set_ylabel('Compression Quality', labelpad=10)



    # Save figure
    plt.savefig(outfile, dpi=300, transparent=False, bbox_inches='tight')

    plt.show()


###############################################################################################
def createCompressionPlot(data, methods, useResidual =  False, outfile = '', showOverlays = False):
    
    dataPNG = data[(data.iloc[:,2] == methods[0])]

    dataZIP = data[(data.iloc[:,2] == methods[1])]

    dataZSTD = data[(data.iloc[:,2] == methods[2])]

    # Generate 2 colors from the 'tab10' colormap
    colors = cm.get_cmap('tab10', 10)
    # Create figure and add axes object
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 6))
       

    # Plot and show our data
    # Without residual
    if (not useResidual):
        ax.plot(dataPNG.iloc[:, 1],  dataPNG.iloc[:, 4], label =methods[0], color = colors(0))
        ax.plot(dataZIP.iloc[:, 1], dataZIP.iloc[:, 4], label =methods[1], color = colors(1))
        ax.plot(dataZSTD.iloc[:,1], dataZSTD.iloc[:,4] , label =methods[2], color = colors(3))


        ax2.plot(dataPNG.iloc[:, 1], dataPNG.iloc[:, 6], label =methods[0], color = colors(0))
        ax2.plot(dataZIP.iloc[:, 1], dataZIP.iloc[:, 6], label =methods[1], color = colors(1))
        ax2.plot(dataZSTD.iloc[:,1], dataZSTD.iloc[:,6] , label =methods[2], color = colors(3))
    else:
        ax.plot(dataPNG.iloc[:, 1], dataPNG.iloc[:, 4]+dataPNG.iloc[:, 5], label =methods[0], color = colors(0))
        ax.plot(dataZIP.iloc[:, 1], dataZIP.iloc[:, 4]+dataZIP.iloc[:, 5], label =methods[1], color = colors(1))
        ax.plot(dataZSTD.iloc[:,1], dataZSTD.iloc[:,4]+dataZSTD.iloc[:, 5] , label =methods[2], color = colors(3))


        ax2.plot(dataPNG.iloc[:, 1], dataPNG.iloc[:, 6]+dataPNG.iloc[:, 7], label =methods[0], color = colors(0))
        ax2.plot(dataZIP.iloc[:, 1], dataZIP.iloc[:, 6]+dataZIP.iloc[:, 7], label =methods[1], color = colors(1))
        ax2.plot(dataZSTD.iloc[:,1], dataZSTD.iloc[:,6]+dataZSTD.iloc[:, 7] , label =methods[2], color = colors(3))


    # Edit the major and minor ticks of the x and y axes
    ax.xaxis.set_tick_params(which='major', size=10, width=2, direction='in', top='on')
    ax.xaxis.set_tick_params(which='minor', size=7, width=2, direction='in', top='on')
    ax.yaxis.set_tick_params(which='major', size=10, width=2, direction='in', right='on')
    ax.yaxis.set_tick_params(which='minor', size=7, width=2, direction='in', right='on')
    # Add the x and y-axis labels
    ax.set_xlabel('#frame', labelpad=10)
    ax.set_ylabel('Processing time (ms)', labelpad=10)
    # Add legend to plot
    ax.legend(bbox_to_anchor=(1, 1), loc=1, frameon=False, fontsize=16)
    ax2.legend(bbox_to_anchor=(1, 1), loc=1, frameon=False, fontsize=16)

    # Add the x and y-axis labels
    ax2.set_xlabel('#frame', labelpad=10)
    ax2.set_ylabel('CompressionRate', labelpad=10)

    # Save figure
    plt.savefig(outfile, dpi=300, transparent=False, bbox_inches='tight')

    plt.show()


def createCompressionTable(inputDir, useResidual):
    
    headers_Table1 = ['Image', '#Planes', 'FIT C Time', 'FIT Rate' , 'JPG C Time', 'JPG Rate', 'MP4 C Time', 'MP4 Rate']
    rows_Table1 = []
    rows_Table1.append(headers_Table1)
    

    headers_Table2 = ['Image', 'Planes', 'FIT D Time', 'FIT PSNR' , 'JPG D Time', 'JPG PSNR', 'MP4 D Time', 'MP4 PSNR']
    rows_Table2 = []
    rows_Table2.append(headers_Table2)

    for i in range(1,10):
        ##TABLE COMPRESSION
        data = pd.read_csv(inputDir + str(i)+"/metricsCompression.csv", delimiter = ';')
        
        datacFIT = data[(data.iloc[:,2] == "FIT")]
        datacJPG = data[(data.iloc[:,2] == "JPG")]
        datacMP4 = data[(data.iloc[:,2] == "MP4")]
        
        if useResidual:
            avgcFIT = datacFIT.iloc[:, 4].mean() + datacFIT.iloc[:, 5].mean()
            avgrFIT = datacFIT.iloc[:, 6].mean() + datacFIT.iloc[:, 7].mean()

            avgcJPG = datacJPG.iloc[:, 4].mean() + datacJPG.iloc[:, 5].mean()
            avgrJPG = datacJPG.iloc[:, 6].mean() + datacJPG.iloc[:, 7].mean()
    
            avgcMP4 = datacMP4.iloc[:, 4].mean() + datacMP4.iloc[:, 5].mean()
            avgrMP4 = datacMP4.iloc[:, 6].mean() + datacMP4.iloc[:, 7].mean()
        else:
            avgcFIT = datacFIT.iloc[:, 4].mean() 
            avgrFIT = datacFIT.iloc[:, 6].mean() 

            avgcJPG = datacJPG.iloc[:, 4].mean() 
            avgrJPG = datacJPG.iloc[:, 6].mean() 
    
            avgcMP4 = datacMP4.iloc[:, 4].mean() 
            avgrMP4 = datacMP4.iloc[:, 6].mean() 

        rows_Table1.append([str(i), datacFIT.iloc[:, 1].count(), avgcFIT, avgrFIT, avgcJPG,avgrJPG,avgcMP4, avgrMP4])
        
        #TABLE DECOMPRESSION
        dataDec = pd.read_csv(inputDir + str(i)+ "/metricsDecompression.csv", delimiter = ';')
        datadFIT = dataDec[(data.iloc[:,2] == "FIT")]
        datadJPG = dataDec[(data.iloc[:,2] == "JPG")]
        datadMP4 = dataDec[(data.iloc[:, 2] == "MP4")]
        
        avgdFIT = datadFIT.iloc[:, 4].mean()
        if useResidual:
            avgqFIT = datadFIT.iloc[:, 5].mean()
        else:
            avgqFIT = datadFIT.iloc[:, 6].mean()

        avgdJPG = datadJPG.iloc[:, 4].mean()
        if useResidual:
            avgqJPG = datadJPG.iloc[:, 5].mean()
        else:
            avgqJPG = datadJPG.iloc[:, 6].mean()

        avgdMP4 = datadMP4.iloc[:, 4].mean()
        if useResidual:
            avgqMP4 = datadMP4.iloc[:, 5].mean()
        else:
            avgqMP4 = datadMP4.iloc[:, 6].mean()

        rows_Table2.append([str(i), datadFIT.iloc[:, 1].count(), avgdFIT, avgqFIT, avgdJPG,avgqJPG,avgdMP4, avgqMP4])
        

       # print(rows_Table2)
    
    table1 = Texttable()
    table1.set_cols_align(["c"] * 8)
    table1.set_deco(Texttable.HEADER | Texttable.VLINES)
    table1.add_rows(rows_Table1)

    print('\nTexttable Latex:')
    print(latextable.draw_latex(table1, caption="Compression metrics."))


    table2 = Texttable()
    table2.set_cols_align(["c"] * 8)
    table2.set_deco(Texttable.HEADER | Texttable.VLINES)
    table2.add_rows(rows_Table2)

    print('\nTexttable Latex:')
    print(latextable.draw_latex(table2, caption="Deompression metrics."))
   

################################
def createImagesPlot():
    
    if not os.path.exists('./paper/frame_0001.jpg'):
        return
        
    #The OffsetBox is a simple container artist.
    imgs = [image.imread('./paper/frame_0001.jpg'),
            image.imread('./paper/frame_0150.jpg'),
            image.imread('./paper/frame_0298.jpg')]

##    plt.figure(figsize=(12,4)) # specifying the overall grid size

    fig, axs = plt.subplots(1, 3, constrained_layout=True)
    axs[0].imshow(imgs[0])
    axs[0].set_title('Plane 0')
    axs[1].imshow(imgs[1])
    axs[1].set_title('Plane 150')
    axs[2].imshow(imgs[2])
    axs[2].set_title('Plane 290')

    plt.savefig('./paper/fig_planes.png', dpi=300, transparent=False, bbox_inches='tight')

    plt.show()

###############################################
## MAIN
inputDir = './DICOM/'
formatsLossy = ['fit', 'jpg', 'mp4']

formatsLossless = ['png', 'zip', 'zstd']

# columns compression
 # 0:index , 1:method, 2:operation, 3:elapsedEncodetime, 4:elapsedResidualTime,5: compressionRateNormal, 6:compressionRateWithResidual
data = pd.read_csv(inputDir + "1/metricsCompression.csv", delimiter = ';')

dataDec = pd.read_csv(inputDir + "1/metricsDecompression.csv", delimiter = ';')

print(data.head())


print(dataDec.head())


createCompressionTable(inputDir, False)



createImagesPlot()


createDeCompressionPlot(dataDec, ("JPG", "FIT", "MP4"), './paper/fig_decompresion.png', False)

# compression plot . With residual and without

createCompressionPlot(data, ("PNG", "ZIP", "ZSTD"), True,'./paper/fig_plot_lossless_time.png' )

createCompressionPlot(data, ("JPG", "FIT", "MP4"), False,'./paper/fig_plot_lossy_time.png' )

createCompressionPlot(data, ("JPG", "FIT", "MP4"), True,'./paper/fig_plot_lossy_time_residual.png' , True)



