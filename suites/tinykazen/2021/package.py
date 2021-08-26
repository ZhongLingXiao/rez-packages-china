name = "tinykazen"

version = "2021"

authors = [
    "ZhongLingXiao"
]

description = \
    """
    Bundle for tinykazen dev.
    """

requires = [
    # TODO: non-std, however is convenient for development. Move these to other suite in final commit. 
    "cmake-3.20",
    "embree-3.13.0",
    "enoki-0.1.0",
    "fmt-7.1.3",   
    "oiio-2.2.15",
    
    # CY2021 standard
    "boost-1.73",
    "ocio-2.0.1",
    "openexr-2.4.3",
    "python-3.7",
    "tbb-2020.2",
]

uuid = "tinykazen"