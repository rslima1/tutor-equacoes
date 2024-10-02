import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Função para centralizar a janela na tela
def centralizar_janela(janela, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

# Função para criar uma janela de aviso personalizada
def mostrar_aviso(mensagem, dica=""):
    aviso_janela = tk.Toplevel(root)
    aviso_janela.title("Atenção")
    
    # Configurando a janela de aviso
    largura = 400
    altura = 200
    centralizar_janela(aviso_janela, largura, altura)
    aviso_janela.configure(bg="lightyellow")

    # Texto da mensagem com fonte maior
    label_aviso = tk.Label(aviso_janela, text=mensagem, font=("Arial", 16), bg="lightyellow", fg="orange", wraplength=350)
    label_aviso.pack(pady=10)

    # Texto da dica, se houver
    if dica:
        label_dica = tk.Label(aviso_janela, text=dica, font=("Arial", 14), bg="lightyellow", wraplength=350)
        label_dica.pack(pady=10)

    # Botão OK para fechar a janela
    botao_ok = tk.Button(aviso_janela, text="OK", command=aviso_janela.destroy, font=("Arial", 14), bg="red", fg="white")
    botao_ok.pack(pady=10)

# Função para criar uma janela de sucesso personalizada
def mostrar_sucesso(mensagem):
    sucesso_janela = tk.Toplevel(root)
    sucesso_janela.title("Sucesso")

    # Configurando a janela de sucesso
    largura = 400
    altura = 200
    centralizar_janela(sucesso_janela, largura, altura)
    sucesso_janela.configure(bg="lightgreen")

    # Texto da mensagem com fonte maior
    label_sucesso = tk.Label(sucesso_janela, text=mensagem, font=("Arial", 16), bg="lightgreen", fg="green", wraplength=350)
    label_sucesso.pack(pady=20)

    # Botão OK para fechar a janela
    botao_ok = tk.Button(sucesso_janela, text="OK", command=sucesso_janela.destroy, font=("Arial", 14), bg="green", fg="white")
    botao_ok.pack(pady=10)

    
    
# Função para calcular e verificar as respostas
def calcular():
    global etapa, erros, acertos
    if etapa == 1:
        resposta_usuario = resposta_5.get().strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp5]:
            mostrar_sucesso("Você acertou a primeira etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", 
                          "Dica: reescreva a equação substituindo o valor de x e efetue as operações.")
            erros += 1
    elif etapa == 2:
        resposta_usuario = resposta_6.get().strip().lower()
        if resposta_usuario == "8=2x+2":
            mostrar_sucesso("Você acertou a segunda etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", 
                          "Dica: reescreva a equação substituindo o valor de y.")
            erros += 1
    elif etapa == 3:
        resposta_usuario = resposta_6b.get().strip().lower()
        if resposta_usuario in ["2x=6", "6=2x"]:
            mostrar_sucesso("Você acertou a terceira etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", 
                          "Dica: subtraia 2 nos dois lados da equação.")
            erros += 1
    elif etapa == 4:
        resposta_usuario = resposta_6c.get().strip().lower()
        if resposta_usuario in ["x=3", "3"]:
            mostrar_sucesso("Você acertou a quarta etapa!")
            acertos += 1
            etapa += 1
            mudar_pagina(3)  # Muda para a página das perguntas 1 a 4
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", 
                          "Dica: divida por 2 nos dois lados da equação.")
            erros += 1
    elif etapa == 5:
        resposta_usuario = resposta_1.get().strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp1]:
            mostrar_sucesso("Você acertou a quinta etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", 
                          "Dica: iguale as equações das retas f e g.")
            erros += 1
    elif etapa == 6:
        resposta_usuario = resposta_2.get().strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp2]:
            mostrar_sucesso("Você acertou a sexta etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", 
                          "Dica: Isole o X em um dos lados da equação.")
            erros += 1
    
    elif etapa == 7:
        resposta_usuario = resposta_3.get().strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp3]:
            mostrar_sucesso("Você acertou a sétima etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Atenção", "Sua resposta não está correta, tente novamente. \nDica: Divida ambos os membros da equação por 4.")
            erros += 1    
           
    elif etapa == 8:
        resposta_usuario = resposta_4.get().strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp4]:
            mostrar_sucesso("Sucesso: Você acertou todas as etapas! \n \nO ponto de interseção das retas f e g é  x = -5 e y = 9")
            acertos += 1
            etapa += 1
            root.after(100, lambda: mudar_pagina(8))
            
        else:
            mostrar_aviso("Atenção", "Sua resposta não está correta, tente novamente. \nDica: substitua o valor de X em alguma das equações f ou g.")
            erros += 1    

