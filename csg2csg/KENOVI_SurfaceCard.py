from csg2csg.SurfaceCard import SurfaceCard




# generic write method
def write_mcnp_surface(filestream, SurfaceCard):
    
    string = boundary_condition(SurfaceCard.boundary_condition)

    string += str(SurfaceCard.surface_id) + " "
    
    if SurfaceCard.surface_type == SurfaceCard.SurfaceType["PLANE_GENERAL"]:
        string += mcnp_plane_string(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["PLANE_X"]:
        string += mcnp_plane_x(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["PLANE_Y"]:
        string += mcnp_plane_y(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["PLANE_Z"]:
        string += mcnp_plane_z(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["CYLINDER_X"]:
        string += mcnp_cylinder_x(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["CYLINDER_Y"]:
        string += mcnp_cylinder_y(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["CYLINDER_Z"]:
        string += mcnp_cylinder_z(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["CONE_X"]:
        string += mcnp_cone_x(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["CONE_Y"]:
        string += mcnp_cone_y(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["CONE_Z"]:
        string += mcnp_cone_z(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["SPHERE_GENERAL"]:
        string += mcnp_sphere(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["GENERAL_QUADRATIC"]:
        string += mcnp_gq(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["TORUS_X"]:
        string += mcnp_tx(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["TORUS_Y"]:
        string += mcnp_ty(SurfaceCard)
    elif SurfaceCard.surface_type == SurfaceCard.SurfaceType["TORUS_Z"]:
        string += mcnp_tz(SurfaceCard)
    else:
        string += "Unknown surface type"
        
    filestream.write(mcnp_line_formatter(string))
    
    return
    
    
    
    
class KENOVI_SurfaceCard(SurfaceCard):
    
    
        # constructor
    def __init__(self,card_string, verbose = False):
        SurfaceCard.__init__(self,card_string)
        #self.classify()
    
