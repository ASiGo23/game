import time
import numpy
from typing import Self

class vertex:
    def __init__(self, coords: tuple[float, float]):
        self.x, self.y = coords
        self.next = None

class adv_polygon:
    def __init__(self, vertices:list, velocity: tuple[float,float]):
        # Error management
        if len(vertices) == [0,1,2]:
            raise AttributeError("Not enough vertices to make a polygon")
        
        temp = []
        for index in vertices:
            if isinstance(index, vertex):
                temp.append(index); continue
            try: temp.append(vertex(index))
            except: raise AttributeError("Unrecognized Type in list vertices")
        vertices = temp

        index = 0
        self.start_vertex = vertices[index]

        vertices[index].next = vertices[index + 1]

        index += 1
        while index < len(vertices)-1:
            vertices[index].next = vertices[index + 1]
            index += 1
        vertices[index].next = vertices[0]

        self.velocity = list(velocity)

    def vertex_list(self) -> numpy.array:
        temp = []
        temp.append(numpy.array([self.start_vertex.x, self.start_vertex.y]))
        vert = self.start_vertex.next
        while vert != self.start_vertex:
            temp.append(numpy.array([vert.x, vert.y]))
            vert = vert.next
        return numpy.array(temp)

    def normal_list(self) -> numpy.array:
        current_vertex = self.start_vertex
        norms = []

        def get_normal(vertex1, vertex2):
            # This function finds the inverse of the slope
            # Represented with a numpy vector
            change_in_x = vertex2.x - vertex1.x
            change_in_y = vertex2.y - vertex1.y

            return numpy.array([change_in_y, change_in_x])

        norms.append(get_normal(current_vertex, current_vertex.next))
        current_vertex = current_vertex.next
        while current_vertex != self.start_vertex:
            norms.append(get_normal(current_vertex, current_vertex.next))
            current_vertex = current_vertex.next

        return norms
    
    def collide_poly(self, polygon: Self):
        self_vertices = self.vertex_list()
        other_vertices = polygon.vertex_list()
        normals = []
        
        def dot_list(normals, vertices):
            for normal in normals:
                print(f"normals: {normal}")
                min = None
                max = None
                for vertex in vertices:
                    print(f"vertex: {vertex}")
                    product = numpy.dot(normal, vertex)
                    if min == None:
                        min = product
                        max = product
                    if product < min:
                        min = product
                    if product > max:
                        max = product
                print(f"min: {min}, max: {max}")

        for norm in self.normal_list() + polygon.normal_list():
            if norm[0] < 0: 
                norm = numpy.multiply(norm, -1)
            if norm[0] == 0 and norm[1] < 0:
                norm = numpy.multiply(norm, -1)
            flag = False
            for normal in normals:
                if (normal[0] == norm[0]) and (normal[1] == norm[1]):
                    flag = True
                    break
            if flag == False: normals.append(norm)

        dot_list(normals, self_vertices)
        dot_list(normals, other_vertices)



class adv_rect(adv_polygon):
    def __init__(self, 
                 origin_point: tuple[float,float], 
                 height: float, 
                 width: float,
                 velocity: tuple[float,float] = [0,0]
                 ):
        # Origin point is meant to be the point that is the most "negative"
        # Left ambiguous as different people have different interpretations as
        # to which direction is positive. 
        
        a = vertex(origin_point)
        b = vertex(((a.x), (a.y + height)))
        c = vertex(((a.x + width), (a.y + height)))
        d = vertex(((a.x + width), (a.y)))
        super().__init__([a, b, c, d], velocity)


start = time.time()
rect1 = adv_rect((0,0),1,1)
rect2 = adv_rect((0,0),1,1)
rect1.collide_poly(rect2)
end = time.time()
print(f"{end-start}")
#best:0.0003 seconds without printing