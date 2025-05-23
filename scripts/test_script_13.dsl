load "data/cursos_online.csv";
filter column "id_estudiante" == "EST0385";
aggregate SUM column "porcentaje_avance";
aggregate AVERAGE column "calificacion_final";
print;