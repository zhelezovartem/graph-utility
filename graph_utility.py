''' This is simple graph utility. It founds one of the possible paths from start node to end node.'''
import fileinput
import ast


# The main function. It asks user for input and founds path.
def main():
    graph = {}
    print("Please type nodes list using space as a delimeter.\nExample: 'A B C D'")
    nodes_str = input()
    print("Please type edges list using space as a delimeter.\nExample: 'AB AC CD'")
    edges_str = input()
    print("Please choose graph type.\n'0' - directed\n'1' - undirected")
    is_undirected = input()
    print("Choose path start node.\nExample: 'A'")
    start = input()
    print("Choose path end node.\nExample: 'D'")
    end = input()
    if is_undirected == "0":
        graph = make_directed_graph(nodes_string_to_list_converter(nodes_str),
                                    edges_string_to_list_converter(edges_str),
                                    graph)
    elif is_undirected == "1":
        graph = make_undirected_graph(nodes_string_to_list_converter(nodes_str),
                                      edges_string_to_list_converter(edges_str),
                                      graph)
    else:
        print("Error, wrong graph type!")

    path = find_path(graph, start, end, path=[])
    if path is None:
        print('Sorry, there are no paths from node {} to node {}'.format(start, end))
    else:
        print('One of the possible paths from node {} to node {} is: {}'.format(start, end, path))


# This function converts nodes string representation to nodes list.
def nodes_string_to_list_converter(nodes_str):
    nodes_list = list(nodes_str.split(" "))
    return nodes_list


# This function converts edges string representation to edges list.
def edges_string_to_list_converter(edges_str):
    edges_list = []
    temp_list = list(edges_str.split(" "))
    for item in temp_list:
        edge = [item[0], item[1]]
        edges_list.append(edge)
    return edges_list


# This function makes directed graph from nodes list and edges list.
def make_directed_graph(nodes_list, edges_list, graph):
    for node in nodes_list:
        node_connected_list = []
        for edge in edges_list:
            if node == edge[0]:
                node_connected_list.append(edge[1])
        if len(node_connected_list) != 0:
            graph.update({node: node_connected_list})
    return graph


# This function makes undirected graph from nodes list and edges list.
def make_undirected_graph(nodes_list, edges_list, graph):
    reverse_edges_list = []
    for edge in edges_list:
        reverse_edges_list.append(edge[::-1])
    edges_list = edges_list + reverse_edges_list
    return make_directed_graph(nodes_list, edges_list, graph)


# This function returns a path from start node to end node or returns None if there are no possible paths.
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


if __name__ == '__main__':
    main()
