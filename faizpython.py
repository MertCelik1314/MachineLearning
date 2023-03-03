
accountBalance = float(input("Ana para miktarini girin :"))
balanceAtStart = accountBalance
mounts = int(input("Faiz suresini girin(ay) :"))
rate = 18/1000
a =0
finalBalance = 0.0

while a < mounts:
 accountBalance = ((accountBalance*rate)+accountBalance)
 a += 1

print("Yeni hesap bakiyeniz : " ,accountBalance)
print(mounts ,"Ay sonunda faizden kazanılan para : ", accountBalance-balanceAtStart)
