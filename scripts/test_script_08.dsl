load "data/cursos_online.csv";
filter column "fecha_fin" > 2023-05-22 OR;
filter column "fecha_fin" < 2024-02-23;
aggregate AVERAGE column "porcentaje_avance";
aggregate COUNT column "id_estudiante";
print;