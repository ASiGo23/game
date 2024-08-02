import time
import numpy
from typing_extensions import Self

class vertex:
    def __init__(self, coords: tuple[float, float]):
        self.x, self.y = coords
        self.next = None

class adv_polygon:
    def __init__(self, vertices:list, velocity: tuple[float,float]):
        # Error management
        if len(vertices) < 3:
            raise AttributeError("Not enough vertices to make a polygon")
        
        temp = []
        for index in vertices:
            if isinstance(index, vertex):
                temp.append(index); continue
            try: temp.append(vertex(index))
            except: raise AttributeError("Unrecognized type in list vertices")
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

    def vertices_list(self) -> numpy.array:
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
    
    def reduced_normal_list(self, other: Self) -> list:
        normals = []
        
        # Removes duplicate normals
        for norm in self.normal_list() + other.normal_list():
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

        return normals

    def ticked_vertices(self, tick: float) -> numpy.array:
        temp = []
        new_x = self.start_vertex.x + tick * self.velocity[0]
        new_y = self.start_vertex.y + tick * self.velocity[1]
        temp.append(numpy.array([new_x, new_y]))
        vert = self.start_vertex.next
        while vert != self.start_vertex:
            new_x = vert.x + tick * self.velocity[0]
            new_y = vert.y + tick * self.velocity[1]

            temp.append(numpy.array([new_x, new_y]))
            vert = vert.next
        return numpy.array(temp)

    def collide_poly(self, other: Self):
        
        def dot_list(normals, vertices):
            #Returns a list of tuples that represent extremes for each normal

            extremes = []
            for normal in normals:
                #print(f"normals: {normal}")
                min = None
                max = None
                for vertex in vertices:
                    #print(f"vertex: {vertex}")
                    product = numpy.dot(normal, vertex)
                    if min == None:
                        min = product
                        max = product
                    if product < min:
                        min = product
                    if product > max:
                        max = product
                extremes.append((min,max))
                #print(f"min: {min}, max: {max}")
            return extremes

        def between(a,b,c) -> bool:
            #a is tested
            #b and c are the bounds

            if (c<=b):
                raise ArithmeticError("c is less than b")
            if (a>b and c<a) or (a<b and c>a):
                return False
            if (b<a and a<c):
                return True

        global tick

        #Generates a list of the normals from both polygons
        normals = self.reduced_normal_list(other)

        #Gets the extremes for each polygon at the start
        self_extremes = dot_list(normals, self.vertices_list())
        other_extremes = dot_list(normals, other.vertices_list())

        #Gets the extremes for each polygon at the end
        tick_self_extremes = dot_list(normals, self.ticked_vertices(tick))
        tick_other_extremes = dot_list(normals, other.ticked_vertices(tick))

        for x in range(len(normals)):
            #Checks if objects already collided
            self_1 = self_extremes[x]
            other_1= other_extremes[x]

            if  not(
                between(other_1[0], self_1[0], self_1[1])
                or
                between(other_1[1], self_1[0], self_1[1])
                or 
                between(self_1[0], other_1[0], other_1[1])
                or
                between(self_1[1], other_1[0], other_1[1])
                ): 
                break
        else: return -2, None

        #Checks if object will collide within the tick
        time = 1/tick
        x_count = 0

        for x in range(len(normals)):
            #Creates tuples of individual extremes for each normal
            #Represented as a tuple (min,max)
            self_1 = self_extremes[x]
            self_2 = tick_self_extremes[x]
            other_1= other_extremes[x]
            other_2 = tick_other_extremes[x]

            # Intersection code from https://stackoverflow.com/a/51127674
            # Adapted for use
            def findIntersection(linesegment_1, linesegment_2):
                (x1, y1), (x2, y2) = linesegment_1
                (x3, y3), (x4, y4) = linesegment_2

                top = (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)
                bottom = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
                if bottom != 0:
                    px= top/bottom
                    return px
                else: 
                    return -1

            other_segment_1 = ((0,other_1[0]),(1,other_2[0]))
            other_segment_2 = ((0,self_1[0]),(1,self_2[0]))

            local_x = 0

            for segment in (
                    (
                    (0,self_1[0]),
                    (1,self_2[0])
                    ), 
                    (
                    (0,self_1[0]),
                    (1,self_2[0])
                    )
                    ):
                inter = findIntersection(segment, other_segment_1)
                if(inter >= 0):
                    local_x += 1
                if (
                    inter > 0
                    and
                    inter < time
                ):
                    x_count += 1
                    time = inter
                    normal = normals[x]

                inter = findIntersection(segment, other_segment_2)
                if(inter >= 0):
                    local_x += 1
                if (
                    inter > 0
                    and
                    inter < time
                ):
                    x_count +=1
                    time = inter
                    normal = normals[x]
                
            if local_x == 0:
                return -1, None
        if x_count != 0:
            return time/(1/tick), normal
        else: return -1, None
                    


class adv_rect(adv_polygon):
    def __init__(self, 
                 origin_point: tuple[float,float], 
                 height: float, 
                 width: float,
                 velocity: tuple[float,float] = [0,0]
                 ):
        # Origin point is meant to be the point that is the most "negative"
        # according to the coordinates
        
        a = vertex(origin_point)
        b = vertex(((a.x), (a.y + height)))
        c = vertex(((a.x + width), (a.y + height)))
        d = vertex(((a.x + width), (a.y)))
        super().__init__([a, b, c, d], velocity)

if __name__ == "__main__":
    global tick
    tick = 1/60
    rect1 = adv_rect((10,0),1,1,(-11,0))
    rect2 = adv_rect((0,0),1,1)
    start = time.time()
    prediction, normal = rect1.collide_poly(rect2)
    end = time.time()
    print(prediction, normal)
    print(f"{end-start}")