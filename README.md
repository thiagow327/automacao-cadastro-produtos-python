Automatizador de Cadastro de Produtos

Este projeto Python visa automatizar o processo de cadastro de produtos em um sistema, eliminando tarefas manuais demoradas e sujeitas a erros. Com o uso das bibliotecas pyautogui, pillow, e mouseinfo, o código permite o cadastro eficiente e preciso de produtos a partir de um arquivo de texto (produtos.txt) com os seguintes campos: nome do produto, quantidade e preço.

Pré-requisitos: Python 3.x

Bibliotecas: pyautogui, pillow, mouseinfo

Como utilizar: Certifique-se de ter o Python instalado em seu sistema;

Instale as bibliotecas necessárias através do seguinte comando:
Copy code
pip install pyautogui pillow mouseinfo

Clone este repositório ou baixe o arquivo do código (app.py) e o arquivo de dados (produtos.txt).

Certifique-se de que o arquivo produtos.txt contém as informações dos produtos a serem cadastrados, separadas por vírgula e cada produto em uma nova linha (exemplo: produto1,10,100.50).

Execute o código main.py para iniciar o processo de automação.

Observações
Antes de executar o código, certifique-se de que a janela do sistema de cadastro esteja visível e posicionada corretamente na tela.
As coordenadas de cliques (pyautogui.click(x, y)) utilizadas no código podem variar dependendo do layout do sistema de cadastro. É recomendado ajustá-las conforme necessário para a correta interação com os elementos da interface.

Aviso
O uso inadequado deste script em sistemas ou plataformas protegidas ou sem permissão pode violar os termos de serviço e políticas de uso, resultando em consequências legais. Este script destina-se apenas para fins educacionais e de automação em ambientes controlados. O desenvolvedor não assume qualquer responsabilidade pelo uso indevido deste código.

Aproveite a automação para simplificar o cadastro de produtos e ganhar mais produtividade!
