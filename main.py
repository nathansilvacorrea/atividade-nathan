
Exercício 2
nome = input("Digite seu nome: ").strip()
idade = int(input("Digite sua idade: "))
turma = input("Digite sua turma: ").strip().uper()
altura = float(input("Digite sua altura: ").replace(",", "."))
programou = input("Já programou? (sim/não): ").strip().lower() ==

print("\n--- FICHA DO ALUNO ---")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Turma: {turma}")
print(f"Altura: {altura:.2f} m")
print(f"Já programou: {programou}")