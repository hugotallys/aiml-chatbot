# aiml-chatbot

Chatbot simples criado para disciplina de Inteligência Artificial - ECOM031 utilizando o interpretador AIML `python-aiml`. O objetivo do chatbot é solucionar o seguinte problema de negócio.

---

## Problema de negócio 3

## Banco Financeiro
* Crie uma aplicação para um banco que será responsável por abrir uma conta corrente para um usuário.
* Verifique se o usuário já tem conta em outros bancos.
* Caso o usuário tenha conta em outros bancos verifique se ele quer fazer portabilidade
* Verifique o nome do correntista.
* Verifique qual o saldo que será depositado, zero ou um outro valor inicial.
* Verifique se o usuário quer um empréstimo.
* Ao final informe o nome do correntista, se ele quis um empréstimo e se ele fez portabilidade e o valor inicial da conta.

## Instruções

Para executar a aplicação é necessário ter o pacote `Flask` instalado. Se estiver usando _pip_ basta rodar `pip install -r requirements.txt` e em seguida `python app.py`. Para interagir basta acessar http://127.0.0.1:5000/ no navegador. Todo o código _front-end_ foi retirado do repositório [coronabot-chatterbot](https://github.com/huzaifsayed/coronabot-chatterbot), sofrendo somente pequenas alterações.