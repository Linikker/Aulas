#include <stdio.h>
#include <stdlib.h>

int main() {

    //Variaveis
    int dep;
    float SBruto, SNovo;
    char nome[50];


    //Questionario
    printf("-- Calculo de Salario Filhos --\n");

    printf("Digite o seu nome: ");
    scanf("%49s", &nome);

    printf("Digite o salario: ");
    scanf("%f", &SBruto);

    printf("Digite a quantidade de dependentes: ");
    scanf("%d", &dep);

    //Calculo
    switch (dep) {
        case 0:
            SNovo = SBruto + (SBruto * 0.05);
            break;
        case 1:
        case 2:
        case 3:
            SNovo = SBruto + (SBruto * 0.10);
            break;
        case 4:
        case 5:
        case 6:
            SNovo = SBruto + (SBruto * 0.15);
            break;
        default:
            SNovo = SBruto + (SBruto * 0.18);
            break;
    }

    //Resultado
    printf("\n\nO novo salario de %s sera de R$ %.2f.\n\n\n\n\n", nome, SNovo);

    //Final do Programa
    system("pause");
    return 0;
}
