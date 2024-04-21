salarioFuncionario = float(input())

if salarioFuncionario >= 0 and salarioFuncionario <= 400:
    reajuste = salarioFuncionario * 0.15
    porcentagem = "15 %"
elif salarioFuncionario > 400 and salarioFuncionario <= 800:
    reajuste = salarioFuncionario * 0.12
    porcentagem = "12 %"
elif salarioFuncionario > 800 and salarioFuncionario <= 1200:
    reajuste = salarioFuncionario * 0.1
    porcentagem = "10 %"
elif salarioFuncionario > 1200 and salarioFuncionario <= 2000:
    reajuste = salarioFuncionario * 0.07
    porcentagem = "7 %"
elif salarioFuncionario > 2000:
    reajuste = salarioFuncionario * 0.04
    porcentagem = "4 %"
    
novoSalario = salarioFuncionario + reajuste

print(f"Novo salario: {novoSalario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {porcentagem}")    
