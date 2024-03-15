--Criando e Manipulando Tabelas em SQL.


--Criar Tabela:

  create table pessoas
    (
    	idPessoa int primary key identity(1,1),
    	nome varchar(50),
    	rg varchar(10),
    	cpf varchar(12)
    )
    go


--Pesquisar Tabelas:
  
  Select * from pessoas


--Inserir valores de forma simples:
  
  insert into pessoas
  values
  ('  Nome  ','  CPF  ','  RG  ')


--Inserir valores de ordenadamente:

  insert into pessoas(nome, rg, cpf)
  values
  ('  Nome  ','  CPF  ','  RG  '),
  ('  Nome  ','  CPF  ','  RG  '),
  ('  Nome  ','  CPF  ','  RG  ')


-- Deletando Valores da Tabela:

drop table pessoas -- (╯°□°)╯︵ ┻━┻

delete from pessoas	-- apaga especifico
where idPessoa = 6


--Ordenando Dados :
  
  select * from pessoas
  order by nome asc --Crescente(Padrão)
  order by nome desc --Decrescente

	  
-- Pesquisa especifica(Primeiro da Lista ordenado pelo NOME e RG):

  Select top 1 * from pessoas
  where nome = 'Manoel'
  order by rg


-- Pesquisa por trechos:

  Select top 1 * from pessoas
  where nome like 'M%' -- Primeira Letra
  
  where nome like '__N%'-- 3ª Letra
  
  where nome like '%L' -- Termina com o caracter especificado
    
  
-- Lista todos os valores em maiusculo:

  select UPPER(nome) from pessoas


-- Mostrar valores sem repetição:

  select distinct(nome) from pessoas
