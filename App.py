import PySimpleGUI as sg
import clipboard, lorem, io, webbrowser
# 
#      _                               ___                           
#     | |    ___  _ __ ___ _ __ ___   |_ _|_ __  ___ _   _ _ __ ___  
#     | |   / _ \| '__/ _ \ '_ ` _ \   | || '_ \/ __| | | | '_ ` _ \ 
#     | |__| (_) | | |  __/ | | | | |  | || |_) \__ \ |_| | | | | | |
#     |_____\___/|_|  \___|_| |_| |_| |___| .__/|___/\__,_|_| |_| |_|
#                                         |_|                        
#       ____                           _             
#      / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
#     | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
#     | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
#      \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
#                                                    

def lorem_ipsum_create():
    return lorem.paragraph()

text_inicial = ''

sg.theme('Reddit')

menu_def =[
    ['&Arquivo', ['&Novo Ctrl-N', '&Salvar Ctrl-S', '&Sair']],
    ['&Ajuda', ['&Manual do Software', '&Sobre o Autor', ['&Linkedin', '&GitHub']]]
    ]

layout = [
    [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
    [sg.Text('Quantos parágrafos de Lorem Ipsum:'), sg.Combo(['3', '5', '9', '12', '15', '25'], key='-paragrafos-', default_value='3')],
    [sg.Multiline(lorem_ipsum_create(), size=(75, 15), key='-texto-')],
    [sg.Button('Gerar Lorem Ipsum'), sg.Button('Copiar Texto'), sg.Button('Salvar Texto')]
    ]

window = sg.Window('Lorem Ipsum Generator', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Sair'):
        break
    
    if event in ('Gerar Lorem Ipsum'):
        for linha in range(0, int(values['-paragrafos-'])):
            text_inicial+=lorem_ipsum_create()+'\n\n'
            window['-texto-'].update(text_inicial)

    if event in ('Novo Ctrl-N'):
        window['-texto-'].update(lorem_ipsum_create())
    
    if event in ('Salvar Texto', 'Salvar Ctrl-S'):
        with io.open("lorem_ipsum.txt", "w", encoding="utf8") as f:
            f.write(values['-texto-'])
            f.close()
        sg.Popup('Texto Salvo',
                 '''
O Texto Foi salvo como lorem_ipsum.txt e está em alguma pasta de seu computador, geralmente a pasta 'home', mas isso depende de qual sistema operacional você está a usar.
Você pode usar o notepad, gedit, mousepad ou qualquer editor de texto para ler seu conteúdo...
''')
        
    if event in ('Copiar Texto'):
        clipboard.copy(values['-texto-'])
        sg.Popup('Texto copiado para área de transferência',
                 '''
O texto já está na área de transferência de seu computador, cole onde quiser com a combinação de teclas [Ctrl+V] ou clique com o botão direito do mouse e escolha 'colar' no menu suspenso...
''')
        
    if event in ('Manual do Software'):
        sg.Popup('Manual do Software LOREM IPSUM GENERATOR',
                 '''
    COMO O LOREM IPSUM GENERATOR FOI FEITO?
    
- O Lorem Ipsum Generator foi feito inteiramente em Python;
- A interface gráfica do software é obtida graças à biblioteca PySimpleGui;
- Foi utilizada as libs (bibliotecas) lorem (para gerar o texto) e clipboard (para permitir a cópia do texto para a área de trabalho)

    
    PARA QUE FINALIDADE O LOREM IPSUM GENERATOR FOI CRIADO?
    
- O LOREM IPSUM GENERATOR foi criado para aqueles que precisam de texto rápido para exemplos, sem correr o risco de cair em crimes como plágio ou ferir direitos autorais...
- LOREM IPSUM GENERATOR é opensource e seu conteúdo poderá ser utilizado para qualquer finalidade...

    
    COMO USAR O LOREM IPSUM GENERATOR?

- Usar o LOREM IPSUM GENERATOR é muito simples:
1. Após abrir o software, escolha a quantidade de parágrafos desejados usando o dropdown. Você também pode digitar a quantidade de parágrafos que desejar...
2. Clique no botão [Gerar Lorem Ipsum] e seu texto está pronto...
3. Para copiar todo o texto para a área de transferência use o botão [Copiar Texto], ele corresponde ao CTRL+C do teclado...
4. Se quiser salvar o texto, clique no botão [Salvar Texto] ou use o menu: Arquivo>Salvar...

    Obrigado por usar o LOREM IPSUM GENERATOR S2
''')
        
    if event in ('Linkedin'):
        webbrowser.open('https://www.linkedin.com/in/elizeu-barbosa-abreu-69965b218/')
                 
    if event in ('Copiar Texto'):
        webbrowser.open('https://github.com/elizeubarbosaabreu/Lorem-Ipsum-Generator.git')
        
window.close()
