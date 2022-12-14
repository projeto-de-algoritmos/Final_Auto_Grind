from collections import Counter
from collections import defaultdict

menu_txt = """
[1] adicionar item
[2] remover item
[3] traçar rota
[0] sair

[?] """

items = [
	("Túnica única", 6, 50), ("Espada de pau", 3, 20), ("Espada de fogo", 5, 70), ("Escudo de pedra", 9, 30),
	("Escudo de pau", 4, 20), ("Chapéu nobre", 7, 45), ("Machado de ferro", 8, 50), ("Bota de botas", 2, 40),
	("Queijo de mamute", 1, 10)
	]

mochila = []

graph = {
	'1' : [], 
	'2' : ['1'], 
	'3' : [], 
	'4' : ['3'],
	'5' : ['4'], 
	'6' : ['2'], 
	'7' : ['6'], 
	'8' : ['5'], 
	'9' : ['8', '7'],
	}

def totalvalue(comb):
	peso_total = valor_total = 0
	for item, peso, valor in comb:
		peso_total  += peso
		valor_total += valor
	return (valor_total, -peso_total)


def knapsack01(items, cap):
	tabela = [[0 for w in range(cap + 1)] for q in range(len(items) + 1)]
	
	for item in range(1, len(items) + 1):
		_, peso_item, valor_item = items[item-1]
		
		for aux_peso in range(1, cap + 1):
			if peso_item > aux_peso:
				tabela[item][aux_peso] = tabela[item-1][aux_peso]
			else:
				v1 = tabela[item-1][aux_peso-peso_item] + valor_item
				v2 = tabela[item-1][aux_peso]

				if v1 > v2:
					tabela[item][aux_peso] = v1
				else:
					tabela[item][aux_peso] = v2

	result = []
	cap_limite = cap

	for item in range(len(items), 0, -1):
		was_added = tabela[item][cap_limite] != tabela[item-1][cap_limite]

		if was_added:
			_, peso_item, _ = items[item-1]
			result.append(items[item-1])
			cap_limite -= peso_item
	
	return result


def djikstra():
	...

def clear():
    print(chr(27) + "[2J")


def listar_itens(arr):
	i = 0
	for item in arr:
		i+=1
		print(f"[{i}] {item[0]}\tpeso: {item[1]} valor: {item[2]}")


def adicionar_item_mochila():
	global mochila
	global capacidade
	print("[+] Itens da mochila:\n")
	listar_itens(mochila)

	print("\n[+] Qual item deseja adicionar?\n")
	listar_itens(items)
	print("\n[0] Cancelar")

	while True:
		opt = input("[?] ")
		try:
			opt = int(opt)
			if opt >= len(items)+1:
				input("[-] Digite uma opcao valida, tecle ENTER para continuar")
				continue
			break
		except:
			input("[-] Digite um numero inteiro, tecle ENTER para continuar")
			continue
	
	if opt == 0:
		return

	aux_mochila = mochila.copy()
	aux_mochila.append(items[opt-1])
	aux_mochila = knapsack01(aux_mochila, capacidade)

	if sorted(aux_mochila) == sorted(mochila):
		input("[-] Nao ha vantagem em pegar o item, precione ENTER para continuar")
		return

	mochila_c = Counter(mochila)
	aux_mochila_c = Counter(aux_mochila)

	diff = aux_mochila_c - mochila_c
	diff = list(diff.elements())
	
	if len(diff) > 0:
		for item in diff:
			print(f"[+] Item adicionado: {item}")

	diff = mochila_c - aux_mochila_c
	diff = list(diff.elements())
	
	if len(diff) > 0:
		for item in diff:
			print(f"[+] Item removido: {item}")


	input("[+] Tecle ENTER para continuar")
	mochila = aux_mochila


def remover_item_mochila():
	global mochila

	print("[+] Qual item deseja remover?\n")
	listar_itens(mochila)
	print("\n[0] Cancelar")

	while True:
		opt = input("[?] ")
		try:
			opt = int(opt)
			if opt >= len(mochila)+1:
				input("[-] Digite uma opcao valida, tecle ENTER para continuar")
				continue
			break	
		except:
			input("[-] Digite um numero inteiro, tecle ENTER para continuar")
			continue
	
	if opt == 0:
		return

	input(f"[+] Item removido: {mochila[opt-1][0]} Tecle ENTER para continuar")
	del mochila[opt-1]

	return

while True:
	capacidade = input("[+] Qual a capacidade de sua mochila?\n[?] ")
	try:
		capacidade = int(capacidade)
		break
	except:
		input("[-] Digite um numero inteiro, tecle ENTER para continuar")
		continue


while True:
	clear()
	print("[+] Itens da mochila:\n")
	listar_itens(mochila)
	val, totalWeight = totalvalue(mochila)
	print("\n[+] Valor: %i Peso: %i/%i" % (val, -totalWeight, capacidade))
	opt = input(menu_txt)

	try:
		opt = int(opt)
	except:
		input("[-] Digite uma opcao valida, tecle ENTER para continuar")
		continue

	if opt == 1:
		clear()
		adicionar_item_mochila()
		continue

	if opt == 2:
		clear()
		remover_item_mochila()
		continue
	
	if opt == 3:
		clear()
		djikstra()
		continue
 
	if opt == 0:
		exit(0)

	input("[-] Digite uma opcao valida, tecle ENTER para continuar")