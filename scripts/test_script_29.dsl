load "data/cursos_online.csv";
filter column "id_estudiante" == "EST0989" AND;
filter column "plataforma" == "Udemy" OR;
filter column "plataforma" != "Platzi";
aggregate AVERAGE column "calificacion_final";
print;