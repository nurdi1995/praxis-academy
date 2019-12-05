print("========================ATM=====================")
print("      Welcome to this simple ATM machine        ")
print("================================================")

print("""
Press [1]        Deposit
press [2]        Withdraw
press [3]        Balance Inquiry
Press [4]        Exit
""")
print()

while True:
    try:
        Saldo=50000
        Option=int(input("What would you like to do ? "))
    except ValueError:
        print("Input salah, transaksi tidak dapat dilakukan!")
        continue
    else:
        break
        

if Option==1:
    print("Saldo anda ",Saldo)
    Deposit=float(input("Masukkan jumlah yang akan didepositkan: "))
    if Deposit>0:
        forewardbalance=(Saldo+Deposit)
        print("saldo anda saat ini :   ",forewardbalance)
    else:
        print("None deposit made")
if Option==2:
    print("saldo anda    ",Saldo)
    Withdraw=float(input("Enter Withdraw amount  "))
    if Withdraw>0:
        forewardbalance=(Saldo-Withdraw)
        print("Foreward Balance   ",forewardbalance)
    elif Withdraw>saldo:
        print("No funs in account")
    else:
        print("None withdraw made")

        
if Option==3:
    print("Saldo anda saat ini:   ",Saldo)

    
if Option==4:
    exit()

