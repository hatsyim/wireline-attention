import torch
import numpy as np

class SSDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings
    def __getitem__(self, idx):
        return {key: val[idx].clone().detach() for key, val in self.encodings.items()}
    def __len__(self):
        return len(self.encodings['inputs_embeds'])
def plot_wirelines(df1, df2=None, label1=None, label2=None):
    fig, ax = plt.subplots(figsize=(15,8))#Set up the plot axes
    ax1 = plt.subplot2grid((1,7), (0,0), rowspan=1, colspan = 1)
    ax2 = plt.subplot2grid((1,7), (0,1), rowspan=1, colspan = 1, sharey = ax1)
    ax3 = plt.subplot2grid((1,7), (0,2), rowspan=1, colspan = 1, sharey = ax1)
    ax4 = plt.subplot2grid((1,7), (0,3), rowspan=1, colspan = 1, sharey = ax1)
    ax5 = ax3.twiny() 
    ax7 = plt.subplot2grid((1,7), (0,5), rowspan=1, colspan = 1, sharey = ax1)
    # ax8 = plt.subplot2grid((1,7), (0,6), rowspan=1, colspan = 1, sharey = ax1)

    #Twins the y-axis for the density track with the neutron track
    ax6 = plt.subplot2grid((1,7), (0,4), rowspan=1, colspan = 1, sharey = ax1)

    # As our curve scales will be detached from the top of the track,
    # this code adds the top border back in without dealing with splines
    ax10 = ax1.twiny()
    ax10.xaxis.set_visible(False)
    ax11 = ax2.twiny()
    ax11.xaxis.set_visible(False)
    ax12 = ax3.twiny()
    ax12.xaxis.set_visible(False)
    ax13 = ax4.twiny()
    ax13.xaxis.set_visible(False)
    ax14 = ax6.twiny()
    ax14.xaxis.set_visible(False)
    ax15 = ax7.twiny()
    ax15.xaxis.set_visible(False)
    # ax16 = ax8.twiny()
    # ax16.xaxis.set_visible(False)

    # Gamma Ray track
    ax1.plot("GR", "DEPTH_MD", data=df1, color = "green", lw = 1.5, label=label1)
    ax1.set_xlabel("Gamma Ray [API]")
    ax1.xaxis.label.set_color("green")
    # ax1.set_xlim(0, 200)
    ax1.set_ylabel("Depth (m)")
    ax1.tick_params(axis='x', colors="green")
    ax1.spines["top"].set_edgecolor("green")
    ax1.title.set_color('green')
    if (df2 != None).all().values[0]:
        ax1.plot("GR", "DEPTH_MD", data=df2, color = "black", lw = 1.5, label=label2)
        ax1.legend()
    # ax1.set_xticks([0, 50, 100, 150, 200])

    # Resistivity track
    ax2.plot("RDEP", "DEPTH_MD", data=df1, color = "red", lw = 1.5, label=label1)
    ax2.set_xlabel("Resistivity - Deep [ohm.m]")
    # ax2.set_xlim(0.2, 2000)
    ax2.xaxis.label.set_color("red")
    ax2.tick_params(axis='x', colors="red")
    ax2.spines["top"].set_edgecolor("red")
    # ax2.set_xticks([0.1, 1, 10, 100, 1000])
    # ax2.semilogx()
    if (df2 != None).all().values[0]:
        ax2.plot("RDEP", "DEPTH_MD", data=df1, color = "black", lw = 1.5, label=label2)
        ax2.legend()

    # Density track
    ax3.plot("RHOB", "DEPTH_MD", data=df1, color = "red", lw = 1.5, label=label1)
    ax3.set_xlabel("Density [g/cc]")
    # ax3.set_xlim(1.95, 2.95)
    ax3.xaxis.label.set_color("red")
    ax3.tick_params(axis='x', colors="red")
    ax3.spines["top"].set_edgecolor("red")
    if (df2 != None).all().values[0]:
        ax3.plot("RHOB", "DEPTH_MD", data=df1, color = "black", lw = 1.5, label=label2)
    # ax3.set_xticks([1.95, 2.45, 2.95])

    # Sonic track
    ax4.plot("DTC", "DEPTH_MD", data=df1, color = "purple", lw = 1.5, label=label1)
    ax4.set_xlabel("Sonic - Compressional [us/ft]")
    # ax4.set_xlim(140, 40)
    ax4.xaxis.label.set_color("purple")
    ax4.tick_params(axis='x', colors="purple")
    ax4.spines["top"].set_edgecolor("purple")
    if (df2 != None).all().values[0]:
        ax4.plot("DTC", "DEPTH_MD", data=df1, color = "black", lw = 1.5, label=label2)
        ax4.legend()

    # Neutron track placed ontop of density track
    ax5.plot("NPHI", "DEPTH_MD", data=df1, color = "blue", lw = 1.5, label=label1)
    ax5.set_xlabel('Neutron [pu]')
    ax5.xaxis.label.set_color("blue")
    # ax5.set_xlim(.5, 0)
    ax5.tick_params(axis='x', colors="blue")
    ax5.spines["top"].set_position(("axes", 1.1))
    ax5.spines["top"].set_visible(True)
    ax5.spines["top"].set_edgecolor("blue")
    if (df2 != None).all().values[0]:
        ax5.plot("NPHI", "DEPTH_MD", data=df1, color = "black", lw = 1.5, label=label2)
        ax5.legend()        
    # ax5.set_xticks([45,  15, -15])

    # Caliper track
    ax6.plot("CALI", "DEPTH_MD", data=df1, color = "orange", lw = 1.5, label=label1)
    ax6.set_xlabel("Caliper [inch]")
    # ax6.set_xlim(8, 10)
    ax6.xaxis.label.set_color("orange")
    ax6.tick_params(axis='x', colors="orange")
    ax6.spines["top"].set_edgecolor("orange")
    if (df2 != None).all().values[0]:
        ax6.plot("CALI", "DEPTH_MD", data=df1, color = "black", lw = 1.5, label=label2)
        ax6.legend()
    # ax6.fill_betweenx(well_nan.index, 8.5, well["CALI"], facecolor='yellow')
    # ax6.set_xticks([6,  11, 16])

    # Shear track
    ax7.plot("PEF", "DEPTH_MD", data=df1, color = "magenta", lw = 1.5, label=label1)
    ax7.set_xlabel("Photoelectric [API]")
    # ax4.set_xlim(140, 40)
    ax7.xaxis.label.set_color("purple")
    ax7.tick_params(axis='x', colors="magenta")
    ax7.spines["top"].set_edgecolor("magenta")
    if (df2 != None).all().values[0]:
        ax7.plot("PEF", "DEPTH_MD", data=df1, color = "black", lw = 1.5, label=label2)
        ax7.legend()

    # # Shear track
    # ax4.plot("DTC", "DEPTH_MD", data=df1, color = "purple", lw = 1.5, label=label1)
    # ax4.set_xlabel("Sonic - Compressional [us/ft]")
    # # ax4.set_xlim(140, 40)
    # ax4.xaxis.label.set_color("purple")
    # ax4.tick_params(axis='x', colors="purple")
    # ax4.spines["top"].set_edgecolor("purple")
    # if (df2 != None).all().values[0]:
    #     ax4.plot("DTC", "DEPTH_MD", data=df1, color = "black", lw = 1.5, label=label2)
    #     ax4.legend()

    # Common functions for setting up the plot can be extracted into
    # a for loop. This saves repeating code.
    for ax in [ax1, ax2, ax3, ax4, ax6, ax7]:
        # ax.set_ylim(4500, 3500)
        ax.grid(which='major', color='lightgrey', linestyle='-')
        ax.xaxis.set_ticks_position("top")
        ax.xaxis.set_label_position("top")
        ax.spines["top"].set_position(("axes", 1.02))
        
    for ax in [ax2, ax3, ax4, ax6, ax7]:
        plt.setp(ax.get_yticklabels(), visible = False)
        
    plt.tight_layout()
    fig.subplots_adjust(wspace = 0.15)
    # plt.show()

