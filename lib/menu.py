from .automato import AFD

class Menu:
    def __init__(self):
        self.afd = AFD()

    def run(self):
        try:
            while True:
                self._run_loop()
        except KeyboardInterrupt:
            self.afd.plot()

    def _run_loop(self):
        greetings = '''
        \rDigite 1 opção:
        \r  1) Inserir de estado
        \r  2) Inserir transicao
        \r  3) Checar palavra
        \r  4) Imprimir AFD
        \r  5) Carregar AFD sobre (a+b)*a(a+b)(a+b)
        \r  6) Encerrar
        \n
        '''

        print(greetings)
        opt = input('Opção: ')

        match(opt):
            case '1':
                self.insert_state()
            case'2': 
                self.insert_transition()
            case '3':
                self.check_word()
            case '4':
                self.print()
            case '5':
                self.load_afd()
            case '6':
                print('fim')
                exit()
            case other:
                print('\nNão entendi\n')

    def print(self):
        self.afd.plot()

    def _ask_value(self):
        opt = input('Digite o valor (vazio para cancelar): ').strip()

        if not opt:
            return

        try:
            return opt
        except:
            print('Não entendi. Digite de novo')
            self._ask_value()

    def insert_state(self):
        while value := self._ask_value():
            if not value:
                break
            
            exists = False
            for state in self.afd.states:
                if state.name == value:
                    print(f'Valor {state.name} não adicionado.')
                    exists = True

          
            if not exists:
                initial = False
                if not self.afd.initial_state:
                    initial = int(input("É um estado inicial? (Nao == 0)")) != 0
                final = int(input("É um estado final? (Nao == 0)")) != 0 
                self.afd.add_state(value, is_initial=initial, is_final=final)
                print()

    def insert_transition(self):
        while True:
            value = int(input("Adicionar a transição? (0 para cancelar):"))
            if not value:
                break

            origin = input("Estado de origem: ")
            destine = input("Estado de destino: ")

            for state in self.afd.states:
                if state.name == origin:
                    origin = state
                if state.name == destine:
                    destine = state

            symbol = input("Simbolo: ")
            
            self.afd.add_transition(origin, destine, symbol)

    def check_word(self):
        while True:
            word = input("Digite a palavra para checagem (Vazio para cancelar): ")
            if not word:
                break

            if self.afd.word_checker(word):
                print("A palavra pertence à linguagem")
            else:
                print("A palavra não pertence à linguagem")

    def print(self):
        self.afd.plot()
    
    def load_afd(self):
        self.afd = AFD()
        # Adicionando os estados
        q0 = self.afd.add_state('q0', is_initial=True)
        q1 = self.afd.add_state('q1')
        q2 = self.afd.add_state('q2')
        q3 = self.afd.add_state('q3')
        q4 = self.afd.add_state('q4', is_final=True)
        q5 = self.afd.add_state('q5', is_final=True)
        q6 = self.afd.add_state('q6', is_final=True)
        q7 = self.afd.add_state('q7', is_final=True)

        # Adicionando as transições
        self.afd.add_transition(q0, q1, 'a')
        self.afd.add_transition(q0, q0, 'b')
        self.afd.add_transition(q1, q2, 'a')
        self.afd.add_transition(q1, q3, 'b')
        self.afd.add_transition(q2, q4, 'a')
        self.afd.add_transition(q2, q5, 'b')
        self.afd.add_transition(q3, q6, 'a')
        self.afd.add_transition(q3, q7, 'b')
        self.afd.add_transition(q4, q4, 'a')
        self.afd.add_transition(q4, q5, 'b')
        self.afd.add_transition(q5, q6, 'a')
        self.afd.add_transition(q5, q7, 'b')
        self.afd.add_transition(q6, q2, 'a')
        self.afd.add_transition(q6, q3, 'b')
        self.afd.add_transition(q7, q1, 'a')
        self.afd.add_transition(q7, q0, 'b')
    