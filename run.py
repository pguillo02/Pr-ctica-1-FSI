import search

problems = {
    "Arad - Bucharest": search.GPSProblem('A', 'B', search.romania),
    "Oradea - Eforie": search.GPSProblem("O", "E", search.romania),
    "Giurgiu - Zerind": search.GPSProblem("G", "Z", search.romania),
    "Neamt - Dobreta": search.GPSProblem("N", "D", search.romania),
    "Mehadia - Fagaras": search.GPSProblem("M", "F", search.romania)
}

def execute_search(problem_name, problem):
    methods = {
        "Anchura": search.breadth_first_graph_search,
        "Profundidad": search.depth_first_graph_search,
        "Ramificación y Acotación": search.bab,
        "Ramificación y Acotación con Subestimación": search.babsub
    }

    print(problem_name)
    for method_name, method in methods.items():
        print(f"\n{method_name}")
        search_result = method(problem)
        ruta = search_result.path()

        print(f"Ruta: {ruta}")

for name, problem in problems.items():
    execute_search(name, problem)
