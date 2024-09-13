/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DAL;

import java.sql.Connection;
import java.sql.PreparedStatement;
import modelo.MdDadosClimaticos;

/**
 *
 * @author Aluno
 */
public class ClimaDAO
{

    public String mensagem;
    Conexao conex = new Conexao();

    public void cadastrar(MdDadosClimaticos md)
    {
        this.mensagem = "";
        try
        {
            Connection conn = conex.conectar();

            String instrucao = "insert into dados (temperatura, humidade, precipitacao) values (?,?,?)";

            PreparedStatement stmt = conn.prepareStatement(instrucao);
            stmt.setFloat(0, md.temperatura);
            stmt.setFloat(1, md.humidade);
            stmt.setFloat(2, md.precipitacao);

            stmt.execute();
            conex.desconectar();
            this.mensagem = "Dados cadastrados com sucesso!  :D";

        } catch (Exception e)
        {
            this.mensagem = "Erro de Cadastro, tente novamente ou confira os valores.  :[";
        }

    }
}