# Wrap in PyTorch dataset
class WirelineDataset(torch.utils.data.Dataset):
    def __init__(self, data, seq_len, pred_type='DTS'):
        self.data = data
        self.seq_len = seq_len
        self.pred_type = pred_type
    def __getitem__(self, idx):

        well = np.unique(self.data.WELL.values[idx*self.seq_len:(idx+1)*self.seq_len])[0]
        if self.pred_type=='DTS':
            data = self.data.drop(columns=['DTS','Type']).values[idx*self.seq_len:(idx+1)*self.seq_len]
            label = self.data['DTS'].values[idx*self.seq_len:(idx+1)*self.seq_len].reshape(-1,1)
        elif self.pred_type=='FACIES':
            data = self.data.drop(columns=['FORCE_2020_LITHOFACIES_LITHOLOGY']).values[idx*self.seq_len:(idx+1)*self.seq_len]
            label = self.data['FORCE_2020_LITHOFACIES_LITHOLOGY'].values[idx*self.seq_len:(idx+1)*self.seq_len].reshape(-1,1)

        wells = {'well': well, 'data': data, 'label':label}

        return wells
    def __len__(self):
        return int(len(self.data)/self.seq_len)

def plot_wirelines_dts(df1, df2=None, label1=None, label2=None):
    fig, ax = plt.subplots(figsize=(15,8))#Set up the plot axes
    ax1 = plt.subplot2grid((1,8), (0,0), rowspan=1, colspan = 1)
    ax2 = plt.subplot2grid((1,8), (0,1), rowspan=1, colspan = 1, sharey = ax1)
    ax3 = plt.subplot2grid((1,8), (0,2), rowspan=1, colspan = 1, sharey = ax1)
    ax4 = plt.subplot2grid((1,8), (0,3), rowspan=1, colspan = 1, sharey = ax1)
    ax5 = ax3.twiny() 
    ax7 = plt.subplot2grid((1,8), (0,5), rowspan=1, colspan = 1, sharey = ax1)
    ax8 = plt.subplot2grid((1,8), (0,6), rowspan=1, colspan = 1, sharey = ax1)

    #Twins the y-axis for the density track with the neutron track
    ax6 = plt.subplot2grid((1,8), (0,4), rowspan=1, colspan = 1, sharey = ax1)

    # As our curve scales will be detached from the top of the track,
    # this code adds the top border back in without dealing with splines
    ax10 = ax1.twiny()
    ax10.xaxis.set_visible(False)
    ax11 = ax2.twiny()
    ax11.xaxis.set_visible(False)
    ax12 = ax3.twiny()
    ax12.xaxis.set_visible(False)
    ax13 = ax4.twiny()
    ax13.xaxis.set_visible(False)
    ax14 = ax6.twiny()
    ax14.xaxis.set_visible(False)
    ax15 = ax7.twiny()
    ax15.xaxis.set_visible(False)
    ax16 = ax8.twiny()
    ax16.xaxis.set_visible(False)

    # Gamma Ray track
    ax1.plot("GR", "DEPTH_MD", data=df1, color = "green", lw = 1.5, label=label1)
    ax1.set_xlabel("Gamma Ray [API]")
    ax1.xaxis.label.set_color("green")
    # ax1.set_xlim(0, 200)
    ax1.set_ylabel("Depth (m)")
    ax1.tick_params(axis='x', colors="green")
    ax1.spines["top"].set_edgecolor("green")
    ax1.title.set_color('green')
    # ax1.set_xticks([0, 50, 100, 150, 200])

    # Resistivity track
    ax2.plot("RDEP", "DEPTH_MD", data=df1, color = "red", lw = 1.5, label=label1)
    ax2.set_xlabel("Resistivity - Deep [ohm.m]")
    # ax2.set_xlim(0.2, 2000)
    ax2.xaxis.label.set_color("red")
    ax2.tick_params(axis='x', colors="red")
    ax2.spines["top"].set_edgecolor("red")
    # ax2.set_xticks([0.1, 1, 10, 100, 1000])
    # ax2.semilogx()

    # Density track
    ax3.plot("RHOB", "DEPTH_MD", data=df1, color = "red", lw = 1.5, label=label1)
    ax3.set_xlabel("Density [g/cc]")
    # ax3.set_xlim(1.95, 2.95)
    ax3.xaxis.label.set_color("red")
    ax3.tick_params(axis='x', colors="red")
    ax3.spines["top"].set_edgecolor("red")
    # ax3.set_xticks([1.95, 2.45, 2.95])

    # Sonic track
    ax4.plot("DTC", "DEPTH_MD", data=df1, color = "purple", lw = 1.5, label=label1)
    ax4.set_xlabel("Sonic - Compressional [us/ft]")
    # ax4.set_xlim(140, 40)
    ax4.xaxis.label.set_color("purple")
    ax4.tick_params(axis='x', colors="purple")
    ax4.spines["top"].set_edgecolor("purple")

    # Neutron track placed ontop of density track
    ax5.plot("NPHI", "DEPTH_MD", data=df1, color = "blue", lw = 1.5, label=label1)
    ax5.set_xlabel('Neutron [pu]')
    ax5.xaxis.label.set_color("blue")
    # ax5.set_xlim(.5, 0)
    ax5.tick_params(axis='x', colors="blue")
    ax5.spines["top"].set_position(("axes", 1.1))
    ax5.spines["top"].set_visible(True)
    ax5.spines["top"].set_edgecolor("blue")   
    # ax5.set_xticks([45,  15, -15])

    # Caliper track
    ax6.plot("CALI", "DEPTH_MD", data=df1, color = "orange", lw = 1.5, label=label1)
    ax6.set_xlabel("Caliper [inch]")
    # ax6.set_xlim(8, 10)
    ax6.xaxis.label.set_color("orange")
    ax6.tick_params(axis='x', colors="orange")
    ax6.spines["top"].set_edgecolor("orange")
    # ax6.fill_betweenx(well_nan.index, 8.5, well["CALI"], facecolor='yellow')
    # ax6.set_xticks([6,  11, 16])

    # Shear track
    ax7.plot("PEF", "DEPTH_MD", data=df1, color = "magenta", lw = 1.5, label=label1)
    ax7.set_xlabel("Photoelectric [API]")
    # ax4.set_xlim(140, 40)
    ax7.xaxis.label.set_color("purple")
    ax7.tick_params(axis='x', colors="magenta")
    ax7.spines["top"].set_edgecolor("magenta")

    # Shear track
    ax8.plot("DTS", "DEPTH_MD", data=df1, color = "purple", lw = 1.5, label=label1)
    ax8.set_xlabel("Sonic - Shear [us/ft]")
    # ax4.set_xlim(140, 40)
    ax8.xaxis.label.set_color("purple")
    ax8.tick_params(axis='x', colors="purple")
    ax8.spines["top"].set_edgecolor("purple")
    # if (df2 != None).all().values[0]:
    #     ax8.plot("DTS", "DEPTH_MD", data=df2, color = "orange", lw = 1.5, label=label2)
    #     ax8.legend()

    # Common functions for setting up the plot can be extracted into
    # a for loop. This saves repeating code.
    for ax in [ax1, ax2, ax3, ax4, ax6, ax7, ax8]:
        # ax.set_ylim(4500, 3500)
        ax.grid(which='major', color='lightgrey', linestyle='-')
        ax.xaxis.set_ticks_position("top")
        ax.xaxis.set_label_position("top")
        ax.spines["top"].set_position(("axes", 1.02))
        
    for ax in [ax2, ax3, ax4, ax6, ax7, ax8]:
        plt.setp(ax.get_yticklabels(), visible = False)
        
    plt.tight_layout()
    fig.subplots_adjust(wspace = 0.15)
    # plt.show()

