# ---------------------------------------------------------------------------- #
# Title: Assignment 7
# Description: Description of a pickle
# ChangeLog (Who,When,What):
# MCLARK, 02.29.2021, created script
# ---------------------------------------------------------------------------- #

import pickle

# code a dictionary
dicSalmon = {"King": "30", "Chinook": "67", "Coho": "18", "Pink": "8.2", "Chum": "19", "Sockeye": "9.3"}
dicBear = {"Brown Bear": "250", "Black Bear": "150", "Polar Bear": "500"}

# pickle dictionary into binary format
file_P = open("pickledWeights.txt", "wb")
pickle.dump(dicSalmon, file_P)
file_P.close()

# unpickle dictionary list from binary to human readable format
fileUnpickle = open("pickledWeights.txt", "rb")
dicSalmonP = pickle.load(fileUnpickle)
fileUnpickle.close()

# print the dictionary
print(dicSalmonP)