load "data/cursos_online.csv";
filter column "id_estudiante" != "EST0952";
aggregate SUM column "porcentaje_avance";
print;