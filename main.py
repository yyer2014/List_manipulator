class Actor:
    def __init__(self):
        # Список для манипулирования
        self.li = ['0']


    def wait(self):
        while(True):
            print("+".join(self.li))
            # Ожидание ввода строки
            symbol = input('Операция со списком: введи один знак (PQRS - служебные) ').upper()
            if symbol == 'Q':   # служебный символ для выхода из цикла
                break
            elif symbol == 'P':
                self.li.pop()
            elif symbol == 'R':
                self.li.reverse()
            elif symbol == 'S':
                self.li.sort()
            else:
                self.li.append(symbol)


if __name__ == '__main__':
    Actor().wait()
