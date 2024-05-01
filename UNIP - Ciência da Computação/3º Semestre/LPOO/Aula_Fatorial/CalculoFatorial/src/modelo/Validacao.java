package modelo;

public class Validacao extends AbsPropiedades
{

    public Validacao(String numero)
    {
        super(numero);
    }

    @Override
    public void Executar()
    {
        Estatico.MENSAGEM = "";
        try
        {
            this.num = Integer.valueOf(this.numero);
        } catch (Exception e)
        {
            Estatico.MENSAGEM = "Digite um numero valido!";
        }
    }
    
}
