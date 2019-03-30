Analise de Logs
=================================


Udacity - Desenvolvedor Web Full-Stack Nanodegree Program
---------------------------------------------
Projeto 3: Analise de Logs com Python e SQL

Este projeto tem como objetivo construir uma ferramenta interna de relatórios com Python e SQL que utiliza informações consultadas no banco de dados de um site de jornal para determinar que tipo de artigos e o autor que os leitores preferem e o dia em que o site experimentou um alto nível de erros de solicitação do usuário.

Pre-requisitos
------------

+ [Python 2.7.12](https://www.python.org/downloads/release/python-2712/) instalado.
+ A versao pode ser verificada executando o comando abaixo:
```bash
$ python -V
```
+ [Virtual Box](https://www.virtualbox.org/wiki/Downloads) instalado.
+ [Vagrant](https://www.vagrantup.com/downloads.html) instalado.
+ [Arquivos de cofiguracao da VM](https://github.com/udacity/fullstack-nanodegree-vm).
+ [Arquivo do log do bando de dados para PostgreSQL](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) instalado.
+ [PostgreSQL 9.5.14](https://www.postgresql.org/download/linux/) instalado.
+ A versao pode ser verificada executando o comando abaixo dentro do PostgreSQL:
```bash
=> SELECT version();
```
+ [Instalar a lib Python psycopg2](https://pypi.org/project/psycopg2/).
+ [Instalar a lib Python pycodestyle](https://pypi.org/project/pycodestyle/).
+ [Instalar a lib Python PrettyTable](https://pypi.org/project/PrettyTable/).

Uso
-----
* Instalar o Virtual Box e depois o Vagrant, se já não estiver instalada.
* Baixar os [Arquivos de configuração da VM](https://github.com/udacity/fullstack-nanodegree-vm).
* Decompactar o arquivo fullstack-nanodegree-vm-master.zip.
* Baixar e descopactar o [Arquivo do log do bando de dados para PostgreSQL](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) para a pasta /vagrant.
* Dentro do Shell ir para a pasta FSND-Virtual-Machine/vagrant/.
```bash
$ cd FSND-Virtual-Machine/vagrant/
```
* Inicialize a VM (depo demorar um pouco, principalmente se for a primeira vez, pois vai baixo e instalar o Ubuntu Linux.
```bash
$ vagrant up
```
* Faça o ogin an VM.
```bash
$ vagrant ssh
```
* Entre na pasta partilhada /vagrant e carregue o banco de dados [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
```bash
$ cd /vagrant
$ psql -d news -f newsdata.sql
```
* Execute o arquivo analise_log.py pela linha de comando.
* Os resultados irao aparecer automaticamente na tela.
```bash
$ 
```

