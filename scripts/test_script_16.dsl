load "data/cursos_online.csv";
filter column "fecha_fin" < 2024-04-18 AND;
filter column "id_estudiante" == "EST0779";
aggregate COUNT column "modalidad";
aggregate AVERAGE column "calificacion_final";
print;