load "data/cursos_online.csv";
filter column "plataforma" != "edX";
aggregate COUNT column "fecha_inicio";
print;