load "data/cursos_online.csv";
filter column "id_estudiante" == "EST0770";
aggregate AVERAGE column "porcentaje_avance";
aggregate SUM column "calificacion_final";
print;