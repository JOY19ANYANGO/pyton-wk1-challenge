def time_converter(hour ,minute,period):
    if (hour>=0 and hour<12) and period=="pm" and(minute>=0 and minute<=59):
         hour += 12
         return f"{hour:02d}:{minute:02d}"
         
    elif hour==12 and (minute>=0 and minute<=59) and period=="pm":
        return f"{hour:02d}:{minute:02d}"
    
    elif (hour>=0 and hour<12) and period=="am" and(minute>=0 and minute<=59):
         return f"{hour:02d}:{minute:02d}"
    
    elif hour==12 and (minute>=0 and minute<=59) and period=="am":
        hour =00
        return f"{hour:02d}:{minute:02d}"
    else:
        print("invalid time format")     
         
         
    
     

    
    