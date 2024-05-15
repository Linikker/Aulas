package modelo;

public abstract class absPropriedades implements IMetodos
{
    
    public String temperatura;
    public Double valor;
    public String resposta;

    public absPropriedades(String temperatura)
    {
        this.temperatura = temperatura;
    }

    public absPropriedades(Double valor)
    {
        this.valor = valor;
    }

    @Override
    public String toString()
    {
        return resposta;
    }
    
    
    
    
}
