/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DAL;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 *
 * @author Aluno
 */
public class Conexao
{

    public Connection conn;
    public String mensagem;

    public Connection conectar()
    {
        this.mensagem = "";
        try
        {

            if (conn.isClosed() || conn == null)
            {
                conn = DriverManager.getConnection("jdbc:sqlserver://localhost\\LAB815\\SQLEXPRESS:1433;databaseName=dadosClimaticos;encrypt=false");
            }
        } catch (SQLException e)
        {
            this.mensagem = "Erro de conexão";

        }

        return conn;
    }

    public void desconectar()
    {
        try
        {
            if (!conn.isClosed())
            {
                conn.close();
            }
        } catch (SQLException e)
        {
            this.mensagem = "Erro no momento de fechar a conexão!";
        }

    }
}
