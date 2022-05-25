# Esteganografia

<b>Dupla:</b> João Vitor Specht Kogut e Nicole Magagnin <br>

O objetivo do trabalho da M2.2 é trabalhar com esteganografia em imagens. Dada uma imagem, devem ser implementados os algoritmos para esconder uma mensagem e para ler uma mensagem escondida.<br>

Essa mensagem deve ser escondida no último bit da cor vermelha (não precisa trabalhar com binários, somente com valores pares e ímpares) e deve ser retirada uma mensagem de lá.<br>

Precisam ser criadas duas funções: uma que crie uma lista de inteiros (com valores de 0 ou 1) composta pelos últimos dígitos da cor vermelha da imagem; a outra função dever receber uma lista de inteiros como parâmetro e alterar o último bit da cor vermelha da imagem para cada elemento. Lembre-se que a lista não vai ser grande o suficiente para toda a imagem, então altere a imagem só até a mensagem terminar.
<br>
Não precisam se preocupar com a conversão da mensagem de texto para a lista de bits e nem o contrário, abaixo já existem essas duas funções prontas: gerar_mensagem() recebe uma string por parâmetro e gera uma lista de inteiros e converter_mensagem() recebe uma lista de inteiros e gera uma mensagem.
