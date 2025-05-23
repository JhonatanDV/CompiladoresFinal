load "data/cursos_online.csv";
filter column "estado_curso" == "Completado" OR;
filter column "fecha_fin" == 2022-07-25 OR;
filter column "plataforma" == "LinkedIn Learning";
aggregate AVERAGE column "calificacion_final";
print;