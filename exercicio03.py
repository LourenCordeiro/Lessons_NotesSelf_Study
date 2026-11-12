aluno = {
    "Nome": "Ursula",
    "Notas": [8.0, 9.5, 9.5],
    "Aprovada": True
}

media_notas = sum(aluno["Notas"]) / len(aluno["Notas"]) 
aluno["Média Final"] = media_notas
print(aluno)
