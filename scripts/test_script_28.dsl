load "data/cursos_online.csv";
filter column "curso" == "Data Science con R";
aggregate COUNT column "plataforma";
print;