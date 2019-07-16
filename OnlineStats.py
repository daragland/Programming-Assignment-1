#------------------------------------------------------------------------------#
# CPSC-511 Section 3,   Summer 2019                                            #       
# OnlineStats.py       Author: Debra Ragland                                   #
# 7/16/19                                                                      #
#------------------------------------------------------------------------------#


#declare variables
sample_count = 0
variance = 0
mean = 0

#ask use for input, if the value is greater than 0, continue with calculation
while True:
    in_value = float(input('Enter a number: '))
    if in_value < 0:
        break
    sample_count += 1
   
#if there is only 1 input, there should be no variance, if there is more than 1
#input, continue with calculation 
    if sample_count == 1:
        mean = in_value
        variance = 0
    else:
        mean = mean + (in_value - mean)/sample_count
        variance = (((sample_count - 2)/ (sample_count - 1))*variance) + ((in_value - mean)**2)/sample_count
        
    print('Mean is {} variance is {}'.format(mean, variance))
   

