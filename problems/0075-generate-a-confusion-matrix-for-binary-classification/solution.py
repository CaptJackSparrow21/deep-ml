from collections import Counter

def confusion_matrix(data):
	TP = FN = FP = TN = 0

	for actual, predicted in data :
		if actual == 1 and predicted == 1 :
			TP += 1

		elif actual == 1 and predicted == 0 :
			FN += 1

		elif actual == 0 and predicted == 1 :
			FP += 1
		
		elif actual == 0 and predicted == 0 :
			TN += 1

	return [[TP, FN], [FP, TN]]
	
