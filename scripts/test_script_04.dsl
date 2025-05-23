load "data/cursos_online.csv";
filter column "fecha_inicio" <= 2024-03-01 OR;
filter column "calificacion_final" > 10.8 AND;
filter column "plataforma" != "Coursera";
aggregate COUNT column "calificacion_final";
print;