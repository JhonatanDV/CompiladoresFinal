load "data/cursos_online.csv";
filter column "id_estudiante" == "EST0811" AND;
filter column "modalidad" != "Virtual" AND;
filter column "calificacion_final" != 39.5;
aggregate SUM column "porcentaje_avance";
print;