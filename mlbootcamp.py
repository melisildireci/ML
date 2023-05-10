"""Problem Statement
You have been tasked with implementing a basic linear regression model using only Python core libraries. Your task is to write a function that takes in two lists, X and y, where X represents the features and y represents the target variable. Your function should return the slope (m) and intercept (b) that minimize the sum of squared errors (SSE) between the predicted and actual target values.

To implement the model, you can use the following steps:

Calculate the mean of X and y using a for loop
Calculate the variance of X using a for loop
Calculate the covariance between X and y using a for loop
Calculate the slope m using the formula: m = cov(X, y) / var(X)
Calculate the intercept b using the formula: b = mean(y) - m * mean(X)
To test the function, you can create sample data as follows:

X = [1, 2, 3, 4, 5]
y = [2.1, 3.9, 6.2, 8.1, 9.8]

m, b = linear_regression(X, y)

print(f"Slope (m): {m:.2f}")
print(f"Intercept (b): {b:.2f}")
The output should be:

Slope (m): 1.98
Intercept (b): 0.12
These values represent the slope
and intercept of the line that best fits the sample data, minimizing the sum of squared errors."""


def mean(values):
    """
    Calculate the mean of a list of values.

    Parameters:
    values (list): A list of numeric values.

    Returns:
    float: The mean value.
    """
    # YOUR CODE HERE
    total = 0.0   #The variable total is used to hold the total and is initialized to 0.0. float 
    for value in values:
        total += value #The for loop adds to the sum by traversing each value in the values list
    return total / len(values)
#len = Finds the length of the value values.
#(sum / len(values)) is calculated and returned.


sample_X = [1, 2, 3, 4, 5] #sample_X list
sample_y = [2.1, 3.9, 6.2, 8.1, 9.8] #sample_y list

meanX = mean(sample_X)
meany = mean(sample_y)
print(f"****Made by Melis İldireci****")
print(f"meanX=", meanX)  
print(f"meany=", meany) 




def variance(values):
  
  """
    Calculate the variance of a list of values.

    Parameters:
    values (list): A list of numeric values.

    Returns:
    float: The variance value.
    """
    # YOUR CODE HERE


  def mean(values):
        return sum(values) / len(values)
    #The mean() function is defined. This function will calculate the average of the given list of values.
  total = 0.0
  for value in values:
        total = total + (value - mean(values)) ** 2
  return total / len(values)
#The total variable is reset. Then, with the for loop, the list of values is traversed, 
#and the square of each element and the square of its difference from the mean are added to the sum.
# The variance is then calculated by dividing the sum by the length of the values list.

sample_X = [1, 2, 3, 4, 5]
sample_y = [2.1, 3.9, 6.2, 8.1, 9.8]
#round() function rounds each variance value to 2 decimal places
variance_X = round(variance(sample_X),2)
variance_y = round(variance(sample_y),2)

print(f"****Made by Melis İldireci****")
print("Sample_X varyansı: ", variance_X)
print("Sample_y varyansı: ", variance_y)

#"""various mean calculate
#n = len(values)
#mean= sum(values)/n
#But, total = total + (value - mean(values)) ** 2
#The variable mean(values) in this line of code will change to mean. It will give the same result.
#"""


def linear_regression(X, y):
    """
    Implement a basic linear regression model using Python core libraries.

    Parameters:
    X (list): A list of features.
    y (list): A list of target values.

    Returns:
    float: The slope (m) that minimizes the sum of squared errors.
    float: The intercept (b) that minimizes the sum of squared errors.
    """
    # YOUR CODE HERE
  
    n = len(X)
    #It was made with the help of the explanations and formulas given in the question.
    # Calculate the mean of X and y
    mean_x = sum(X) / n
    mean_y = sum(y) / n
    
    # Calculate the variance of X
    var_x = sum((xi - mean_x) ** 2 for xi in X) / (n - 1)
    
    # Calculate the covariance between X and y
    cov_xy = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(X, y)) / (n - 1)
    
    # Calculate the slope m
    m = cov_xy / var_x
    
    # Calculate the intercept b
    b = mean_y - m * mean_x
    
    return m, b
sample_X = [1, 2, 3, 4, 5]
sample_y = [2.1, 3.9, 6.2, 8.1, 9.8]

m, b = linear_regression(sample_X, sample_y)
print(f"****Made by Melis İldireci****")
print(f"Slope (m): {m:.2f}")
print(f"Intercept (b): {b:.2f}")

def covariance(x, y):
    # Finding the mean of the series x and y
    mean_x = sum(x)/float(len(x))
    mean_y = sum(y)/float(len(y))
    # Subtracting mean from the individual elements
    sub_x = [i - mean_x for i in x]
    sub_y = [i - mean_y for i in y]
    numerator = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
    denominator = len(x) - 1
    cov = numerator/denominator
    return cov

