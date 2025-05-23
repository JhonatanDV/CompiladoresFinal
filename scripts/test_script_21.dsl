load "data/cursos_online.csv";
filter column "curso" != "Data Science con R" OR;
filter column "estado_curso" != "Activo" AND;
filter column "fecha_inicio" >= 2022-01-10;
aggregate COUNT column "plataforma";
aggregate COUNT column "curso";
print;