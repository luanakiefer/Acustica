from cProfile import label
import matplotlib.pyplot as plt

def plotar_perfis(pontos: list, posicao: str, data: str) -> None:
    profundidades = [ponto.profundidade for ponto in pontos]
    
    # Perfil de salinidade
    fig = plt.figure(1)
    plt.plot([ponto.salinidade for ponto in pontos], profundidades)
    plt.title(f"Perfil de salinidade interpolado em {posicao}\n({data})", fontdict={'fontweight': 'bold'})
    plt.ylabel("Profundidade (m)")
    plt.xlabel("Salinidade (psu)")
    plt.gca().invert_yaxis()

    # Perfil de temperatura
    fig = plt.figure(2)
    plt.plot([ponto.temperatura for ponto in pontos], profundidades)
    plt.title(f"Perfil de temperatura interpolado em {posicao}\n({data})", fontdict={'fontweight': 'bold'})
    plt.ylabel("Profundidade (m)")
    plt.xlabel("Temperatura (ºC)")
    plt.gca().invert_yaxis()

    # Perfil de velocidade
    fig = plt.figure(3)
    plt.plot([ponto.velocidade for ponto in pontos], profundidades)
    plt.title(f"Perfil de velocidade interpolado em {posicao}\n({data})", fontdict={'fontweight': 'bold'})
    plt.ylabel("Profundidade (m)")
    plt.xlabel("Velocidade (m/s)")
    plt.gca().invert_yaxis()

def plotar_varios_perfis(perfis: list, posicao: str, data: str) -> None:
    profundidades = [ponto.profundidade for ponto in perfis[0]]
    
    # Perfil de salinidade
    fig = plt.figure(1)

    for i, perfil in enumerate(perfis):
        plt.plot([ponto.salinidade for ponto in perfil], profundidades, label=f"{i}")

    plt.title(f"Perfil de salinidade interpolado em {posicao}\n({data})", fontdict={'fontweight': 'bold'})
    plt.ylabel("Profundidade (m)")
    plt.xlabel("Salinidade (psu)")
    plt.gca().invert_yaxis()
    plt.legend(loc="upper right")

    # Perfil de temperatura
    fig = plt.figure(2)
    
    for i, perfil in enumerate(perfis):
        plt.plot([ponto.temperatura for ponto in perfil], profundidades, label=f"{i}")
    plt.title(f"Perfil de temperatura interpolado em {posicao}\n({data})", fontdict={'fontweight': 'bold'})
    plt.ylabel("Profundidade (m)")
    plt.xlabel("Temperatura (ºC)")
    plt.gca().invert_yaxis()
    plt.legend(loc="upper right")

    # Perfil de velocidade
    fig = plt.figure(3)
    
    for i, perfil in enumerate(perfis):
        plt.plot([ponto.velocidade for ponto in perfil], profundidades, label=f"{i}")
    plt.title(f"Perfil de velocidade interpolado em {posicao}\n({data})", fontdict={'fontweight': 'bold'})
    plt.ylabel("Profundidade (m)")
    plt.xlabel("Velocidade (m/s)")
    plt.gca().invert_yaxis()
    plt.legend(loc="upper right")