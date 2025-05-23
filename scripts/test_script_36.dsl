load "data/cursos_online.csv";
filter column "plataforma" != "LinkedIn Learning" AND;
filter column "id_estudiante" != "EST0780";
aggregate COUNT column "estado_curso";
aggregate COUNT column "calificacion_final";
print;