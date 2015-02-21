import struct
import sys



#filepath = ".\\Normandy Demo v100\\vehicles\\jeep\\jeep-unarmed.mdr"
#filepath = "ak-74.mdr"
filepath = "rpg-7v1-lod-5.mdr"
#filepath = "rpg-7v1.mdr"


########
# perhaps:
# object
# UVs
# face indices
# then,
# object
# vertices (in object space)
####

#
# ak-74m-lod-2.mdr
# number of floats/3 = number of vertices

with open(filepath, "rb") as f:
    num_models,name_length = struct.unpack("<IxH", f.read(7))
    #print "number of models", num_models
    #print "name length", name_length
    model_class = f.read(name_length)
    #print "model class", model_class
    f.read(1) # always 2?
    for i in range(0, 44):
        unk, = struct.unpack("f", f.read(4))
        #print unk
    print hex(f.tell())
    vertex_count, = struct.unpack("<I", f.read(4))
    print "Face count:", vertex_count/3

    for i in range(0, vertex_count/3):
        v0, v1, v2 = struct.unpack("<HHH", f.read(6))
        print "f",v0+1,v1+1,v2+1
    
    uv_in_section, = struct.unpack("<I", f.read(4))
    #print "UV in section:", uv_in_section
    #print hex(f.tell())    
    
    for i in range(0, uv_in_section/2):     
        u,v = struct.unpack("<ff", f.read(8))        
        #print "v", u,v,0
        
        
    unk, = struct.unpack("<I", f.read(4))
    print unk
    for i in range(0, unk):
        print i,struct.unpack("f", f.read(4))
    
    print "end of object", hex(f.tell())

# ak-74.mdr
# offset 0x27cf is number of floats (num/3 = vertices), followed by x,y,z
# rifle, unknown, then magazine model
