# Projeto de Teste - Definições

## Software

O software que será testado consiste no site do Correios, sendo acessível via [link](https://www.correios.com.br/).

### Descrição geral

Consiste em uma plataforma de browser destinada a atender às necessidades da Empresa Brasileira de Correios e Telégrafos (Correios) cuja função pública está voltada para transporte de produtos para território brasileiro e internacional. Dessa maneira, tal software, de modo geral, é a ferramenta de intermédio remoto entre a estatal e os consumidores do serviço desta.

## Funcionalidades

Serão testadas as seguintes funcionalidades pertencentes ao software web dos Correios: 

- **Acompanhe seu objeto**: funcionalidade que permite ao usuário rastrear sua encomenda a partir de um código de rastreio ou seu próprio CPF.
- **Busca CEP**: funcionalidade que permite obter um endereço a partir de um CEP, ou o contrário, obter um CEP a partir de um endereço inserido.
- **Simulador de Preços e Prazos Nacionais**: funcionalidade que permite simular os preços e os prazos de entrega para uma encomenda enviada em solo nacional.
- **Simulador de Preços e Prazos Internacionais**: funcionalidade que permite simular os preços e os prazos de entrega para uma encomenda enviada para territórios internacionais.
- **Busca Agências por Localidade**: funcionalidade que permite buscar as agências presentes em uma localidade específica inserida pelo usuário através das informações de estado, município e bairro.

## Tecnologias empregadas

As tecnologias empregadas para testar as funcionalidades serão:

- **.NET Framework**: framework da Microsoft que busca unificar todo o desenvolvimento em um único ambiente, será utilizado para a criação do projeto de testes automatizados assim como a implementação dos mesmos.
- **Bogus Framework**: framework utilizado para gerar dados falsos que serão acoplados nos testes automatizados.
- **Selenium**: framework poderoso para execução de testes automatizados em interfaces web que, em conjunto com .NET Framework, implementará os testes descritos nos cenários de testes.
- **HackMD**: plataforma onde serão escritos os cenários de testes, assim como todo o trabalho em .md.

## Cronograma

| # | Funcionalidade                           | Data_Início | Data_Fim   | Responsável    |
| - | ---------------------------------------- | ----------- | ---------- | -------------- |
| 1 | Acompanhe seu Objeto (Rastreamento)      | 07/02/2022  | 11/02/2022 | Lucas Borges   |
| 2 | Busca CEP                                | 14/02/2022  | 18/02/2022 | Abigail Arruda |
| 3 | Simulador Preços e Prazos Nacionais      | 21/02/2022  | 25/02/2022 | Jacob Ferraz   |
| 4 | Simulador Preços e Prazos Internacionais | 28/02/2022  | 04/03/2022 | Victor Melo    |
| 5 | Busca Agências por Localidade            | 07/03/2022  | 11/03/2022 | Heitor Melo    |