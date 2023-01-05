import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost', database='siperj_bd', user='root', password='')
    cursor = con.cursor()

    def consulta_bairro():
        cursor.execute("SELECT * FROM bairro")
        return cursor.fetchall()
    
    linhas = consulta_bairro()

    def areas_de_planejamento():
        comando = "SELECT bairro.Nome, area_de_planejamento.Nome"
        comando += " FROM bairro"
        comando += " INNER JOIN regiao_administrativa ON bairro.fk_Regiao_Administrativa_Numero = regiao_administrativa.Numero"
        comando += " INNER JOIN area_de_planejamento ON area_de_planejamento.Numero = regiao_administrativa.fk_Area_de_Planejamento_Numero ;"
        cursor.execute(comando)
        return cursor.fetchall()

    def atividade_economica():
        comando = "SELECT Atividade_Economica.Nome, Table_A .Quantidade FROM (SELECT * FROM Bairro INNER JOIN Registra ON fk_bairro_numero=Bairro.numero "
        comando += "WHERE Bairro.Nome='Bangu') AS Table_A INNER JOIN Atividade_Economica ON Atividade_Economica.Codigo=Table_A.fk_atividade_economica_codigo;" 
        cursor.execute(comando)
        return cursor.fetchall()

    def IDS_medio_RA():
        comando = "SELECT DISTINCT Regiao_Administrativa.Nome,Table_A.IDS "
        comando +=    "FROM (SELECT DISTINCT fk_regiao_administrativa_numero,avg(Indice_de_Desenvolvimento_Social) as IDS "
        comando +=    "FROM Bairro "
        comando +=    "GROUP BY fk_regiao_administrativa_numero "
        comando +=    "ORDER BY IDS asc) AS Table_A INNER JOIN Regiao_Administrativa ON Table_A.fk_regiao_administrativa_numero=Regiao_Administrativa.Numero;"
        cursor.execute(comando)
        return cursor.fetchall()

    def pobreza_AP():
        comando = "(SELECT fk_Area_de_Planejamento_Numero,Area_de_Planejamento.Nome,sum(Familias_em_Extrema_Probreza) "
        comando += "FROM Bairro INNER JOIN Regiao_Administrativa ON Regiao_Administrativa.Numero=fk_Regiao_Administrativa_Numero "
        comando += "INNER JOIN Area_de_Planejamento ON Area_de_Planejamento.Numero=fk_Area_de_Planejamento_Numero "
        comando += "GROUP BY fk_Area_de_Planejamento_Numero);"
        cursor.execute(comando)
        return cursor.fetchall()

    def atividades_zero(num_bairro):
        comando = "SELECT atividade_economica.Nome "
        comando +=        "FROM atividade_economica "
        comando +=        "LEFT OUTER JOIN "
        comando +=        "(SELECT Table_A.Nome "
        comando +=        "FROM "
        comando +=        "(SELECT fk_Bairro_Numero, fk_Atividade_Economica_Codigo, atividade_economica.Nome "
        comando +=            "FROM registra "
        comando +=            "INNER JOIN atividade_economica " 
        comando +=            "ON atividade_economica.Codigo = registra.fk_Atividade_Economica_Codigo "
        comando +=            "ORDER BY fk_Atividade_Economica_Codigo ASC) AS Table_A "
        comando +=        "INNER JOIN bairro "
        comando +=        "ON bairro.Numero = Table_A.fk_Bairro_numero "
        comando +=        "WHERE Table_A.fk_Bairro_Numero = "+str(num_bairro)
        comando +=        ") AS Table_B "
        comando +=        "ON Table_B.Nome = atividade_economica.Nome;"
        cursor.execute(comando)
        return cursor.fetchall()

    def getNomeBairro(num_bairro):
        comando = "SELECT Nome FROM bairro WHERE Numero="+str(num_bairro)+';'
        cursor.execute(comando)
        return cursor.fetchall()[0][0]


    #print(pobreza_AP())
    #print(IDS_medio_RA())
    #print(atividade_economica())
    #print(areas_de_planejamento())
    #print(getNomeBairro(5))
except Error as e:
    print("Erro ao abrir Banco de Dados",e)

'''finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão MySQL encerrada")
'''