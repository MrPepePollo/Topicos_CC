
import pandas as pd
import numpy as np

distritos = {
    "San Borja": {
        "lat_range": (-12.087, -12.116),
        "lon_range": (-77.003, -76.983)
    },
    "Surco": {
        "lat_range": (-12.091, -12.192),
        "lon_range": (-76.983, -76.953)
    },
    "Surquillo": {
        "lat_range": (-12.107, -12.138),
        "lon_range": (-77.018, -76.983)
    },
    "Lince": {
        "lat_range": (-12.071, -12.101),
        "lon_range": (-77.035, -77.003)
    },
    "Ate": {
        "lat_range": (-12.026, -12.135),
        "lon_range": (-76.868, -76.922)
    },
    "Cercado de Lima": {
        "lat_range": (-12.038, -12.087),
        "lon_range": (-77.050, -77.003)
    },
    "Miraflores": {
        "lat_range": (-12.070, -12.115),
        "lon_range": (-77.01, -77.045)
    },
    "La Molina": {
        "lat_range": (-12.061, -12.158),
        "lon_range": (-76.899, -76.882)
    },
    "San Isidro": {
        "lat_range": (-12.087, -12.121),
        "lon_range": (-77.03, -77.043)
    }
}


# Número de pacientes a generar
num_patients = 1200

# Generamos datos para los pacientes
patients_data = []
district_names = list(distritos.keys())

for patient_id in range(1, num_patients + 1):
    # Elegir un distrito aleatorio
    chosen_district = np.random.choice(district_names)

    # Generar coordenadas aleatorias dentro del rango del distrito
    lat = np.random.uniform(distritos[chosen_district]["lat_range"][0], distritos[chosen_district]["lat_range"][1])
    lon = np.random.uniform(distritos[chosen_district]["lon_range"][0], distritos[chosen_district]["lon_range"][1])

    # Gravedad aleatoria entre 1 y 5
    severity = np.random.randint(1, 6)  # 1 a 5


    # Crear diccionario con la información del paciente
    patient_info = {
        "id": patient_id,
        "latitude": lat,
        "longitude": lon,
        "severity": severity
    }

    patients_data.append(patient_info)

# Crear un DataFrame y guardarlo en un CSV
patients_df = pd.DataFrame(patients_data)

# Guardar en un archivo CSV sin índice
patients_df.to_csv("Patients.csv", index=False)
