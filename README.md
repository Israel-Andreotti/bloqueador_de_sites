<h1>🛡️ Foco Total - Bloqueador de Sites</h1>
O Foco Total é uma ferramenta simples e eficaz desenvolvida em Python para ajudar a manter a concentração. Ele bloqueia o acesso ao YouTube (e suas variações) modificando o arquivo hosts do Windows, redirecionando o tráfego para o localhost.

<h1>✨ Funcionalidades</h1>
Bloqueio Instantâneo: Adiciona as URLs do YouTube ao arquivo de sistema para impedir o carregamento.

Desbloqueio Simples: Remove as restrições e restaura o acesso original.

Limpeza de Cache DNS: Executa automaticamente o comando ipconfig /flushdns para que as mudanças surtam efeito imediato.

Interface Amigável: Criada com Tkinter para uma experiência visual fácil de usar.

<h1>🚀 Como Executar</h1>
Pré-requisitos
Python 3.x instalado.

Privilégios de Administrador: Como o script altera um arquivo de sistema (C:\Windows\System32\drivers\etc\hosts), ele precisa ser executado como Administrador.

Passo a Passo
Baixe o arquivo gerenciador_sites.py

Abra o Prompt de Comando ou PowerShell como Administrador.

Navegue até a pasta do script e execute:

Bash
python gerenciador_sites.py
🛠️ Tecnologias Utilizadas
Python: Linguagem principal.

Tkinter: Para a interface gráfica (GUI).

OS Library: Para manipulação de caminhos de arquivos e comandos de sistema.

<h2>⚠️ Avisos Importantes</h2>
[!IMPORTANT]
Permissões: Se você não executar o script como administrador, verá uma mensagem de "Acesso Negado", pois o Windows protege o arquivo hosts contra modificações não autorizadas.

Navegadores: Alguns navegadores mantêm o site em cache. Se o bloqueio não funcionar de imediato após o uso, feche e abra o navegador novamente.

<h2>📝 Licença</h2>
Este projeto é para fins de estudo e uso pessoal. Sinta-se à vontade para expandir a lista de sites bloqueados no código fonte!
