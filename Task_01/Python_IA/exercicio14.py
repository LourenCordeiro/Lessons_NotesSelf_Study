termos = ["python", "dados", "python", "api", "dados", "sql"]

termos_unicos = set(termos)
print(termos_unicos)

termos_unicos[0:2] = ["python", "dados"]
print(termos_unicos)

#O set não é indexado(imutável) e com elementos não ordenados, com isso, não conseguimos usar o slicing para fatiar.