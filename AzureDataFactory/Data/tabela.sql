

# Cria a tabela no banco de dados
CREATE TABLE dbo.musicos
(
    ID int IDENTITY(1,1) NOT NULL,
    Nome varchar(100),
    SobreNome varchar(100)
)
GO

# Cria o índice
CREATE CLUSTERED INDEX IX_musicos_ID ON dbo.musicos (ID);


