def convertir_coordenadas(latitud, longitud):
    # Coordenadas de latitud
    grados_lat = int(latitud[0:2])
    minutos_lat = int(latitud[3:5])
    segundos_lat = float(latitud[6:])

    # Coordenadas de longitud
    grados_lon = int(longitud[0:3])
    minutos_lon = int(longitud[4:6])
    segundos_lon = float(longitud[7:])

    # Cálculo de la latitud decimal
    lat_decimal = grados_lat + (minutos_lat / 60) + (segundos_lat / 3600)

    # Cálculo de la longitud decimal
    lon_decimal = grados_lon + (minutos_lon / 60) + (segundos_lon / 3600)

    return lat_decimal, lon_decimal


# Ejemplo de uso
latitud = "43 deg 15' 56.48\" N"
longitud = "2 deg 55' 59.23\" W"

lat_decimal, lon_decimal = convertir_coordenadas(latitud, longitud)
print("Latitud decimal:", lat_decimal)
print("Longitud decimal:", lon_decimal)
