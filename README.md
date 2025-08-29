# Btime Scrapping

Este projeto realiza uma coleta de dados meteorológicos no site do INMET (Instituto Nacional de Meteorologia) e salva os resultados em um arquivo CSV.

## Requisitos

- Python 3.10 ou superior
- [Google Chrome](https://www.google.com/chrome/) instalado no sistema

## Instalação

1. Clone o repositório e entre na pasta do projeto:
   ```bash
   git clone <url-do-repositorio>
   cd Btime_scrapping
   ```
2. Crie e ative um ambiente virtual (opcional, porém recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux ou macOS
   .venv\Scripts\activate     # Windows
   ```
3. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```
4. Instale os navegadores necessários do Playwright:
   ```bash
   playwright install
   ```

## Configuração opcional

O script utiliza variáveis de ambiente que podem ser definidas em um arquivo `.env` na raiz do projeto.

```env
URL=https://tempo.inmet.gov.br/
PRODUCT=Condições de Tempo Registradas nas Capitais
DAYS_BEFORE=0
```

- `URL`: Endereço da página a ser acessada.
- `PRODUCT`: Nome do produto a ser filtrado.
- `DAYS_BEFORE`: Quantidade de dias anteriores à data atual para filtrar os dados.

Os valores acima são os padrões utilizados caso o arquivo `.env` não seja fornecido.

## Executando o script

Após a instalação e configuração, execute:

```bash
python main.py
```

O navegador será aberto para realizar a coleta de dados. Ao final, um arquivo CSV será criado na pasta `output/` e os logs serão armazenados em `logs/`.

## Observações

- Caso esteja executando em um servidor ou ambiente sem interface gráfica, será necessário ajustar a configuração do Playwright para usar o modo `headless` ou um navegador compatível.