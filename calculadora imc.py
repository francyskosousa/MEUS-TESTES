peso=100
altura=1.65

imc = peso/altura**2

print(imc)

if imc <18.5:
    print('abaixo do peso')
elif imc >18.5 and imc <24.9:
    print('acima do peso')
elif imc >24.9 and imc<29.9:
    print('sobrepeso')
elif imc >30 and imc <34.9:
    print('obesidade1')
elif imc >35 and imc <39.9:
    print('Obesidade2')
else:
    print('Procure um médico urgente!')


    

