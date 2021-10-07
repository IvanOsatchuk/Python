from tkinter import *
import random


def gera_numero():
    return random.randrange(0, 9)


def gera_email():
    coluna1 = ["Caros colegas,", "Por outro lado,", "Nao podemos esquecer que,", "Do mesmo modo,",
               "A prática mostra que,", "Nunca é demais insistir que,", "A experiência mostra que,",
               "É fundamental ressaltar que,", "O incentivo ao avanço tecnológico, assim como,", "Assim mesmo,"]
    coluna2 = ["a complexidade dos estudos efetuados", "a execução deste projeto", "a atual estrutura da organização",
               "o novo modelo estrutural aqui preconizado", "o desenvolvimento de formas distintas de atuação",
               "a constante divulgação das informações", "a consolidação das estruturas",
               "a análise dos diversos resultados", "o início do programa de formação de atitudes",
               "a expansão de nossa atividade"]
    coluna3 = ["nos obriga à análise", "cumpre um papel essencial na formulação", "auxilia a preparação e estruturação",
               "contribui para a correta determinação", "assume importantes posições na definição",
               "facilita a definiçãoo", "prejudica a percepção da importância",
               "oferece uma boa oportunidade de verificação", "acarreta um processo de ·reformulação",
               "exige precisão e definição"]
    coluna4 = ["das nossas opções de desenvolvimento futuro.", "das nossas metas financeiras e administrativas.",
               "das atitudes e das atribuições da diretoria.", "das novas proposições.",
               "das opções básicas para o sucesso do programa.", "do nosso sistema de formação de quadros.",
               "das condições apropriadas para os negócios.", "dos índices pretendidos.", "das formas de ação.",
               "dos conceitos de participação geral"]

    return f"{coluna1[gera_numero()]} \n\n {coluna2[gera_numero()]} {coluna3[gera_numero()]} {coluna4[gera_numero()]} \n\nAtt,"

def setTextInput(text):
    display.delete(1.0,"end")
    display.insert(1.0, text)

def clipboard_get():
    
    display.clipboard_append(display.get(1.0, END))
    display.update() 
    display.delete(1.0,"end")
    display.insert(1.0, 'Texto copiado')


root = Tk()
root.title("Gerador de E-mail")
root.geometry('400x400+400+100')

janela = Frame(root)
janela.pack(fill=BOTH)

titulo = Label(
    janela,
    text="Gerador de e-mails para ganhar promoção",
    font=("Arial", 14)
).pack(side=TOP, pady=15)


top = Frame(janela)
top.pack(expand=1, fill=BOTH, side=TOP)

titulo = Label(
    janela,
    text="Desenvolvido por Corporação Osatchuk",
    font=("Arial", 10)
).pack(pady=25,side=BOTTOM)

bottom = Frame(janela)
bottom.pack(fill=BOTH, side=BOTTOM)

display = Text(top, wrap=WORD, width=40, height=10,  relief="groove",)
display.pack(padx=30, pady=15)


botao_gerar_email = Button(bottom, text="Gerar Email", borderwidth=2, relief="raised",command=lambda:setTextInput(gera_email())).pack(pady=10, padx=10, expand=True, fill=X, side=LEFT)

botao_copiar = Button(bottom, height=1, text="Copiar texto", borderwidth=2, relief="raised",command=lambda:clipboard_get()).pack(pady=10, padx=10, expand=True, fill=X, side=LEFT)

botao_sair = Button(bottom, text="Sair", borderwidth=2, relief="raised", command=root.destroy).pack(pady=10, padx=10, expand=True, fill=X, side=LEFT)


janela.mainloop()
