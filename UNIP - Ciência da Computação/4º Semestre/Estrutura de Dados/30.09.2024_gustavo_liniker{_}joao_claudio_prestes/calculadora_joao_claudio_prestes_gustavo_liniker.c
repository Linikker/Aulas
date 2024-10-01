#include <stdio.h>
#include <stdlib.h>

void op(float x, const char* sinal, float y, float res)
{
    printf("\n\nO resultado de %.2f %s %.2f = %.2f.\n\n", x, sinal, y, res);
}

void menu(int *opcao, float *x, float *y)
{
    printf("1 - Somar\n");
    printf("2 - Subtrair\n");
    printf("3 - Multiplicar\n");
    printf("4 - Dividir\n");
    printf("5 - Sair\n");

    printf("\nDigite o numero da opcao desejada: ");
    scanf("%d", opcao);

    if (*opcao != 5) {
        printf("\nDigite o primeiro numero: ");
        scanf("%f", x);

        printf("\nDigite o segundo numero: ");
        scanf("%f", y);
    }
}

int main()
{
    int opcao;
    const char* sinal;
    float x, y, resultado;

    printf("-- Calculadora --\n");

    do {
        menu(&opcao, &x, &y);

        // Calculo
        switch (opcao)
        {
            case 1:
                sinal = "+";
                resultado = x + y;
                op(x, sinal, y, resultado);
                break;
            case 2:
                sinal = "-";
                resultado = x - y;
                op(x, sinal, y, resultado);
                break;
            case 3:
                sinal = "*";
                resultado = x * y;
                op(x, sinal, y, resultado);
                break;
            case 4:
                if (y != 0) {
                    sinal = "/";
                    resultado = x / y;
                    op(x, sinal, y, resultado);
                } else {
                    printf("Erro: Divisao por zero.\n\n");
                }
                break;
            case 5:
                printf("Obrigado!\n\n");
                break;
            default:
                printf("Opcao invalida! Tente novamente.\n");
                break;
        }
    } while (opcao != 5);

    // Final do Programa
    system("pause");
    return 0;
}
