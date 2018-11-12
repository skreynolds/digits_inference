#! /usr/bin/env python

import itertools
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix, accuracy_score

def plot_confusion_matrix(cm, classes,
						  normalise=False,
						  title='Confusion Matrix',
						  cmap=plt.cm.Blues):

	if normalise:
		cm = cm.astype('float') / cm.sum(axis=1)[:,np.newaxis]
		print("Normalised confusion matrix")
	else:
		print("Confusion matrix, without normalisation")

	print(cm)

	plt.imshow(cm, interpolation='nearest', cmap=cmap)
	plt.title(title)
	plt.colorbar()
	tick_marks = np.arange(len(classes))
	plt.xticks(tick_marks, classes, rotation=45)
	plt.yticks(tick_marks, classes)

	fmt = '.2f' if normalise else 'd'
	thresh = cm.max() / 2.
	for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
		plt.text(j, i, format(cm[i,j], fmt),
				 horizontalalignment="center",
				 color="white" if cm[i, j] > thresh else "black")

	plt.ylabel
	plt.xlabel
	plt.tight_layout()
	


if __name__ == '__main__':
	
	y_true = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
			  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
			  2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,]
	
	y_pred = [1, 2, 1, 0, 0, 2, 2, 1, 0, 0, 1, 1, 1, 0, 2,
			  1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1,
			  2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2]
	
	print(accuracy_score(y_true, y_pred))

	class_names = ['Clean', 'Soiled', 'No Solar Panel']

	cnf_matrix = confusion_matrix(y_true, y_pred)
	np.set_printoptions(precision=2)

	plt.figure()
	plot_confusion_matrix(cnf_matrix, classes=class_names,
						  title="Confusion Matrix, without Normalisation")

	plt.figure()
	plot_confusion_matrix(cnf_matrix, classes=class_names, normalise=True,
						  title='Normalised confusion matrix')

	plt.show()