import cmath
import math
from math import sqrt, atan

import numpy as np


def convertToPolar(complexNumber):
    module, angleRad = cmath.polar(complexNumber)
    angle = math.degrees(angleRad)
    PolarNumber = {"Intensidad": module, "Angulo": angle}
    return PolarNumber


def ObtainIntensitiesPolar(Intensities):
    IntensitiesPolar = []
    for Intensity in Intensities:
        IntensityPolar = convertToPolar(Intensity)
        IntensitiesPolar.append(IntensityPolar)
    return IntensitiesPolar


def ObtainComplexIntensities(Determinants):
    Intensity_1 = Determinants[1] / Determinants[0]
    Intensity_2 = Determinants[2] / Determinants[0]
    Intensity_B = Intensity_2 - Intensity_1
    Intensity_C = (-1) * Intensity_2
    Intensity_N = Intensity_1 + Intensity_B + Intensity_C
    Intensities = [Intensity_1, Intensity_2, Intensity_B, Intensity_C, Intensity_N]
    return Intensities


def ObtainDeterminantes(Matrices):
    DeterminantePrincipal = np.linalg.det(Matrices[0])
    DeterminanteIntensidad_1 = np.linalg.det(Matrices[1])
    DeterminanteIntensidad_2 = np.linalg.det(Matrices[2])
    Determinants = [DeterminantePrincipal, DeterminanteIntensidad_1, DeterminanteIntensidad_2]
    return Determinants


def ObtainMatrices(arrayValues):
    Principal_Matriz = np.array([[complex(arrayValues[0]), complex(arrayValues[1])],
                                 [complex(arrayValues[3]), complex(arrayValues[4])]])
    Matriz_Intensiad_1 = np.array([[complex(arrayValues[2]), complex(arrayValues[1])],
                                   [complex(arrayValues[5]), complex(arrayValues[4])]])
    Matriz_Intensiad_2 = np.array([[complex(arrayValues[0]), complex(arrayValues[2])],
                                   [complex(arrayValues[3]), complex(arrayValues[5])]])
    Matrices = [Principal_Matriz, Matriz_Intensiad_1, Matriz_Intensiad_2]
    return Matrices


def CalcularMatriz(arrayValues):
    Matrices = ObtainMatrices(arrayValues)
    Determinants = ObtainDeterminantes(Matrices)
    Intensities = ObtainComplexIntensities(Determinants)
    IntensitiesPolar = ObtainIntensitiesPolar(Intensities)
    return IntensitiesPolar,Intensities
