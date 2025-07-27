#Desarrolla una función que reciba una tupla de estudiantes (nombre, edad, promedio)
#  y use un ciclo for para encontrar y devolver una nueva tupla solo con los estudiantes que tienen promedio mayor a 8.0.


def students_filter(tuplas):
    choosed = []

    for  students in tuplas:
        name,age,score = students
        if score > 8.0:
            choosed.append(students)
    return tuple(choosed)

estudiantes = (
    ("Ana", 20, 9.2),
    ("Luis", 22, 7.5),
    ("Carla", 19, 8.7),
    ("Pedro", 21, 6.8),
    ("María", 23, 8.1),
    ("Juan", 20, 7.9),
    ("Sofía", 18, 9.5),
    ("Diego", 22, 5.4),
    ("Lucía", 21, 8.3),
    ("Andrés", 20, 7.1),
    ("Valentina", 19, 8.6),
    ("Ricardo", 24, 6.7),
    ("Laura", 22, 9.0),
    ("Mateo", 20, 7.3),
    ("Camila", 21, 8.9),
    ("Julián", 19, 5.9),
    ("Isabella", 23, 9.1),
    ("Sebastián", 20, 6.5),
    ("Gabriela", 18, 8.0),
    ("Tomás", 22, 7.8),
    ("Daniela", 21, 8.4),
    ("Felipe", 20, 6.9),
    ("Paula", 19, 9.3),
    ("Miguel", 23, 7.0),
    ("Nicole", 22, 8.8),
    ("Samuel", 21, 6.3),
    ("Antonella", 18, 9.6),
    ("Brayan", 24, 7.6),
    ("Emilia", 20, 8.2),
    ("Ángel", 21, 5.5),
)

answer = students_filter(estudiantes)
print(answer)