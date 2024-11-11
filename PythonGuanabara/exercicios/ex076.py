from tabulate import tabulate

compra = [

        (1,'Macarrão', 2.99),
        (2,'Tomate', 1.69),
        (3,'Leite Condensado', 2.50),
        (4, 'Biscoito', 4.50)

        ]

print(tabulate(compra,  headers=['ID', 'Item', 'Preço (R$)'], tablefmt="grid"))
