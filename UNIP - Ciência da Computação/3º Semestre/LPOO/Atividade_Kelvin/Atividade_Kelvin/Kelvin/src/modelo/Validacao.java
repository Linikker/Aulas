package modelo;

public class Validacao extends absPropriedades
{

    public Validacao(String temperatura)
    {
        super(temperatura);
    }

    @Override
    public void Executar()
    {
        Estaticos.MENSAGEM = "";
        try
        {
            this.valor = Double.valueOf(this.temperatura);
        }
        catch (NumberFormatException e)
        {
            Estaticos.MENSAGEM = "Digite números válidos";
        }
    }
    
}
