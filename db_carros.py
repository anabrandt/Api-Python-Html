import oracledb
import traceback


def recupera_carros():
    sql = "select id, ano, montadora, modelo, marca, placa from carro"


def insert_carro(carro):
    ins = '''insert into carro(id, ano, montadora, modelo, placa)
            values(:id, :ano, :montadora, :modelo, :placa)'''
    try:
        with oracledb.connect(
            user="RM552283", password="170204", 
            dsn="oracle.fiap.com.br/orcl"
        ) as conexao:
            
            with conexao.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()

    except Exception as erro:
        traceback.print_exc()
        raise erro

if __name__ == '__main__':
    c = {"id": 5, "montadora": "Volkswagen", "modelo": "Amarok", 
         "ano": 2022, "placa": "LFG-6A45"}
    insert_carro(c)    