load "data/cursos_online.csv";
filter column "id_estudiante" == "EST0459" AND;
filter column "curso" == "Desarrollo Web Full Stack";
aggregate AVERAGE column "calificacion_final";
aggregate SUM column "porcentaje_avance";
print;