# 785A - Anton and Polyhedrons

n = int(input().strip())
polyhedrons_number_of_faces = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20
}
list_of_number_of_faces = []

for _ in range(n):
    list_of_number_of_faces.append(polyhedrons_number_of_faces[input().strip()])

print(sum(list_of_number_of_faces))