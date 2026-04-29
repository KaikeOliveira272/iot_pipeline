📊 IoT Temperature Monitoring Pipeline
Este projeto implementa um pipeline de dados IoT completo, abrangendo desde a ingestão de um arquivo CSV até a visualização interativa em um dashboard web. O objetivo é processar grandes volumes de dados térmicos de sensores utilizando tecnologias escaláveis de Big Data.


📂 Estrutura de Pastas
src/: Scripts Python (etl.py, app.py) e arquivo de definição de banco (database.sql).
data/: Diretório contendo a fonte de dados IOT-temp.csv.


🚀 Guia de Execução
Preparação do Banco (Docker): Suba o container do PostgreSQL via terminal: docker run --name postgres-iot -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres.

Configuração do Python: Instale as bibliotecas necessárias: pip install 

Processamento e Carga (ETL): Rode o script para enviar os dados do CSV para o banco: python src/etl.py.

Criação das Views Analíticas: Execute as definições SQL para preparar as visualizações no banco: docker exec -i postgres-iot psql -U postgres -d iot_db < src/database.sql.

Visualização no Dashboard: Inicie a interface gráfica: streamlit run src/app.py.


📈 Insights Gerados
O dashboard apresenta a média térmica por dispositivo, o volume de ingestão horária (Big Data), a variação entre máximas e mínimas, além de um sistema automático de detecção de anomalias (alertas para temperaturas >35°C ou <15°C).


