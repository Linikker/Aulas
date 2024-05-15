package modelo;

public class Kelvin extends absPropriedades
{

    public Kelvin(Double valor)
    {
        super(valor);
    }

    @Override
    public void Executar()
    {
        //0 °C + 273,15 = 273,15 K
        
        this.temperatura = String.valueOf(this.valor + 273.15);
        
    }
    
}
