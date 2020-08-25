def calcular_BMI(peso_lb,altura_inch):
    pesokg=peso_lb*0.45
    alturamts=altura_inch*0.025
    bmi=pesokg/(alturamts**2)
    return round(bmi,2)
print(calcular_BMI(1,2))

def calcular_BMI2(peso_lb: float, altura_inch: float)->float:
    peso_lb=peso_lb*0.45
    altura_inch=altura_inch*0.025
    resultado = peso_lb/(altura_inch**2)
    return round(resultado,2)
print(calcular_BMI2(1,2))