def is_golden_number(n):
#     # function implementation ...
     A = 0
     while n > 0:
          if n * A == 1000:
               boolean = True
               break
          A = A + 1
          n = n - 1
     if n == 0:
          boolean = False
    

     
     return boolean
print(is_golden_number(70))
