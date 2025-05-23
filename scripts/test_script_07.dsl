load "data/cursos_online.csv";
filter column "fecha_fin" < 2024-08-26 OR;
filter column "fecha_inicio" < 2024-12-15;
aggregate AVERAGE column "porcentaje_avance";
aggregate COUNT column "curso";
print;