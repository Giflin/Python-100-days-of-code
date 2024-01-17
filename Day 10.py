def format_name(f_name,l_name):
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"{formated_f_name} {formated_l_name}"
print(format_name("Angela","Yu"))

def format_name(f_name,l_name):
  """ Take the names and convert it into the title case
  """
  if f_name=="" or l_name=="":
      return "You didn't provide complete information."
  formated_f_name=f_name.title()
  formated_l_name=l_name.title()
  return f"{formated_f_name} {formated_l_name}"
print(format_name(input("Enter your first name:"),input("Enter your last name:")))

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year)==True:
    month_days[1]=29
    return month_days[month-1]
  else:
    return month_days[month-1]

year = int(input("Enter a year:"))
month = int(input("Enter a month:"))
days = days_in_month(year, month)
print(days)



# CALCULATOR

def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2
operations={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}
num1=int(input("Enter a number1: "))
for symbols in operations:
  print(symbols)
cal_symbol=input("Select an operation from the list of symbols to perform calculation: ")
num2=int(input("Enter a number2: "))
calculation=operations[cal_symbol]
answer=calculation(num1,num2)
print(f"{num1} {cal_symbol} {num2} = {answer}")


