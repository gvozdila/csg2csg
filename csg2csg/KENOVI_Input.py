#/usr/env/python3

from csg2csg.Input import InputDeck #, get_surface_with_id





class KenoviInput(InputDeck):
    """ Kenovi_InputDeck class - does the actuall processing 
    """
    preserve_xsid = False

    # constructor
    def __init__(self, filename =""):
        InputDeck.__init__(self,filename)
        
        
        
        
        
    # main write MCNP method, depnds on where the geometry
    # came from
    def write_kenovi(self, filename, flat = True):
        f = open(filename, 'w')
        
        self.__write_name_and_title(f)
        
        
        self.__write_parameters(f)
        self.__write_mixt(f)
        self.__write_geometry(f)
        self.__write_array(f)
        self.__write_endoffile(f)
        #self.__write_mcnp_cells(f)
        #self.__write_mcnp_surfaces(f)
        #self.__write_mcnp_materials(f)
        f.close()
    
    def __write_name_and_title(self, filestream):
        filestream.write("=KENOVI\n") # blank line
        string_line=self.title + "\n"
        filestream.write(string_line) # blank line
        pass
    
    def __write_parameters(self, filestream):
        filestream.write("READ PARAMETERS\n") # blank line
        string_line="END PARAMETERS" + "\n"
        filestream.write(string_line) # blank line
        pass
    
    def __write_mixt(self,  filestream):
        pass
        
    def __write_array(self, filestream):
        pass
        
    
    
    def __write_geometry(self, filestream):
        filestream.write("C surface definitions\n")
        for surface in self.surface_list:
            write_mcnp_surface(filestream, surface)
        filestream.write("\n") # blank line


        
    # perhaps these write functions should actually build strings 
    # and then write at once?
    # write all surfaces to mcnp format
    def __write_mcnp_surfaces(self, filestream):
        filestream.write("C surface definitions\n")
        for surface in self.surface_list:
            write_mcnp_surface(filestream, surface)
        filestream.write("\n") # blank line

    # write all cells to mcnp format
    def __write_mcnp_cells(self, filestream):
        filestream.write("C cell definitions\n")
        for cell in self.cell_list:
            write_mcnp_cell(filestream, cell)
        filestream.write("\n") # the important blank line

    # write all cells to mcnp format
    def __write_mcnp_materials(self, filestream):
        filestream.write("C material definitions\n")
        for material in sorted(self.material_list.keys()):
            write_mcnp_material(filestream, self.material_list[material], self.preserve_xsid )
            
            
    def __write_endoffile(self, filestream):
        filestream.write("END\n") # end of kenovi input file line
        pass
