import logging
from sys import argv

def get_log():
    logging.basicConfig(
        filename='Bankomat.log',
        filemode='a',
        encoding='UTF-8',
        format='{asctime} {levelname:<6} {lineno:3>} : {msg}',
        style='{',
        level=logging.INFO
    )

    return logging.getLogger(__name__)

class Bankomat():
    def __init__(self, bank = 0):
        self.__bank = bank
        
    def get_bank(self):
        return self.__bank
    

    def add_bank(self):
        cash = int(input("Введите сумму, кратную 50: "))
        self.__bank += cash
        get_log().info(f'Внесена сумма {cash}. Баланс {self.get_bank()}')
        
        return print('Your balance: ', self.get_bank())
    

    def take_bank(self):
        cash = int(input("Введите сумму, кратную 50: "))
        if cash > self.__bank:
            get_log().error(f'Не удалось снять {cash}...')
            print('Нет денег!')
            get_log().info(f'Завершение работы банкомата')
            exit()        
        if cash <=2000:
            cash -=30
        elif 2001 <= cash <= 40000:
            cash *= 0.0985
        else:
            cash -= 600
        self.__bank -= cash
        
        get_log().info(f'Cнята сумма {cash}. Баланс {self.get_bank()}')
        print('Your balance: ', self.get_bank())

b = Bankomat(0)

def wellcome():
        dict = {}
        id = 1
        while True:
            action = int(input('1 - Снять\n2 - Пополнить\n3 - Выйти\n'))
            if b.get_bank() >= 5000000:
                b.__bank *= 0.9
            match action:
                case 1:
                    b.take_bank()                                    
                        
                case 2:
                    b.add_bank()
                case 3:
                    get_log().info(f'Завершение работы банкомата')
                    exit()


if __name__ == '__main__':
    wellcome()