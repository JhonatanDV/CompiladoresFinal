load "data/cursos_online.csv";
filter column "plataforma" == "Udemy";
aggregate COUNT column "curso";
print;