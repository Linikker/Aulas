/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modelo;

import java.util.List;

/**
 *
 * @author Aluno
 */
public class Validacao
{

    public float temperatura;
    public float humidade;
    public float precipitacao;

    public String mensagem;

    public void validar(List<String> listDadosClimaticos)
    {
        if()
        try
        {
            this.temperatura = toString(listDadosClimaticos.get(0));
            this.humidade = Float.parseFloat(listDadosClimaticos.get(1));
            this.precipitacao = Float.parseFloat(listDadosClimaticos.get(2));
        } catch (Exception e)
        {
            this.mensagem = "Erro ao efetuar a valição! Preencha coretamente...";
        }
    }
}
