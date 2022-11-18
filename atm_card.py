
class ATMCard:

    def __init__(self, cardNum, cardPin):
        self.__cardNumber = cardNum
        self.__cardPin = cardPin
        self.__cardBalance = 0
        print("\nSukses membuat kartu ATM !\ninformasi\nnomor kartu Anda: " + str(self.__cardNumber) + "\nNomor PIN Anda: "  + str(self.__cardPin) + "\nDengan Saldo: " + str(self.__cardBalance) + '\n')

    def _secureAccess(self, authPin):
        if (self.__cardPin == authPin):
            return True
        else:
            return False
    
    def addBalance(self, authPin, newBalance):
        if (self._secureAccess(authPin)):
            self.__cardBalance += newBalance
        

    def checkBalance(self):
        return self.__cardBalance

    def checkCard(self):
        return self.__cardNumber

    def checkPin(self):
        return self.__cardPin

    def gantiPin(self, newPin):
        self.__cardPin = newPin
        return "Anda berhasil mengubah pin menjadi " + str(newPin)
        
        

a_card = ATMCard(10101, 55555)
a_card.addBalance(55555, 100000)
print(a_card.checkBalance())