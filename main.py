n = input()
new_n = num[::-1]
if eval(num) == eval(new_n):
    print("此数是回文数")
else:
    print("此数不是回文数")