x = [1, 2, 3, 4, 5]
y = [2.1, 3.9, 6.2, 8.1, 9.8]
cov = covariance(x, y)
print(cov)


"""Problem Statement
Given a garden with different types of flowers, try to find if a particular combination of flowers is present. Each flower in the garden is represented by a character (D = Daisies, F = Daffodils, I = Irises, L = Lilies, M = Marigolds, P = Peonies, R = Roses, S = Sunflowers, T = Tulips, V = Violets). For example, consider the following garden:

FILMPRSTVD
DVTSRPMLIF
FFFFFFFFFF
FFFFFFFFFF
IIIIIIIIII
The combination of flowers to search for is:

TSRPML
FFFFFF
FFFFFF
The combination begins at the second row and the third column of the grid and continues in the following two rows. The combination is said to be present in the garden. The return value should be 'YES' or 'NO', depending on whether the combination is found. In this case, return YES.


Function Description
Complete the flower_search function in the editor below. It should return YES if the combination exists in the garden, or NO otherwise.

flower_search has the following parameter(s):

string G: the garden to search
string P: the combination to search for


Input Format
The test cases is represented as follows: There are two input strings. The first string is the lines that represent the garden. The second string is the lines that represent the combination.


Returns
string: either YES or NO"""

# Do not import any additional libraries
import math
import os
import random
import re
import sys

# Complete the 'flower_search' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING G
#  2. STRING P

def flower_search(G, P):
    # YOUR CODE HERE

    print("******Made by MELİS İLDİRECİ******")
    # Split the garden and combination strings into lists of strings
    G_rows = G.split("\n")
    P_rows = P.split("\n")
    
  
    """
    I calculated the dimensions of the Garden and 
    combination strings. I calculated the garden sizes with the G_height and G_width variables, 
    and the combination sizes with the P_height and P_width variables."""
    
    G_height = len(G_rows)
    G_width = len(G_rows[0])
    P_height = len(P_rows)
    P_width = len(P_rows[0])
    


    """
     I started a loop for all positions in the Garden where combination can have any position.
     In this loop, the variables i and j represent positions in the garden.
    """
    # Iterate over all possible starting positions for the combination in the garden
    for i in range(G_height - P_height + 1):
        for j in range(G_width - P_width + 1):
            # Check if the combination is present starting at this position
            match = True
            for k in range(P_height):
                for l in range(P_width):
                    garden_char = G_rows[i+k][j+l]
                    pattern_char = P_rows[k][l]
                    if garden_char != pattern_char:
                        match = False
                        break
                if not match:
                    break
            if match:
                return "YES"
                """
                In each position, we checked whether the combination exists in the garden. I performed the control with the match variable. 
    The variables k and l represent positions in the combination.
     Using two nested loops, we compared the characters in the garden and combination strings for each value of k and l. 
     If the characters do not match, we stop the inner loop by setting the variable match to False. We then continued the loop to check for combination at the next position.

     If the combination is found at any position in the garden, the variable match becomes True and the return "YES" command returns the value "YES" from the function.
                """
    
    # If we didn't find a match, return "NO"
    return "NO"
# Sample Input 1
G = "SITLMPPTRM\nRSLFFPTRFV\nTVTTIMIRML\nLTLDPTVLIM\nIIIVPDPTFL\nPRLLTMPLSM\nRMSLPLDIVL\nSDPLFDRRDF\nDTLMITIVPR\nMRDSVIMFLS"
P = "VPDP\nLTMP\nLPLD"

#call the flower_search function
result1 = flower_search(G, P)
#Sample Output 1
print('Result 1 ={0}'.format(result1))  


#Sample Input 2
G = "MDDMPLPVIFIRPRD\nFFMIFLFLLDVTRVI\nMSMLTRDTITSVRMT\nPIILPRVPFFTVFRV\nTTSFDVMPDMTSMVR\nIPITDIRLLLTTSTI\nPDISSFMTMVRRSMT\nDSPVSPIDSRVLSTD\nPFFSVVSTVPRITDR\nMDMDDSMPMISIPDM\nPMVDMLTDVVFRDTD\nVRIMFDTDVPLMTFF\nMMPTVLPILSLLMSP\nSRTSDPLDLIFMFSM\nRPDRIVISDTTSFRD"
P = "VV\nVV"

#call the flower_search function
result2 = flower_search(G, P)
#Sample Output 2
print('Result 2 ={0}'.format(result2)) 
# This function will output NO according to G and P inputs.