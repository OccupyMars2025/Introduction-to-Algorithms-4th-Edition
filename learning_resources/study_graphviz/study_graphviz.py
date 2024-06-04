"""

https://graphviz.readthedocs.io/en/stable/
"""



# from graphviz import Digraph

# dot = Digraph(comment='The Round Table')

# dot.node('A', 'King Arthur')
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')

# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')

# dot.render('round-table.gv', view=True)



from graphviz import Digraph

dot = Digraph()

dot.attr(size='10,10')

dot.node('A', 'Root', shape='ellipse')
dot.node('B', 'Left Child', shape='ellipse')
dot.node('C', 'Right Child', shape='ellipse')

dot.edge('A', 'B', label='Left', color='blue')
dot.edge('A', 'C', label='Right', color='red')

dot.render('example-bst.gv', view=True)
