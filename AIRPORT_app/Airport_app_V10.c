#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

// Constantes
#define NUM_PISTAS 5
#define TIEMPO_DESPEGUE 15
#define TIEMPO_ATERRIZAJE 10
#define TIEMPO_LLEGADA_PISTA 5
#define TIEMPO_ENTRE_VIP 30

// Semaforos
sem_t pistas[NUM_PISTAS];
sem_t mutex;
sem_t aviones_normales;
sem_t aviones_vip;

// Variables globales
int aviones_en_espera[2] = {0, 0}; // 0: normal, 1: vip
char *ultimo_avion = NULL;
time_t ultimo_vip = 0; // Tiempo en el que el último avión VIP despegó o aterrizó


typedef struct
{
    int id;
    char *tipo;
    char *estado;
    char *operacion;
} Avion;

void *run(void *arg)
{
    Avion *avion = (Avion *)arg;
    printf("Avión [%d] %s está en %s, esperando para %s.\n", avion->id, avion->tipo, avion->estado, avion->operacion);
    sem_wait(&mutex);
    aviones_en_espera[avion->tipo == "NORMAL" ? 0 : 1] += 1;
    int pista_asignada = rand() % NUM_PISTAS; // Asignación aleatoria de pista
    if (avion->tipo == "NORMAL" || (avion->tipo == "VIP" && ultimo_avion != "VIP"))
    {
        printf("Pista %d preparada.\n", pista_asignada);
        sem_wait(&pistas[pista_asignada]);
        printf("Pista %d asignada a Avión [%d] %s.\n", pista_asignada, avion->id, avion->tipo);
        if (avion->tipo == "VIP")
        {
            time_t ahora = time(NULL);
            if (ultimo_avion == "VIP" && ahora - ultimo_vip < TIEMPO_ENTRE_VIP)
            {
                sleep(TIEMPO_ENTRE_VIP - (ahora - ultimo_vip));
            }
            ultimo_vip = time(NULL);
        }
    }
    sem_post(&mutex);
    sem_post(avion->tipo == "NORMAL" ? &aviones_normales : &aviones_vip);
    printf("Avión [%d] %s dirigiéndose a pista de %s.\n", avion->id, avion->tipo, avion->operacion);
    sleep(TIEMPO_LLEGADA_PISTA);
    printf("Avión [%d] %s %s en Pista %d.\n", avion->id, avion->tipo, avion->operacion, pista_asignada);
    sleep(avion->operacion == "aterrizar" ? TIEMPO_ATERRIZAJE : TIEMPO_DESPEGUE);
    if (avion->operacion == "aterrizar")
    {
        printf("Avión [%d] %s dirigiéndose a puerta de embarque.\n", avion->id, avion->tipo);
    }
    printf("Avión [%d] %s, hasta luego.\n", avion->id, avion->tipo);
    ultimo_avion = avion->tipo;
    sem_post(&pistas[pista_asignada]);
    free(avion);
    return NULL;
}

int main()
{
    for (int i = 0; i < NUM_PISTAS; i++)
    {
        sem_init(&pistas[i], 0, 1);
    }
    sem_init(&mutex, 0, 1);
    sem_init(&aviones_normales, 0, 0);
    sem_init(&aviones_vip, 0, 0);

    int id = 0;
    while (1)
    {
        char *tipo = rand() % 2 == 0 ? "NORMAL" : "VIP";
        char *estado = rand() % 2 == 0 ? "aire" : "tierra";
        char *operacion = estado == "aire" ? "aterrizar" : "despegar";
        Avion *avion = malloc(sizeof(Avion));
        avion->id = id;
        avion->tipo = tipo;
        avion->estado = estado;
        avion->operacion = operacion;
        pthread_t thread;
        pthread_create(&thread, NULL, run, avion);
        id += 1;
        sleep(6); // Tiempo entre la creación de cada avión
    }

    return 0;
}
