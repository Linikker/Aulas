#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Variaveis
    char tipo[50];
    float comp, larg, area;

    // Questionario
    printf("-- Calculo de Area --\n");

    printf("Digite o Comprimento: ");
    scanf("%f", &comp);

    printf("Digite a Largura: ");
    scanf("%f", &larg);

    area = comp * larg;

    // Calculo
    if (area <= 100)
    {

        sprintf(tipo, "TERRENO POPULAR");
    }
    else if (area >= 101 && area <= 500)
    {
        sprintf(tipo, "TERRENO MASTER");
    }
    else
    {
        sprintf(tipo, "TERRENO V I P");
    }

    // Resultado
    printf("O seu terreno foi avaliado como - %s\n", tipo);

    system("pause");
    return 0;
}
