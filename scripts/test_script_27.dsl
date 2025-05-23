load "data/cursos_online.csv";
filter column "fecha_inicio" < 2023-02-20;
aggregate AVERAGE column "calificacion_final";
aggregate COUNT column "id_estudiante";
print;