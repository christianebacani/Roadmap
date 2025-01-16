# Load Module

def load(transformedGadgetsDF):
    targetFilepath = 'Target Data Files\\Transformed Gadgets Dataset\\GadgetsData.csv'
    transformedGadgetsDF.to_csv(targetFilepath, index=False)
    
    return transformedGadgetsDF
