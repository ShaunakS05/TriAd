import aspose.threed as a3d

scene = a3d.Scene.from_file("18750.ply")
scene.save("outPutStl.stl")
