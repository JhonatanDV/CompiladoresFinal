load "data/cursos_online.csv";
filter column "fecha_inicio" > 2023-06-05 AND;
filter column "plataforma" != "LinkedIn Learning" OR;
filter column "curso" != "Machine Learning";
aggregate COUNT column "calificacion_final";
print;