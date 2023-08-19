def two_positive_numbers(a, b, c):
    positive_count = 0
    
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    return positive_count == 2

       
two_positive_numbers(2, 4, -3) 
two_positive_numbers(-4, 6, 8)
two_positive_numbers(4, -6, 9) 
two_positive_numbers(-4, 6, 0) 
two_positive_numbers(4, 6, 10)
two_positive_numbers(-14, -3, -4)
 
