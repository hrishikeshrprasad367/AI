

def truthTable(expression,expression1,inputs=2):
  print("Boolean Expression:")
  print("  KB = " + expression.upper())
  print("  Alpha = " + expression1.upper())
  expression = expression.lower()
  expression1 = expression1.lower()
  
  #replace Boolean Operators with bitwise operators
  expression = expression.replace("and","&")
  expression = expression.replace("xor","^")
  expression = expression.replace("or","|")
  expression = expression.replace("not","~")

  expression1 = expression1.replace("and","&")
  expression1 = expression1.replace("xor","^")
  expression1 = expression1.replace("or","|")
  expression1 = expression1.replace("not","~")
  
  print("\nTruth Table:")
  is_entails=True   
  if inputs==3:
    print("  ---------------------")
    print("  | A | B | C | KB| α |")
    print("  ---------------------")
    
    for a in range(0,2):
      for b in range(0,2):
        for c in range(0,2):
          x = eval(expression)
          y = eval(expression1)

          if x==1:
            if y==0:
              is_entails=False

          print("  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(x) + " | " + str(y) + " |" )
          print("  ---------------------")
       


  if is_entails:
    print("KB ⊨ Alpha since wherever KB is true so is alpha")
    print(expression + " ⊨ " + expression1)
  else:
    print("KB does not entail Alpha")
    print(expression + " ⊭ " + expression1)
    
##############################################

kb = "(A or C) and (B or (not C))"
alpha = "A or B"
truthTable(kb,alpha,3)

