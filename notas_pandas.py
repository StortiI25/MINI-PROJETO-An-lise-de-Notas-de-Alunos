import os
import pandas as pd
import matplotlib.pyplot as plt
base_dir = os.path.dirname(__file__)
caminho = os.path.join(base_dir, "data", "notas.csv")

df = pd.read_csv(caminho)

print("Dados:")
print(df.head())

media = df["nota"].mean()
print(f"\nMedia geral: {media}\n")

media_curso = df.groupby("curso")["nota"].mean().sort_values(ascending=False)
print (f"Media de notas por cursos: \n{media_curso}\n")

alunos = df[df["nota"] > 8]
print(f"Alunos que se destacaram: \n{alunos}\n")

melhor_aluno = df.loc[df["nota"].idxmax()]
print(f"Aluno do mês: \n{melhor_aluno}\n")

idade_media = df.groupby("curso")["idade"].mean()
print(f"Idade media por curso: \n{idade_media}\n")

alunos_cursos = df["curso"].value_counts()
print(f"Alunos matriculas por curso: \n{alunos_cursos}")

media_curso.plot(kind="bar", color="green")

plt.title("Medía de Notas por Curso")
plt.xlabel("Cursos")
plt.ylabel("Medía de Notas")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("media_por_cusos.png")

plt.show()
plt.clf()

alunos_cursos.plot(kind="bar")

plt.title("Alunos por Cursos")
plt.xlabel("Cursos")
plt.ylabel("Alunos")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("alunos_por_curso.png")

plt.show()
plt.clf()

# Gráfico de Pizza
plt.figure(figsize=(6,6))
plt.axis('equal')
plt.pie(
    alunos_cursos,
    labels=alunos_cursos.index,
    autopct='%1.1f%%',
    startangle=90,
    explode=[0.02] * len(alunos_cursos)
)

plt.title("Distribuição de Alunos por Curso")
plt.tight_layout()
plt.savefig("distribuicao_alunos.png")
plt.show()
