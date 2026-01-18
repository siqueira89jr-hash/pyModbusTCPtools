from pyModbusTCPtools import ModbusTCPResiliente

# Configuração do cliente Modbus TCP
client = ModbusTCPResiliente(
    host="192.168.18.98",  # IP do CLP
    port=502,
    unit_id=1,
    console=True          # mostra logs no console (opcional)
)

# Leitura de 1 coil a partir do endereço 0
result = client.read_coils_safe(addr=0, count=1)

if result is not None:
    coil_0 = bool(result[0])
    print(f"Coil 0 = {coil_0}")
else:
    print("Falha na leitura do Coil 0")

# Fecha a conexão explicitamente (opcional)
client.close()
