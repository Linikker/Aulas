package modelo;

public class Controle extends AbsPropiedades
{

    public Controle(String numero)
    {
        super(numero);
    }
    
    @Override
    public void Executar()
    {
        Estatico.MENSAGEM = "";
        Validacao validacao = new Validacao(this.numero);
        if (Estatico.MENSAGEM.equals(""))
        {
            Calculo calculo = new Calculo(validacao.num);
            this.numero = calculo.toString();
        }
    }

    @Override
    public String toString()
    {
        return this.numero;
    }
    
        
}
