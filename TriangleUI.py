import TriangleUtils

a = ""
while a != "exit":
    a = input("Tell me the length of the first side. Type 'exit' to quit. ")
    if a == "exit":
        print("Keep your triangles")
        break
    try:
        a = int(a)
        b = int(input("Tell me the length of the second side: "))
        c = int(input("Tell me the length of the third side: "))
    except ValueError:
        print("Only integers are accepted")
        continue
    print(TriangleUtils.triangleInspector(a,b,c))

    # JANNE VILJANEN TKM24