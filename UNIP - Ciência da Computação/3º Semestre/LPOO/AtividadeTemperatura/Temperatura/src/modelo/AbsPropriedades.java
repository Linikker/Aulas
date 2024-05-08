package modelo;

public class AbsPropriedades
{
    Double temp;
    String temperatura;
    String tipo;

    public AbsPropriedades(Double temp, String tipo)
    {
        this.temp = temp;
        this.tipo = tipo;
    }

    public AbsPropriedades(String temperatura, String tipo)
    {
        this.temperatura = temperatura;
        this.tipo = tipo;
    }
    
    
    
}
