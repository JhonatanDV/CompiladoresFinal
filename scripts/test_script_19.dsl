load "data/cursos_online.csv";
filter column "modalidad" == "Presencial";
aggregate AVERAGE column "calificacion_final";
print;