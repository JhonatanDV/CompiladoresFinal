load "data/cursos_online.csv";
filter column "id_estudiante" == "EST0627" OR;
filter column "fecha_inicio" == 2022-05-28;
aggregate SUM column "porcentaje_avance";
aggregate AVERAGE column "calificacion_final";
print;