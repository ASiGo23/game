import numpy

class vertex:
    def __init__(self, coords: tuple[float, float]):
        self.x, self.y = coords
        self.next = None

class adv_polygon:
    def __init__(self, vertices:list):
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
    
class adv_rect(adv_polygon):
    def __init__(self, origin_point: tuple[float,float], height: float, width: float):
        # Origin point is meant to be the point closest to the origin
        # Left ambiguous as different people have different interpretations as
        # to which direction is positive. 
        
        a = vertex(origin_point)
        b = vertex((a.x), (a.y + height))
        c = vertex((a.x + width), (a.y + height))
        d = vertex((a.x + width), (a.y))
        super().__init__([a, b, c, d])