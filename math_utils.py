def find_max_number(num1, num2, num3):
  if num1 > num2 and num1 > num2 :
    return num1
  if num2 > num1 and num2 > num3 :
    return num2
  return num3

def find_mean(num1, num2, num3):
    x=((num1 + num2 + num3)/3)
    return x

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    mean_std= ((((num1 - x)**2) + ((num2 - x)**2) + ((num3 - x)**2)/3)**(1/2))x=((num1 + num2 + num3)/3)

