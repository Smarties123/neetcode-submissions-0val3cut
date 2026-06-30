from typing import List, Tuple

def best_student(scores: List[Tuple[str, int]]) -> str:
    yMax = 0
    yName = ""

    for point in scores:
        x, y = point[0], point[1]
        if y > yMax:
           yMax = point[1]
           yName = point[0]

    
    return yName



# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