# Função para mostrar as perguntas subsequentes na mesma página
def mostrar_proxima_pergunta():
    global etapa
    if etapa == 2:
        pergunta_6.pack(pady=20)
        resposta_6.pack()
        verificar_button_6.pack(pady=3)
    elif etapa == 3:
        pergunta_6b.pack(pady=20)
        resposta_6b.pack()
        verificar_button_6b.pack(pady=3)
    elif etapa == 4:
        pergunta_6c.pack(pady=20)
        resposta_6c.pack()
        verificar_button_6c.pack(pady=3)
    elif etapa == 5:
        pergunta_1.pack(pady=20)
        resposta_1.pack()
        verificar_button_1.pack(pady=3)
    elif etapa == 6:
        pergunta_2.pack(pady=20)
        resposta_2.pack()
        verificar_button_2.pack(pady=3)      
    elif etapa == 7:
        pergunta_3.pack(pady=20)
        resposta_3.pack()
        verificar_button_3.pack(pady=3)
    elif etapa == 8:
        pergunta_4.pack(pady=20)
        resposta_4.pack()
        verificar_button_4.pack(pady=3)

# Função para mudar de página
def mudar_pagina(pagina):
    frame_welcome.pack_forget()
    frame_1.pack_forget()
    frame_2.pack_forget()
    frame_results.pack_forget()

    if pagina == 1:
        frame_welcome.pack(fill="both", expand=1)
    elif pagina == 2:
        frame_1.pack(fill="both", expand=1)
    elif pagina == 3:
        frame_2.pack(fill="both", expand=1)
    elif pagina == 8:
        frame_results.pack(fill="both", expand=1)
        mostrar_grafico()  # Adiciona o gráfico à página de resultados

# Função para mostrar resultados gráficos
def mostrar_grafico():
    global acertos, erros

    # Dados para o gráfico
    categorias = ['Corretas', 'Erradas']
    valores = [acertos, erros]

    # Criação do gráfico
    fig, ax = plt.subplots()
    ax.bar(categorias, valores, color=['green', 'red'])
    ax.set_xlabel('Resultado')
    ax.set_ylabel('Número de Perguntas')
    ax.set_title('Resultados do Quiz')

    # Adiciona o gráfico ao frame de resultados
    canvas = FigureCanvasTkAgg(fig, master=frame_results)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Configuração inicial
etapa = 1
erros = 0
acertos = 0
resp_esp1 = ["3x+24=-x+4", "3x+24=4-x", "-x+4=3x+24", "-x+4=24+3x", "4-x=24+3x", "4-x=3x+24", "24+3x=-x+4", "24+3x=4-x"]
resp_esp2 = ["4x=-20", "-20=4x", "3x+x=4-24", "24-4=-x-3x"]
resp_esp3 = ["x=-5", "x = -5", "-5"]
resp_esp4 = ["y=9", "y = 9", "9"] 
resp_esp5 = ["y=7", "7", "y = 7", "y=2*2+3", "y = 2*2 + 3", "y=4+3", "y = 4 + 3"]
resp_esp6 = ["8=2x+2", "2x=6", "6=2x", "2x = 6", "6 = 2x"]

# Criar a janela principal
root = tk.Tk()
root.title("Tutor de Matemática")
root.configure(bg="lightgreen")

# Página de Boas-vindas
frame_welcome = tk.Frame(root)
welcome_label = tk.Label(frame_welcome, text="Bem-vindo ao Tutor de Matemática!", font=("Arial", 20))
welcome_label.pack(pady=20)

instructions_label = tk.Label(
    frame_welcome, 
    text="Este tutorial irá guiá-lo através de várias etapas para resolver equações e sistemas de equações. \n \nPara cada pergunta, insira a resposta na caixa fornecida e clique em 'Verificar'. \n \nSe você errar, receberá uma dica para tentar novamente. \n \nVamos começar!", 
    font=("Arial", 16)  
)
instructions_label.pack(pady=20)

