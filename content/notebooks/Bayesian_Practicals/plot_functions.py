import seaborn as sns
import scipy.integrate as integrate
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib.cm as cm


sbcolorcyclebright=sns.color_palette("bright")
sbcolorcycledark=sns.color_palette("dark")
sbcolorcyclemuted=sns.color_palette("muted")
sns.set_style("ticks") # Set plot properties
sns.set_context("talk")
sns.despine()

iconditionlist = ['1','2']

def plot_experimental_trajectories():

    fig_height = 8
    #plot_aspect_ratio = 2.0/len(iconditionlist)
    plot_aspect_ratio = 1.2
    fig = plt.figure(figsize=(fig_height * plot_aspect_ratio, fig_height))

    rows = 2
    gs = gridspec.GridSpec(rows, 2)
    axlist = [[0,0] for n in range(rows)]

    for iicond,icond in enumerate(iconditionlist):
        fileAsep = np.loadtxt('data/A_sep_'+icond+'.dat') # file with WT separate culture
        fileBsep = np.loadtxt('data/B_sep_'+icond+'.dat') # file with mutant separate culture
        fileAcoc = np.loadtxt('data/A_coc_'+icond+'.dat') # file with coculture of mutant and WT
        fileBcoc = np.loadtxt('data/B_coc_'+icond+'.dat') # file with coculture of mutant and WT


        axlist[iicond][0]=plt.subplot(gs[iicond,0]) # separate
        axlist[iicond][1]=plt.subplot(gs[iicond,1]) # coculture

        axlist[iicond][0].plot(fileAsep[:,0],fileAsep[:,1]/1E5,'o', # 
            color = sbcolorcyclebright[0],label='A')
        axlist[iicond][0].plot(fileBsep[:,0],fileBsep[:,1]/1E5,'o', # 
            color = sbcolorcyclebright[1],label='B')

        axlist[iicond][1].plot(fileAcoc[:,0],fileAcoc[:,1]/1E5,'o', # 
            color = sbcolorcyclebright[0],label='A')
        axlist[iicond][1].plot(fileBcoc[:,0],fileBcoc[:,1]/1E5,'o', # 
            color = sbcolorcyclebright[1],label='B')

        plt.legend()

        axlist[iicond][0].set_title('$A_0$ = '+str(fileAsep[0,1]/1E5)+'$\\times 10^5$'+
            ',   $B_0$ = '+str(fileBsep[0,1]/1E5)+'$\\times 10^5$')

        axlist[iicond][1].set_title('$A_0$ = '+str(fileAcoc[0,1]/1E5)+'$\\times 10^5$'+
            ',   $B_0$ = '+str(fileBcoc[0,1]/1E5)+'$\\times 10^5$')

        axlist[iicond][0].set_xlabel("time (days)")
        axlist[iicond][1].set_xlabel("time (days)")
        axlist[iicond][0].set_ylabel("separate cells ($\\times 10^5$)") # This is the regularization constant
        axlist[iicond][1].set_ylabel("co-culture cells ($\\times 10^5$)") # This is the regularization constant

    plt.tight_layout()
    return axlist

def plot_ODEs(experimentalplot, rhs_ODEs,rhoA, rhoB,KAA, KBB, KAB, KBA):

    rhs_ODEs_tc = lambda t,c: rhs_ODEs(t,c,rhoA, rhoB,KAA, KBB, KAB, KBA)

    t_span = [0,4] # time range to integrate
    t_eval = np.linspace(0,4,100) # time points for the output

    for iicond,icond in enumerate(iconditionlist):
        fileAsep = np.loadtxt('data/A_sep_'+icond+'.dat') # file with WT separate culture
        fileBsep = np.loadtxt('data/B_sep_'+icond+'.dat') # file with mutant separate culture
        fileAcoc = np.loadtxt('data/A_coc_'+icond+'.dat') # file with coculture of mutant and WT
        fileBcoc = np.loadtxt('data/B_coc_'+icond+'.dat') # file with coculture of mutant and WT

        # prediction separate culture A
        init = [fileAsep[0,1]/1E5,0]
        trajectory = integrate.solve_ivp(rhs_ODEs_tc, t_span, init, t_eval = t_eval) ## Calling the solver
        experimentalplot[iicond][0].plot(trajectory.t,trajectory.y[0],color = sbcolorcyclebright[0])

        # prediction separate culture B
        init = [0,fileBsep[0,1]/1E5]
        trajectory = integrate.solve_ivp(rhs_ODEs_tc, t_span, init,t_eval = t_eval) ## Calling the solver
        experimentalplot[iicond][0].plot(trajectory.t,trajectory.y[1],color = sbcolorcyclebright[1])

        # prediction coculture
        init = [fileAcoc[0,1]/1E5,fileBcoc[0,1]/1E5]
        trajectory = integrate.solve_ivp(rhs_ODEs_tc, t_span, init,t_eval = t_eval) ## Calling the solver
        experimentalplot[iicond][1].plot(trajectory.t,trajectory.y[0],color = sbcolorcyclebright[0])
        experimentalplot[iicond][1].plot(trajectory.t,trajectory.y[1],color = sbcolorcyclebright[1])



        initcond = []

posterior = np.load('data/ABC_output.npy') # loading ABC-SMC results
likelihoods = np.load('data/Likelihoods.npy').flatten()


sorted_idxs = likelihoods.argsort() # Sorting datapoint by order of likelihood
posterior = posterior[sorted_idxs]
likelihoods = likelihoods[sorted_idxs]


def plot_marginal(par_name):

    pardict = {'rhoA':0, 'rhoB':1,'KAA':2, 'KBB':3, 'KAB':4, 'KBA':5} # Order of parameters in the file
    marginal_sample = posterior[:,pardict[par_name]]
    plt.hist(marginal_sample,histtype = 'stepfilled',
        color = sbcolorcyclemuted[4], edgecolor = sbcolorcycledark[4],
        density = True, bins = 100)
    plt.xlabel('$\\log_{10}$'+par_name)
    plt.ylabel('density')
    print('min:{},  max:{},  median:{}'.format(10**min(marginal_sample),10**max(marginal_sample),10**np.median(marginal_sample)))

def plot_joint(par_name1,par_name2):

    pardict = {'rhoA':0, 'rhoB':1,'KAA':2, 'KBB':3, 'KAB':4, 'KBA':5} # Order of parameters in the file
    plt.scatter(posterior[:,pardict[par_name1]], posterior[:,pardict[par_name2]], c = likelihoods,
              s = 2, cmap = 'viridis', vmin = likelihoods[1000], vmax = likelihoods[-1])
    cmap = cm.get_cmap('viridis')
    plt.gca().set_facecolor(cmap(0))
    plt.xlabel('$\\log_{10}$'+par_name1)
    plt.ylabel('$\\log_{10}$'+par_name2)


