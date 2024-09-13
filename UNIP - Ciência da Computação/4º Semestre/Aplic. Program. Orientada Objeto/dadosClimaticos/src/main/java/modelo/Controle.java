/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modelo;

import DAL.ClimaDAO;
import java.util.List;

/**
 *
 * @author Aluno
 */
public class Controle
{

    public String mensagem;

    public void cadastrar(List<String> listDadosClimaticos)
    {
        Validacao validacao = new Validacao();
        validacao.validar(listDadosClimaticos);

        if (validacao.mensagem.equals(""))
        {
            MdDadosClimaticos md = new MdDadosClimaticos();
            md.setTemperatura(validacao.temperatura);
            md.setHumidade(validacao.humidade);
            
            ClimaDAO climaDao = new ClimaDAO();
            climaDao.cadastrar(md);
            this.mensagem = climaDao.mensagem;
        } else
        {
            this.mensagem = validacao.mensagem;
        }
    }
}
