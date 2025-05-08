## Introducción

Satellogic es una empresa argentina de satélites, orgullo nacional. Sus satélites tiene nombres muy patriótricos, como "dulce y batata" (2 satélites). Mi favorito es **MilaneSAT** que le da el nombre a esta consigna.

Esta vuelta, no vamos a lanzar un satélite sino una constelación de ellos. Estamos encargados de verificar que la distancia mínima (ángulo) entre ellos se respete.

## Descripción del programa

La función `validate_orbit_positions` recibe dos parámetros:

```python
def validate_orbit_positions(positions, min_distance):
```

### Parámetros

- `positions`: una lista de números (floats o enteros) entre 0 y 360 (no inclusivo), que representan posiciones angulares en la órbita (en grados).
- `min_distance`: un número positivo que representa la distancia mínima permitida entre dos satélites.

### Salida

La función retorna una tupla con dos elementos:

1. Un valor booleano (`True` o `False`) que indica si todas las posiciones cumplen con la distancia mínima.
2. Una lista de pares de posiciones que están demasiado cerca entre sí, en caso de que existan violaciones. Si no hay violaciones, la lista está vacía.

### Ejemplo

```python
validate_orbit_positions([0, 90, 180, 270], 80)
# Retorna: (True, [])

validate_orbit_positions([10, 25, 355], 20)
# Retorna: (False, [(10, 25), (355, 10)])
```

**Nota**: La función considera que la órbita es circular, por lo tanto también compara el último valor con el primero (por ejemplo, entre 350° y 10° hay una diferencia de 20°).

Si siguen sin entender como funciona el programa, pueden hacer pruebas modificando el final de la sección marcada con un comentario en `main.py`

## Consigna Base

En el archivo `test_basico.py`, escriban un conjunto de tests unitarios usando pytest que verifiquen el comportamiento de la función en los siguientes casos:

1. Cuando todas las posiciones están correctamente espaciadas.
2. Cuando hay al menos un par de satélites demasiado cerca.
3. Cuando los satélites están exactamente a la distancia mínima.
4. Cuando hay una sola posición.
5. Cuando no hay posiciones.
6. Cuando hay múltiples violaciones.
7. Cuando las posiciones están desordenadas.
8. Cuando hay dos satélites en la misma posición.
9. Cuando la violación de distancia se da en un par de satélites que están cerca al dar la vuelta.

**IMPORTANTE**: Recuerden chequear tanto el valor booleano como la lista.

## Extra

En el archivo `test_extra.py`, escriban tests que consideren entradas no válidas, como por ejemplo:

1. Posiciones negativas o mayores o iguales a 360.
2. Posiciones que no son números (como strings).
3. Un valor de min_distance igual a 0, negativo, mayor a 360 o no numérico.

El programa, al encontrarse con cualquiera de esos casos, dispara una excepción del tipo `ValueError`. Googleen como hacer en pytest para chequear que la excepción sea la correcta.
