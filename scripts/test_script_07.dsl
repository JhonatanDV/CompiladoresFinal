load "data/cursos_online.csv";
filter column "fecha_fin" == 2023-10-26 AND;
filter column "curso" == "Data Science con R";
aggregate COUNT column "id_estudiante";
aggregate COUNT column "calificacion_final";
print;