class ATMCard:
    def __init__(self):
        self.cardNumber = 1003122892928
        self.cardPin = 1234
        self.cardBalance = 0
        print("\nSukses membuat kartu ATM !\ninformasi\nnomor kartu Anda: " + str(self.cardNumber) + "\nNomor PIN Anda: "  + str(self.cardPin) + "\nDengan Saldo: " + str(self.cardBalance) + '\n')

    def checkBalance(self):
        return self.cardBalance

    def checkCard(self):
        return self.cardNumber

    def checkPin(self):
        return self.cardPin

    def gantiPin(self, newPin):
        self.cardPin = newPin
        return "Anda berhasil mengubah pin menjadi " + str(newPin)
        