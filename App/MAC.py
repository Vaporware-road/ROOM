#!/usr/bin/env
# Start
# MAC Module
# Modules
import logMac
import pprint
import living

# Logging with locMac Module
logger = logMac.LogWriter()
logger.file_name = "mac_loger.log"


def pprinter(dictiona):
    return pprint.pprint(dictiona)


class Nature:
    
    def metal(self, shape:str, metalType:str, flexibility:str, color:str):
        """  """
        metal = {
            "shape" : shape,
            "metal_type" : metalType,
            "flexibility" : flexibility,
            "color" : color
        }
        pretified = pprinter(metal)
        logger.info(f"metal with {pretified} attribute had saved")
        return metal


    def wood(self, shape, woodType, flexibility, color):
        """  """
        wood = {
            "shape" : shape,
            "wood_type" : woodType,
            "flexibility" : flexibility,
            "color" : color
        }
        pretified = pprinter(wood)
        logger.info(f"wood with {wood} attribute had saved")
        return wood

    def plastic(self, shape, plasticType, flexibility, color):
        """  """
        plastic = {                
            "shape" : shape,
            "plastic_type" : plasticType,
            "flexibility" : flexibility,
            "color" : color
        }        
        pretified = pprinter(plastic)
        logger.info(f"plastic with {plastic} attribute had saved")
        return plastic

    def glass(self, shape:str, glassType:str, flexibility:str, color:str):
        """  """
        glass = {
            "shape" : shape,
            "glass_type" : glassType,
            "flexibility" : flexibility,
            "color" : color
        }
        pretified = pprinter(glass)
        logger.info(f"glass with {glass} attribute had saved")
        return glass


class Pet(living.Living):
    """ A List of pets from cat to fishes 
    there are kinds of pets you can choose
    for seeing the list you should call::
         Pet.animal_list()
    if you choose any cat, dog, bird or fish outside of the list
    it will raise an Error"""   

    def cat(self, name):
        name = {"cat" : name}
        return name.update(self.cats)

    def dog(self, name):
        name = {"dog" : name}
        return name.update(self.dogs)


    def bird(self, name):
        name = {"bird" : name}
        return name.update(self.birds)

    def fish(self, name):
        name = {"fish" : name}
        return name.update(self.fishes)


    def animal_list(self, pet):
        """ A list of Available Cats, Dogs, Birds or fishes 
        you only can use this avalilable pets::
            self.animal_list(dog) -> list[dog_breads]"""
        
        animals = {
            "birds" : [
                    "kiwi",
                    "eagle",
                    "parret",
                    "crow",
                    "pigeon",
                    "owl"
                    ],

            "cats" : [
                    "abyssinian",
                    "aegean",
                    "balinese",
                    "bengal",
                    "birman",
                    "bombay"
                    ],

            "dogs" : [
                    "akbash",
                    "bulldog",
                    "malamute",
                    "dingo",
                    "Foxhound",
                    "loepard"
                    ],

            "fishes" : [
                    "goldfish",
                    "guppy",
                    "betta",
                    "cherryBarb",
                    "Anglefish"
                    "discus"
                    ]
            }
        for key in animals.keys():
            if key == pet:
                return animals[pet]
            else:
                raise ValueError("CHOSEN PET DOESN'T EXIST")


def physicality(hardship, unit, weight, area):
    physica = {
        "hardship" : hardship,
        "unti" : unit,
        "weight" : weight,
        "area" : area
    }
    pretified = pprinter(physica)
    logger.info(f"physicality with {physica} attribute had saved")
    return physica


# End
