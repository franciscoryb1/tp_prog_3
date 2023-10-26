"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo, y los empates se resuelvan de forma aleatoria.
Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from problem import OptProblem, TSP
from random import choice
from time import time


class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        while True:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val ==
                        max(diff.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Retornar si estamos en un optimo local 
            # (diferencia de valor objetivo no positiva)
            if diff[act] <= 0:

                self.tour = actual
                self.value = value
                end = time()
                self.time = end-start
                return

            # Sino, nos movemos al sucesor
            else:

                actual = problem.result(actual, act)
                value = value + diff[act]
                self.niters += 1


class HillClimbingReset(LocalSearch):
    """Algoritmo de ascension de colinas con reinicio aleatorio."""

    def solve(self, problem: TSP):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        limit = 10
        count = 0
            
        while True:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val ==
                        max(diff.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Retornar si estamos en un optimo local 
            # (diferencia de valor objetivo no positiva)
            if diff[act] <= 0:

                if count == limit:
                    self.tour = actual
                    self.value = value
                    end = time()
                    self.time = end-start
                    return

                else:
                    actual = problem.random_reset()
                    value = problem.obj_val(actual)
                    count += 1
                    
            # Sino, nos movemos al sucesor
            else:

                actual = problem.result(actual, act)
                value = problem.obj_val(actual)
                self.niters += 1


class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""

    def solve(self, problem: OptProblem):
        actual = problem.init
        mejor = actual
        value_mejor = problem.obj_val(mejor)
        tabu = []
        start = time()
        
        while self.niters <= 1000:
            sucesores = problem.val_diff(actual)
            # no_tabues = [s for s in sucesor if s not in tabu]
            no_tabues = {}
            for k, v in sucesores:
                if k not in tabu:
                    no_tabues[k] = v
            sucesor = [act for act, val in no_tabues.items() if val == max(sucesores.values())]
            
            act = choice(sucesor)
            
            actual = problem.result(actual, act)
            value = problem.obj_val(actual)
                
            if value_mejor < value:
                mejor = actual
                value_mejor = problem.obj_val(mejor)
                
                if len(tabu) == 20:
                    tabu.pop(0) 
                    tabu.append(act)
                else:
                    tabu.append(act)
            self.niters += 1
            
        self.tour = mejor
        self.value = value_mejor
        end = time()
        self.time = end-start
        return mejor


# class Tabu(LocalSearch):
#     """Algoritmo de busqueda tabu."""