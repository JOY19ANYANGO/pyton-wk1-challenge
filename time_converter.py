'''pseudocode
   Creata a function called time converter that takes in hour minute and period as the parameters.
   Ensure that the hour ranges from 1 to 12 and minute ranges from 0 to 59.
   If the user input hour ranging from 1 to 11 and a period of pm add the hour by 12.
   If the user input hour ranging from 1 to 11 and a period of am leave the hour as it is.
   If the user input hour of 12 and period of pm do not add anything to the hour
   if the user input hour of 12 and period af am set the hour to 0.
   If the user inputs hours and minutes that are not of required range print invalid time format.
   '''
   







def time_converter(hour ,minute,period):
    # adding 12 for hours ranging 1 to 11 and period pm
    if (1<= hour<= 11) and period=="pm" and(1<= minute <=59):
         hour += 12
         print(f"{hour:02d}{minute:02d}")
     # not adding anything for hour==12 and period  pm   
    elif hour==12 and (1<= minute <=59) and period=="pm":
       print(f"{hour:02d}{minute:02d}")
    # not adding anything for ranging 1 to 11 and period am
    elif (1<= hour< 12) and period=="am" and(1<= minute <=59):
         print(f"{hour:02d}{minute:02d}")
    # setting hour to 0 when the hour is 12 and period am
    elif hour==12 and (1<= minute <=59) and period=="am":
        hour =0
        print(f"{hour:02d}{minute:02d}")
    # printing invalid tim foormat for hours not ranging frm 1 to 12 and minutes not ranging from 0 to 59
    else:
        print("invalid time format")     
         
         
    
   #example usage
time_converter(8,30,'am')
time_converter(8,30,'pm')
time_converter(12,15,'am')
time_converter(12,15,'pm')
time_converter(13,30,'am')  

    
    