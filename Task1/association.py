"""Association"""


class Processor:

    def __init__(self, model, frequency, cores):
        self.__model = model
        self.__frequency = frequency
        self.__cores = cores

    def getModel(self):
        return self.__model
    
    def setModel(self, model):
        self.__model = model
    model = property(getModel, setModel)
    
    def getFrequency(self):
        return self.__frequency
    
    def setFrequency(self, frequency):
        self.__frequency = frequency
    frequency = property(getFrequency, setFrequency)
    
    def getCores(self):
        return self.__cores
    
    def setCores(self, cores):
        self.__cores = cores
    cores = property(getCores, setCores)


# composition
class MobilePhoneBest:

    def __init__(self, antenna, battery, box, model, frequency, cores):
        self.__antenna = antenna
        self.__battery = battery
        self.__box = box
        self.__processor = Processor(model, frequency, cores)
    
    def getAntenna(self):
        return self.__antenna
    
    def setAntenna(self, antenna):
        self.__antenna = antenna
    antenna = property(getAntenna, setAntenna)
    
    def getBattery(self):
        return self.__battery
    
    def setBattery(self, battery):
        self.__battery = battery
    battery = property(getBattery, setBattery)
    
    def getBox(self):
        return self.__box
    
    def setBox(self, box):
        self.__box = box
    box = property(getBox, setBox)
    
    def getProcessor(self):
        return self.__processor
    
    def setProcessor(self, processor):
        self.__processor = processor
    processor = property(getProcessor, setProcessor)
        

# aggregation
class MobilePhoneBad:

    def __init__(self, antenna, battery, box, processor):
        self.__antenna = antenna
        self.__battery = battery
        self.__box = box
        self.__processor = processor
        
    def getAntenna(self):
        return self.__antenna

    def setAntenna(self, antenna):
        self.__antenna = antenna
    antenna = property(getAntenna, setAntenna)
    
    def getBattery(self):
        return self.__battery
    
    def setBattery(self, battery):
        self.__battery = battery
    battery = property(getBattery, setBattery)
    
    def getBox(self):
        return self.__box
    
    def setBox(self, box):
        self.__box = box
    box = property(getBox, setBox)
    
    def getProcessor(self):
        return self.__processor
    
    def setProcessor(self, processor):
        self.__processor = processor
    processor = property(getProcessor, setProcessor)
    

bestphone = MobilePhoneBest("antenna Nokia", "battary Samsung", "box Titan", "model Apple A3", "4,7 GHz", "16 cores")
# print(bestphone.__dict__)
# print(bestphone.antenna)
# print(bestphone.battery)
# print(bestphone.box)
# print(bestphone.processor.model)
# print(bestphone.processor.frequency)
# print(bestphone.processor.cores)
print(f'{bestphone.antenna} {bestphone.battery} {bestphone.box} {bestphone.processor.model} {bestphone.processor.frequency} {bestphone.processor.cores}')

processor = Processor("Snapdragon 810", "2 GHz", "8 cores")
badphone = MobilePhoneBad("antenna Tuyama", "battary Tukanava", "box Plastic", processor)
# print(badphone.__dict__)
# print(badphone.antenna)
# print(badphone.battery)
# print(badphone.box)
# print(badphone.processor.model)
# print(badphone.processor.frequency)
# print(badphone.processor.cores)
print(f'{badphone.antenna} {badphone.battery} {badphone.box} {badphone.processor.model} {badphone.processor.frequency} {badphone.processor.cores}')
