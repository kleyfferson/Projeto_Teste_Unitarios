class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 99
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        #print(f"Esse restaturante chama {self.restaurant_name} e serve {self.cuisine_type}.") #Aqui está retornando o tipo da cosinha duas vez e não o tipo e nome do restaurante
        #print(f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto.")
        #esse metodo deveria ter um return da seguinte forma
        return f"Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type}.\nEsse restaturante está servindo {self.number_served} consumidores desde que está aberto."


    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True  #deveria estar True e não False quando o restaurante abrir
            self.number_served = 0  #Deveria ter 0 a quantidade de clientes e não menos 2
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"


    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers): #Aqui é quantidade de pessoas que foram atendidas
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.inteiro_ou_string(total_customers):
            if self.open:
                 self.number_served == total_customers
                 return self.number_served
            else:
                return f"{self.restaurant_name} está fechado!"
        else:
            return

    def increment_number_served(self, more_customers): # Aqui há um incremento
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served += more_customers #aqui ele só está recebendo do parametro o certo na linguagem Python é += para adicionar a quandidade
        else:
            return f"{self.restaurant_name} está fechado!"
    def inteiro_ou_string(self,compara):
        """nesse metodo foi criado com o objetivo de comparar se o valor é string ou inteiro"""
        if type(compara) == int and compara > 0:
            return True
        else:
            return "O valor que você digitou foi tipo diferente do inteiro sendo que tem que ser um numero maior que zero.E só aceitamos inteiro irmão"
