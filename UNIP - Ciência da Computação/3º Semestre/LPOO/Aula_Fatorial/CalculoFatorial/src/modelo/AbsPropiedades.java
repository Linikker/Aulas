package modelo;

public abstract class AbsPropiedades implements IMetodos
{
    //Atributos
    protected String numero;
    protected Integer num;
    
    //Metodos (Construtores)
    public AbsPropiedades(String numero)
    {
        this.numero = numero;
        this.Executar();
    }

    public AbsPropiedades(Integer num)
    {
        this.num = num;
        this.Executar();
    }



}