start_button = tk.Button(frame_welcome, text="Começar", command=lambda: mudar_pagina(2), bg="blue", fg="white")
start_button.pack(pady=20)

# Página das Perguntas 1 a 4
frame_1 = tk.Frame(root, bg="lightgreen")
frame_1.pack(fill="both", expand=1)

pergunta_5 = tk.Label(frame_1, text="1) Encontre o valor de y fazendo a substituição necessária. \n \nDada a reta y = 2x + 3, qual o valor de y quando x = 2", bg="lightgreen", font=("Arial", 14))
pergunta_5.pack(pady=20)
resposta_5 = tk.Entry(frame_1, font=("Arial", 14))
resposta_5.pack()

pergunta_6 = tk.Label(frame_1, text="2) Dada a reta y = 2x + 2, encontre o valor de x quando y = 8. \n \nATENÇÃO: Nas próximas etapas insira apenas a substituição necessária.", bg="lightgreen", font=("Arial", 14))
resposta_6 = tk.Entry(frame_1, font=("Arial", 14))

pergunta_6b = tk.Label(frame_1, text="3) Nossa equação agora é 8 = 2x + 2", bg="lightgreen", font=("Arial", 14))
resposta_6b = tk.Entry(frame_1, font=("Arial", 14))

pergunta_6c = tk.Label(frame_1, text="4) Resolva x em 2x=6? \nInsira o valor final de x", bg="lightgreen", font=("Arial", 14))
resposta_6c = tk.Entry(frame_1, font=("Arial", 14))

verificar_button_5 = tk.Button(frame_1, text="Verificar", command=calcular, bg="blue", fg="white")
verificar_button_5.pack(pady=3)
verificar_button_6 = tk.Button(frame_1, text="Verificar", command=calcular, bg="blue", fg="white")
verificar_button_6b = tk.Button(frame_1, text="Verificar", command=calcular, bg="blue", fg="white")
verificar_button_6c = tk.Button(frame_1, text="Verificar", command=calcular, bg="blue", fg="white")

# Página das Perguntas 7 a 8
frame_2 = tk.Frame(root, bg="lightgreen")
frame_2.pack(fill="both", expand=1)

pergunta_1 = tk.Label(frame_2, text="5) Duas retas f e g se encontram e determinam um ponto de interseção. \nO Ponto de interseção é o lugar no plano cartesiano onde duas retas se encontram, \nEsse ponto é caracterizado por ter coordenadas (x , y) que satisfazem ao mesmo tempo as equações de duas retas. \n \nEncontre o ponto de interseção das retas f e g, sendo, f: y = 3x + 24 e g: y= -x + 4", bg="lightgreen", font=("Arial", 14))
resposta_1 = tk.Entry(frame_2, font=("Arial", 14))

pergunta_2 = tk.Label(frame_2, text="6) Nossa equação agora é 3x + 24 = -x + 4.", bg="lightgreen", font=("Arial", 14))
resposta_2 = tk.Entry(frame_2, font=("Arial", 14))

pergunta_3 = tk.Label(frame_2, text="7) Isolando x, temos a equação: 4x = -20, resolva para encontrar o valor de x. \nInsira o valor final de x.", bg="lightgreen", font=("Arial", 14))
resposta_3 = tk.Entry(frame_2, font=("Arial", 14))

pergunta_4 = tk.Label(frame_2, text="Agora, sabendo que x = -5 encontre o valor y. \nInsira o valor final de y.", bg="lightgreen", font=("Arial", 14))
resposta_4 = tk.Entry(frame_2, font=("Arial", 14))

verificar_button_1 = tk.Button(frame_2, text="Verificar", command=calcular, bg="blue", fg="white")
verificar_button_2 = tk.Button(frame_2, text="Verificar", command=calcular, bg="blue", fg="white")
verificar_button_3 = tk.Button(frame_2, text="Verificar", command=calcular, bg="blue", fg="white")
verificar_button_4 = tk.Button(frame_2, text="Verificar", command=calcular, bg="blue", fg="white")

# Página de Resultados
frame_results = tk.Frame(root)
resultados_button = tk.Button(frame_results, text="Mostrar Resultados", command=mostrar_grafico, bg="blue", fg="white")
resultados_button.pack(pady=20)

# Exibir a página de boas-vindas ao iniciar
mudar_pagina(1)

# Iniciar o loop da interface gráfica
root.mainloop()
