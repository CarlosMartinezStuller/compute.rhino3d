"""Hops default HTTP server example"""
import ghhops_server as ghhs
import rhino3dm


hops = ghhs.Hops()


@hops.component(
    "/add",
    name="Add",
    nickname="Add",
    description="Add numbers with CPython",
    category="Maths",
    subcategory="CPython",
    inputs=[
        ghhs.HopsNumber("A", "A", "First number"),
        ghhs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[ghhs.HopsNumber("Sum", "S", "A + B")],
)
def add(a, b):
    # testing error report
    f = 12 / 0
    return a + b


@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    category="Curve",
    subcategory="Analysis",
    icon="examples/pointat.png",
    inputs=[
        ghhs.HopsCurve("Curve", "C", "Curve to evaluate"),
        ghhs.HopsNumber("t", "t", "Parameter on Curve to evaluate"),
    ],
    outputs=[
        ghhs.HopsPoint(
            "P",
            "P",
            "Point on curve at t",
        )
    ],
)
def pointat(curve, t):
    return curve.PointAt(t)


@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    category="Surface",
    subcategory="Freeform",
    inputs=[
        ghhs.HopsPoint("Corner A", "A", "First corner"),
        ghhs.HopsPoint("Corner B", "B", "Second corner"),
        ghhs.HopsPoint("Corner C", "C", "Third corner"),
        ghhs.HopsPoint("Corner D", "D", "Fourth corner"),
    ],
    outputs=[ghhs.HopsSurface("Surface", "S", "Resulting surface")],
)
def ruled_surface(a, b, c, d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)


if __name__ == "__main__":
    hops.start(debug=True)