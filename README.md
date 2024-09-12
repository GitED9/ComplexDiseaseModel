# ComplexDiseaseModel
This repo includes the code used for the analysis done for the paper 'Using machine learning to predict and analyze complex trait diseases: lessons from an abstract model'

1. ReplaceNAinRealData.py -> contains the code used to replace NA values in the data as described in the Method section under 'Creating the dataset'.
2. RectangleShuffeling.py -> the code used to shuffle the daata using the rectangle shuffeling method described in the the Method section under 
                             'Creating the dataset' subsection 'Extanding the core data'.
3. FilterHealthyOrSickFromShuffledData.py -> This script filtered out all the sick or the healthy from a file. Originaly created to filter out the 
                              healthy created by shuffeling the sick real data and vise versa.
4. DiseaseModel.py -> This class alows to create a complex and simple disease models. To get a Simple model, set all the weights to 1.
5. DeleteSNPS.py ->  This script gets as input a file with correct labels according to some model and number of SNPs to be deleted and then it 
                     deletes them and leaves the genome with the original label. It's done to try and see how the algorithms deals with lack of data.
6. CreateHistograms.py -> This script is used to create a histogram of # of 0/1/2 per sick/healthy groups + printing statistics.
7. AddNoiseSNP.py -> This script gets as input a file with correct labels according to some model and number of SNPs to be added and then it adds them and leave the same labels. It's done to try and see how the algorithms deals with noise data.
8. case_48 -> 48 alleles with the least NaN values of the original data for cases of Crohn's disease
9. control_48 -> 48 alleles with the least NaN values of the original data for control cases
