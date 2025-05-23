load "data/cursos_online.csv";
filter column "fecha_inicio" <= 2023-04-02 AND;
filter column "modalidad" != "Presencial";
aggregate SUM column "calificacion_final";
print;