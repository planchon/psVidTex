from xml.dom import minidom

class SVGHandler():
    def __init__(self, svgFile):
        svgData = self.openDocument(svgFile)
        defs    = self.getDefs(svgData)
        ids     = self.getIDs(svgData)
        
    def openDocument(self, path):
        return minidom.parse(path)

    def getDefs(self, svgData):
        return svgData.getElementsByTagName('path')

    def getIDs(self, svgData):
        return svgData.getElementsByTagName('use')
    
    
