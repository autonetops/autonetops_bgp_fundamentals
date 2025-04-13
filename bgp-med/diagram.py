from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.generic.network import Subnet

# Define the diagram with custom Graphviz attributes
with Diagram(
    "BGP Path Manipulation with MED",
    direction="LR",
    node_attr={"margin": "0.5"},  # Adds space around nodes for better edge alignment
    graph_attr={"splines": "true", "nodesep": "1", "ranksep": "1"}  # Improves edge routing and spacing
):
    # AS 100
    with Cluster("AS 100"):
        r1 = Custom("R1\nlo0:1.1.1.1\nlo1:11.1.1.1", "cisco.png")

    # AS 200
    with Cluster("AS 200"):
        r2 = Custom("R2\nlo0:2.2.2.2\nlo1:22.2.2.2", "cisco.png")
        r3 = Custom("R3\nlo0:3.3.3.3\nlo1:33.3.3.3", "cisco.png")
        r4 = Custom("R4\nlo0:4.4.4.4\nlo1:44.4.4.4", "cisco.png")

        # Subnets connected to R3
        with Cluster("Subnets"):
            net3 = Subnet("NET3\nNET33\nOTHER NET")

    # Physical Links between AS 100 and AS 200
    r1 - Edge(label="192.168.12.0/24", color="black") - r2  # R1 to R2
    r1 - Edge(label="192.168.14.0/24", color="black") - r4  # R1 to R4
    
    # Physical Links within AS 200
    r2 - Edge(label="192.168.23.0/24", color="black") - r3  # R2 to R3
    r4 - Edge(label="192.168.34.0/24", color="black") - r3  # R4 to R3

    # Connect R3 to Subnets
    r3 - Edge(color="black") - net3