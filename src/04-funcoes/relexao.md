1 Qual função é mais flexível em relação ao uso: a do ex01 (que imprime) ou a do ex02 (que retorna o valor)? Por quê?
    A do ex02 que retorna o valor, pois isso é útil para usar o valor retornado em outras funções, pra salvar no banco de dados, enviar por e-mail, salvar em arquivo e etc.

2 Qual abordagem é mais flexível: a do ex02 (3 parâmetros fixos) ou a do ex03/ex04 (que permitem número variável de argumentos)
    A que permite número variável de argumentos, pois aceita qualquer quantidade de valores, a mesma função funciona para poucos ou muitos argumentos e é mais genérica, sendo reutilizável e fácil de manter.

3 As funções do ex03 e ex04 permitem enviar um número variável de parâmetros (tupla ou *args). Em que situações você prefere cada forma? Justifique.
    O uso da tupla é preferível quando os dados já estão agrupados e quando o chamador decide explicitamente passar um grupo de valores.
    O uso de *args é preferível quando o número de argumentos é desconhecido ou opcional e quando deseja uma sintaxe mais simples para o usuário da função.