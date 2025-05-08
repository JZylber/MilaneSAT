def validate_orbit_positions(positions, min_distance):
    """
    Validates satellite spacing and identifies violations.

    Parameters:
    - positions: list of floats or ints in [0, 360)
    - min_distance: float > 0 and < 360

    Returns:
    - (is_valid: bool, violations: list of (a, b) pairs too close)

    Raises:
    - ValueError if positions contain invalid values or min_distance is invalid
    """
    if not isinstance(min_distance, (int, float)) or min_distance <= 0 or min_distance >= 360:
        raise ValueError("La distancia mínima debe ser un número entre 0 y 360")

    for pos in positions:
        if not isinstance(pos, (int, float)) or not (0 <= pos < 360):
            raise ValueError(f"Ángulo de satélite inválido: {pos} (tiene que ser entre 0 y 360 grados)")

    if len(positions) < 2:
        return True, []

    sorted_positions = sorted(positions)
    violations = []

    for i in range(len(sorted_positions)):
        a = sorted_positions[i]
        b = sorted_positions[(i + 1) % len(sorted_positions)]  # circular wrap
        diff = (b - a) % 360
        if diff < min_distance:
            violations.append((a, b))

    return len(violations) == 0, violations

if __name__ == '__main__':
    # Modifiquen acá para hacer prueba
    positions = [10, 25, 355]
    min_distance = 20
    is_valid, violations = validate_orbit_positions(positions, min_distance)
    print(f"Se ejecutó la función con {positions} y distancia mínima {min_distance}\n")
    if not is_valid:
        print("Violaciones encontradas:")
        print(f"Violaciones encontradas: {violations}")
    else:
        print("No se encontraron violaciones.")
