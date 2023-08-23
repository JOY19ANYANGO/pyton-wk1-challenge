'''pseudocode.
   Define a function two_positive_numbers that takes a, b and c as parameters.
   create a variable positive_count and give it an initial value of 0
   If a or b or c is positive the current value of positive_count is increased by 1.
   If the value of positive_count is equal to 2 return true otherwise return false.'''

def two_positive_numbers(a, b, c):
    positive_count = 0
    # increase value of positive_count by 1 if a or b or c is positive
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    #returns true if ppositive_count is 2 and false if otherwise
    print(positive_count == 2)

  #example usage     
two_positive_numbers(2, 4, -3) 
two_positive_numbers(-4, 6, 8)
two_positive_numbers(4, -6, 9) 
two_positive_numbers(-4, 6, 0) 
two_positive_numbers(4, 6, 10)
two_positive_numbers(-14, -3, -4)
 
