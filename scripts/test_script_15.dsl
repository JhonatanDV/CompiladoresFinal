load "data/cursos_online.csv";
filter column "modalidad" == "Híbrida";
aggregate AVERAGE column "porcentaje_avance";
aggregate AVERAGE column "calificacion_final";
print;