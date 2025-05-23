load "data/cursos_online.csv";
filter column "fecha_inicio" < 2023-06-27;
aggregate COUNT column "fecha_fin";
aggregate SUM column "calificacion_final";
print;