def plot_wirelines_facies(df1, df2=None, label1=None, label2=None):
    fig, ax = plt.subplots(figsize=(15,8))#Set up the plot axes
    ax1 = plt.subplot2grid((1,8), (0,0), rowspan=1, colspan = 1)
    ax2 = plt.subplot2grid((1,8), (0,1), rowspan=1, colspan = 1, sharey = ax1)
    ax3 = plt.subplot2grid((1,8), (0,2), rowspan=1, colspan = 1, sharey = ax1)
    ax4 = plt.subplot2grid((1,8), (0,3), rowspan=1, colspan = 1, sharey = ax1)
    ax5 = ax3.twiny() 
    ax7 = plt.subplot2grid((1,8), (0,5), rowspan=1, colspan = 1, sharey = ax1)
    ax8 = plt.subplot2grid((1,8), (0,6), rowspan=1, colspan = 1, sharey = ax1)
    ax9 = plt.subplot2grid((1,8), (0,7), rowspan=1, colspan = 1, sharey = ax1)

    #Twins the y-axis for the density track with the neutron track
    ax6 = plt.subplot2grid((1,8), (0,4), rowspan=1, colspan = 1, sharey = ax1)

    # As our curve scales will be detached from the top of the track,
    # this code adds the top border back in without dealing with splines
    ax10 = ax1.twiny()
    ax10.xaxis.set_visible(False)
    ax11 = ax2.twiny()
    ax11.xaxis.set_visible(False)
    ax12 = ax3.twiny()
    ax12.xaxis.set_visible(False)
    ax13 = ax4.twiny()
    ax13.xaxis.set_visible(False)
    ax14 = ax6.twiny()
    ax14.xaxis.set_visible(False)
    ax15 = ax7.twiny()
    ax15.xaxis.set_visible(False)
    ax16 = ax8.twiny()
    ax16.xaxis.set_visible(False)
    ax17 = ax9.twiny()
    ax17.xaxis.set_visible(False)

    # Gamma Ray track
    ax1.plot("GR", "DEPTH_MD", data=df1, color = "green", lw = 1.5, label=label1)
    ax1.set_xlabel("Gamma Ray [API]")
    ax1.xaxis.label.set_color("green")
    # ax1.set_xlim(0, 200)
    ax1.set_ylabel("Depth (m)")
    ax1.tick_params(axis='x', colors="green")
    ax1.spines["top"].set_edgecolor("green")
    ax1.title.set_color('green')
    # ax1.set_xticks([0, 50, 100, 150, 200])

    # Resistivity track
    ax2.plot("RDEP", "DEPTH_MD", data=df1, color = "red", lw = 1.5, label=label1)
    ax2.set_xlabel("Resistivity - Deep [ohm.m]")
    # ax2.set_xlim(0.2, 2000)
    ax2.xaxis.label.set_color("red")
    ax2.tick_params(axis='x', colors="red")
    ax2.spines["top"].set_edgecolor("red")
    # ax2.set_xticks([0.1, 1, 10, 100, 1000])
    # ax2.semilogx()

    # Density track
    ax3.plot("RHOB", "DEPTH_MD", data=df1, color = "red", lw = 1.5, label=label1)
    ax3.set_xlabel("Density [g/cc]")
    # ax3.set_xlim(1.95, 2.95)
    ax3.xaxis.label.set_color("red")
    ax3.tick_params(axis='x', colors="red")
    ax3.spines["top"].set_edgecolor("red")
    # ax3.set_xticks([1.95, 2.45, 2.95])

    # Sonic track
    ax4.plot("DTC", "DEPTH_MD", data=df1, color = "purple", lw = 1.5, label=label1)
    ax4.set_xlabel("Sonic - Compressional [us/ft]")
    # ax4.set_xlim(140, 40)
    ax4.xaxis.label.set_color("purple")
    ax4.tick_params(axis='x', colors="purple")
    ax4.spines["top"].set_edgecolor("purple")

    # Neutron track placed ontop of density track
    ax5.plot("NPHI", "DEPTH_MD", data=df1, color = "blue", lw = 1.5, label=label1)
    ax5.set_xlabel('Neutron [pu]')
    ax5.xaxis.label.set_color("blue")
    # ax5.set_xlim(.5, 0)
    ax5.tick_params(axis='x', colors="blue")
    ax5.spines["top"].set_position(("axes", 1.1))
    ax5.spines["top"].set_visible(True)
    ax5.spines["top"].set_edgecolor("blue")   
    # ax5.set_xticks([45,  15, -15])

    # Caliper track
    ax6.plot("CALI", "DEPTH_MD", data=df1, color = "orange", lw = 1.5, label=label1)
    ax6.set_xlabel("Caliper [inch]")
    # ax6.set_xlim(8, 10)
    ax6.xaxis.label.set_color("orange")
    ax6.tick_params(axis='x', colors="orange")
    ax6.spines["top"].set_edgecolor("orange")
    # ax6.fill_betweenx(well_nan.index, 8.5, well["CALI"], facecolor='yellow')
    # ax6.set_xticks([6,  11, 16])

    # Shear track
    ax7.plot("PEF", "DEPTH_MD", data=df1, color = "magenta", lw = 1.5, label=label1)
    ax7.set_xlabel("Photoelectric [API]")
    # ax4.set_xlim(140, 40)
    ax7.xaxis.label.set_color("purple")
    ax7.tick_params(axis='x', colors="magenta")
    ax7.spines["top"].set_edgecolor("magenta")

    # Lithology track
    ax8.plot("FACIES", 'DEPTH_MD', data=df1, color = "black", lw = 1.5)
    ax8.set_xlabel("Lithology")
    ax8.set_xlim(0, 1)
    ax8.xaxis.label.set_color("black")
    ax8.tick_params(axis='x', colors="black")
    ax8.spines["top"].set_edgecolor("black")

    for key in lithology_numbers.keys():
        color = lithology_numbers[key]['color']
        # hatch = lithology_numbers[key]['hatch']
        ax8.fill_betweenx(df1['DEPTH_MD'], 0, df1['FACIES'], where=(df1['FACIES']==key), facecolor=color)

    # Lithology track
    ax9.plot("FACIES", 'DEPTH_MD', data=df2, color = "black", lw = 1.5)
    ax9.set_xlabel("Lithology")
    ax9.set_xlim(0, 1)
    ax9.xaxis.label.set_color("black")
    ax9.tick_params(axis='x', colors="black")
    ax9.spines["top"].set_edgecolor("black")

    for key in lithology_numbers.keys():
        color = lithology_numbers[key]['color']
        # hatch = lithology_numbers[key]['hatch']
        ax9.fill_betweenx(df2['DEPTH_MD'], 0, df2['FACIES'], where=(df2['FACIES']==key), facecolor=color)

    # Common functions for setting up the plot can be extracted into
    # a for loop. This saves repeating code.
    for ax in [ax1, ax2, ax3, ax4, ax6, ax7, ax8, ax9]:
        # ax.set_ylim(4500, 3500)
        ax.grid(which='major', color='lightgrey', linestyle='-')
        ax.xaxis.set_ticks_position("top")
        ax.xaxis.set_label_position("top")
        ax.spines["top"].set_position(("axes", 1.02))
        
    for ax in [ax2, ax3, ax4, ax6, ax7, ax8, ax9]:
        plt.setp(ax.get_yticklabels(), visible = False)
        
    plt.tight_layout()
    fig.subplots_adjust(wspace = 0.15)
    # plt.show()

# Wrap in PyTorch dataset
class WirelineDataset(torch.utils.data.Dataset):
    def __init__(self, data, seq_len, pred_type='DTS'):
        self.data = data
        self.seq_len = seq_len
        self.pred_type = pred_type
    def __getitem__(self, idx):

        well = np.unique(self.data.WELL.values[idx*self.seq_len:(idx+1)*self.seq_len])[0]
        if self.pred_type=='DTS':
            data = self.data.drop(columns=['DTS','Type']).values[idx*self.seq_len:(idx+1)*self.seq_len]
            label = self.data['DTS'].values[idx*self.seq_len:(idx+1)*self.seq_len].reshape(-1,1)
        elif self.pred_type=='FACIES':
            data = self.data.drop(columns=['FORCE_2020_LITHOFACIES_LITHOLOGY']).values[idx*self.seq_len:(idx+1)*self.seq_len]
            label = self.data['FORCE_2020_LITHOFACIES_LITHOLOGY'].values[idx*self.seq_len:(idx+1)*self.seq_len].reshape(-1,1)

        wells = {'well': well, 'data': data, 'label':label}

        return wells
    def __len__(self):
        return int(len(self.data)/self.seq_len)