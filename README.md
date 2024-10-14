
# Mercado Livre Data Scraper com AvantPro

Este é um script em Python que lê dados do Mercado Livre utilizando a extensão **AvantPro**.

## Pré-requisitos

Para executar este script, você precisará dos seguintes itens:

- **Python** (versão recomendada: 3.12 ou superior)
- **Pip** (gerenciador de pacotes Python)

## Configuração

### 1. Instalar Python e Pip

Se ainda não tiver o Python e o Pip instalados, você pode baixá-los [aqui](https://www.python.org/downloads/).

### 2. Arquivo `.env`

Na raiz do projeto, crie um arquivo `.env` contendo suas credenciais de login para a extensão **AvantPro**. O arquivo deve seguir o seguinte formato:

```env
LOGIN="emaildeexemplo@gmail.com"
```

### 3. Instalação das Dependências

Após configurar o ambiente, execute o script `Instalar Dependências.bat` para instalar as bibliotecas necessárias.

```bash
./Instalar Dependências.bat
```

### 4. Inserir Produtos

Você já pode começar a inserir produtos dentro da planilha `avantpro.csv` no diretório `planilhas/`.

## Funcionalidades

O script atualmente realiza a raspagem e análise de dados dos produtos no Mercado Livre com as seguintes informações:

- Quantidade de anúncios sem medalha
- Menor preço encontrado
- Maior preço encontrado
- Nível de concorrência

## Como Executar

Após realizar todas as configurações acima, execute o script bash Analise Avant Pro.bat para iniciar a coleta dos dados.

## Contribuição

Se quiser contribuir com o projeto, sinta-se à vontade para abrir um **Pull Request** ou relatar um **Issue**.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
