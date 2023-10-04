import sqlite3 as sql 

class Conexao:
    def __init__(self, database: str, username: str, password: str) -> None:
        self.database = database
        self.username = username
        self.password = password
        self.connection = None
        self.cursor = None
        
    def login(self, username:str, password:str) -> bool:
        return True if self.username == "admin" and self.password == "1234" else False

    def conectar(self) -> bool:
        self.connection = sql.connect(self.database)
        self.cursor = self.connection.cursor()
        return True
        
    def desconectar(self) -> bool:
        self.connection.close()
    
    
    def inserir_dado(self, **valores: dict) -> dict:
        self.conectar()
        self.cursor.execute(
            "INSERT INTO produtos (nome, temperatura, comissao, fundofunil, pesquisas, paginavenda) VALUES(?, ?, ?, ?, ?, ?)",
            (valores['nome'], valores['temperatura'], valores['comissao'], valores['fundofunil'], valores['pesquisas'], valores['paginavenda']))
        self.connection.commit()
        self.desconectar()
        
        return valores
    
    
    def atualizar_dado(self, id:int, **valores:dict) -> None:
        self.conectar()
        self.cursor.execute("UPDATE produtos (nome, temperatura, comissao, fundofunil, pesquisas, paginavenda) WHERE id = ? VALUES (?, ?, ?, ?, ?, ?)",(id, valores['nome'], valores['temperatura'], valores['comissao'], valores['fundofunil'], valores['pesquisas'], valores['paginavenda']))
        self.connection.commit()
        self.desconectar()
        
        return valores 
        
    
    def apagar_dado(self, id:int) -> None:
        backup = self.consultar_dado(id)
        self.conectar()
        self.cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
        self.connection.commit()
        self.desconectar()
        
        return backup
        
        
    def consultar_dado(self, nome:str) -> list:
         self.conectar()
         consulta = self.cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome,)).fetchall()
         self.desconectar()
         
         return consulta
         
         
    def limpar_tabela(self) -> None:
        self.conectar()
        self.cursor.execute("DELETE * FROM produtos")
        self.connection.commit()
        self.desconectar()
        

    def consultar__tabela(self) -> None:
        self.conectar()
        consulta = self.cursor.execute("SELECT * FROM produtos").fetchall()
        self.desconectar()
        
        return consulta
        


if __name__ == "__main__":
    pass