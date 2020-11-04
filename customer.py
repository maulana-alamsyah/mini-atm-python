from atm_card import ATMCard

class Customer:
    def __init__(self, custPin, custBalance):
        self.id = 1
        self.custPin = custPin
        self.custBalance = custBalance

    def withdrawBalance(self, nominal):
        if nominal > int(self.custBalance):
            return '\nSaldo Anda tidak cukup.'
        elif nominal < int(self.custBalance):
            self.custBalance = self.custBalance - nominal
            return '\nAnda telah melakukan debet senilai ' + str(nominal) + '\nsaldo anda sekarang ' + str(self.custBalance)

    def depositBalance(self, nominal):
        self.custBalance = self.custBalance + nominal
        return '\nAnda berhasil melakukan simpan senilai ' + str(nominal) + '\nsaldo anda sekarang ' + str(self.custBalance)

    def checkBalance(self):
        return "\nSaldo Anda saat ini adalah " + str(self.custBalance)
