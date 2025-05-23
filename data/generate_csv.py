import pandas as pd
import random
from datetime import datetime, timedelta
from faker import Faker

def generate_courses_csv(filename='cursos_online.csv', num_records=300):
    """Generate synthetic data for online courses tracking"""
    
    fake = Faker('es_ES')  # Spanish locale for more realistic names
    
    # Define possible values for categorical fields
    cursos = [
        'Python Básico', 'JavaScript Avanzado', 'Data Science con R',
        'Machine Learning', 'Desarrollo Web Full Stack', 'Bases de Datos SQL',
        'Análisis de Datos', 'Inteligencia Artificial', 'Ciberseguridad',
        'Cloud Computing AWS', 'DevOps y CI/CD', 'Mobile App Development',
        'UI/UX Design', 'Marketing Digital', 'Project Management',
        'Excel Avanzado', 'Power BI', 'Tableau', 'Docker y Kubernetes',
        'React Native', 'Vue.js', 'Angular', 'Node.js', 'Django',
        'Blockchain', 'Big Data', 'IoT', 'Robótica', 'AutoCAD'
    ]
    
    estados = ['Activo', 'Completado', 'Pausado', 'Cancelado', 'En Progreso']
    modalidades = ['Virtual', 'Presencial', 'Híbrida', 'Autodirigida']
    plataformas = ['Coursera', 'Udemy', 'edX', 'Platzi', 'Khan Academy', 
                   'LinkedIn Learning', 'Skillshare', 'MasterClass', 
                   'Codecademy', 'FreeCodeCamp']
    
    data = []
    
    for i in range(num_records):
        # Generate dates
        fecha_inicio = fake.date_between(start_date='-2y', end_date='today')
        
        # Calculate end date based on course duration (30-365 days)
        duracion_dias = random.randint(30, 365)
        fecha_fin = fecha_inicio + timedelta(days=duracion_dias)
        
        # Generate progress percentage based on status
        estado = random.choice(estados)
        if estado == 'Completado':
            porcentaje_avance = 100
            calificacion_final = round(random.uniform(60, 100), 1)
        elif estado == 'Cancelado':
            porcentaje_avance = random.randint(0, 30)
            calificacion_final = 0
        elif estado == 'Pausado':
            porcentaje_avance = random.randint(10, 80)
            calificacion_final = 0
        else:  # Activo or En Progreso
            porcentaje_avance = random.randint(1, 95)
            if porcentaje_avance > 80:
                calificacion_final = round(random.uniform(50, 95), 1)
            else:
                calificacion_final = 0
        
        record = {
            'id_inscripcion': f'INS{i+1:04d}',
            'id_estudiante': f'EST{random.randint(1, 1000):04d}',
            'curso': random.choice(cursos),
            'porcentaje_avance': porcentaje_avance,
            'calificacion_final': calificacion_final,
            'fecha_inicio': fecha_inicio.strftime('%Y-%m-%d'),
            'fecha_fin': fecha_fin.strftime('%Y-%m-%d'),
            'estado_curso': estado,
            'modalidad': random.choice(modalidades),
            'plataforma': random.choice(plataformas)
        }
        
        data.append(record)
    
    # Create DataFrame and save to CSV
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    
    print(f"Generated {num_records} records in {filename}")
    print(f"Columns: {list(df.columns)}")
    print(f"Sample data:")
    print(df.head())
    
    # Print some statistics
    print(f"\nData Statistics:")
    print(f"Unique students: {df['id_estudiante'].nunique()}")
    print(f"Unique courses: {df['curso'].nunique()}")
    print(f"Course status distribution:")
    print(df['estado_curso'].value_counts())
    print(f"Platform distribution:")
    print(df['plataforma'].value_counts())
    
    return df

if __name__ == "__main__":
    # Generate the CSV file
    generate_courses_csv('data/cursos_online.csv', 300)
