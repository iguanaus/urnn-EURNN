#This file exports a saved file from my version into the version for Li.
#The only thing is I still need to figure out the parameter count.
#We are going to just put ~6500, cause screw it.
import cPickle
import numpy as np

T = 1000
batch_size=128

def exportFile(filename,histfile,title,task):
	beginning_string='########\n\n\tModel: '+str(title)+'\n\n#Task:\n '+str(task)+'\n\n########'

	try:
	    history=cPickle.load(open(histfile,'rb'))
	except:
	    print ("Can't open file",histfile,"skipping exp:",filename)
	train_loss=np.asarray(history['train_loss'])
	xval=np.arange(train_loss.shape[0])
	xtrain = np.array(range(0,len(train_loss)))*batch_size
	#x is xtrain, y is train_loss

	with open(filename,'w') as f:
		f.write(beginning_string)
		f.write('\n\n');
		for i in xrange(0,len(train_loss)):
			if str(train_loss[i]) == 'nan':
				continue
			else:
				f.write(str(xtrain[i])+"	" + str(train_loss[i]) + "\n")


direc='exp/'


filename = "exp/EURNN_T="+str(T)+"_.txt"
histfile = direc+"memory_problem_EURNN_adhoc_EURNN_nhidden512_t"+str(T)

title="EURNN, N=512, L=2"
task="# Copying Task with T="+str(T)
exportFile(filename,histfile,title,task)
