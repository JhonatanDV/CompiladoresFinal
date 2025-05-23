load "data/cursos_online.csv";
filter column "fecha_fin" <= 2024-07-06 AND;
filter column "fecha_inicio" == 2022-06-06 OR;
filter column "modalidad" == "Virtual";
aggregate COUNT column "calificacion_final";
print;