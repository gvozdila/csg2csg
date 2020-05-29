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
        
        self.write_name_and_title(f)
        # TODO: use \t to build beautiful KENOVI input file
        
        self.write_parameters(f)
        self.write_mixt(f)
        self.write_geometry(f)
        self.write_array(f)
        self.write_endoffile(f)
        #self.__write_mcnp_cells(f)
        #self.__write_mcnp_surfaces(f)
        #self.__write_mcnp_materials(f)
        f.close()
    
    def write_name_and_title(self, filestream):
        filestream.write("=KENOVI\n") # blank line
        string_line=self.title + "\n"
        filestream.write(string_line) # blank line
        pass
    
    def write_parameters(self, filestream):
        filestream.write("READ PARAMETERS\n") # blank line
        string_line="END PARAMETERS" + "\n"
        filestream.write(string_line)
        pass
    
    def write_mixt(self,  filestream):
        filestream.write("READ MIXT\n")
        
        filestream.write("END MIXT" + "\n")
        pass
        
    def write_geometry(self, filestream):
        filestream.write("C surface definitions\n")
        filestream.write("READ GEOMETRY\n")
        
        max_universe_number = self.get_max_unused_universe()
        for universe_number in self.get_universes_list():
            filestream.write("unit " + str(universe_number) + "\n") 
            self.write_unit(universe_number)
            
        self.write_global_unit(max_universe_number)
                
        for surface in self.surface_list:
            #write_mcnp_surface(filestream, surface)
            pass
        filestream.write("\n") # blank line
        filestream.write("END GEOMETRY" + "\n")
    
    def get_max_unused_universe(self):
        # TODO: get max unused
        return 666
        pass
        
    def get_universes_list(self):
        # TODO: return universes list, exept default universe=0
        return [ 1]
        
    def write_unit(self, universe_number):
        # TODO: write unit with u=universe_number surfaces and medias(cells)
        pass
        
    def write_global_unit(self, max_universe_number):
        # TODO: create basic universe UNIT
        pass
        
    def write_array(self, filestream):
        filestream.write("READ ARRAY\n")
        
        filestream.write("END ARRAY" + "\n")
        pass
        
    
    


        
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
            
            
    def write_endoffile(self, filestream):
        filestream.write("END\n") # end of kenovi input file line
        pass
