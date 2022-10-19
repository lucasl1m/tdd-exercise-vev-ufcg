# Filtro de Faturas

Deve-se implementar um filtro de faturas. Uma fatura contém um código, um valor, uma data, e pertence a um cliente. Um cliente tem um nome, data de inclusão e um estado.

O filtro deverá então, dado uma lista de faturas, remover as que se encaixam em algum dos critérios
abaixo:

Se o valor da fatura for menor que 2000;
Se o valor da fatura estiver entre 2000 e 2500 e a data for menor ou igual a de um mês atrás;
Se o valor da fatura estiver entre 2500 e 3000 e a data de inclusão do cliente for menor ou igual a 2 meses atrás;
Se o valor da fatura for maior que 4000 e pertencer a algum estado da região Sul do Brasil.
