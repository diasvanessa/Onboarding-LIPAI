O que você conseguiu enxergar no debugger que não ficava tão claro apenas executando o programa normalmente (sem depuração)?
O fluxo real de execução, como uma função chama outra e passa os valores e essa trabalha em cima deles. 

Em quais situações você acha mais prático usar o pdb pela linha de comando e em quais prefere o debugger visual do VS Code?
O pdb é útil quando estou usando o código em um terminal sem conseguir utilizar uma interface gráfica ou eu quero investigar rapidamente algum valor específico. O vscode é útil em projetos mais complexos, com várias funções se interligando e também é menos complexo que o pdb. 

Houve algum erro ou comportamento inesperado nos seus exercícios que você só percebeu por causa da depuração? Descreva brevemente.
Sim, no caso quando recebe dados do usuário e usa pra converter pra float, se o usuário digitar um caracter inválido o programa lança uma exceção, o que foi percebido durante a depuração.