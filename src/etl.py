import pandas as pd
from sqlalchemy import create_engine

# Conexão com a tua senha: adweb2000
engine = create_engine("postgresql://postgres:123456@127.0.0.1:5432/iot_db")

print("Lendo arquivo CSV...")

# Carrega os dados da pasta data
df = pd.read_csv("data/IOT-temp.csv")

# Renomeia as colunas para evitar o erro da barra '/' que viste antes
df = df.rename(columns={
    'room_id/id': 'device_id',
    'noted_date': 'timestamp',
    'temp': 'temperature',
    'out/in': 'location'
})

print("Enviando dados para o PostgreSQL...")

try:
    # Salva na tabela temperature_readings
    df.to_sql("temperature_readings", engine, if_exists="replace", index=False)
    print("SUCESSO: Dados enviados!")
except Exception as e:
    print(f"ERRO: {e}")
