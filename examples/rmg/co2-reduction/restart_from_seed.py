restartFromSeed(path='seed')

database(
    thermoLibraries = ['electrocatThermo', 'surfaceThermoPt111', 'primaryThermoLibrary', 'DFT_QCI_thermo', 'thermo_DFT_CCSDTF12_BAC'],
    reactionLibraries = [('Surface/CPOX_Pt/Deutschmann2006_adjusted', False)],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['surface', 'electrochem', 'Surface_Proton_Electron_Reduction_Alpha', 'Surface_Proton_Electron_Reduction_Beta', 'Surface_Proton_Electron_Reduction_Beta_Dissociation'],
    kineticsEstimator = 'rate rules',
)

catalystProperties(
    metal = 'Cu111',
    coverageDependence = False,
)
"""
catalystProperties(
    bindingEnergies = {
                        'H': (-2.58383, 'eV/molecule'),
                        'O': (-4.20764, 'eV/molecule'),
                        'C': (-4.96034, 'eV/molecule'),
                        'N': (-3.58447, 'eV/molecule'),
                    },
    surfaceSiteDensity=(2.943e-9, 'mol/cm^2'),
)
"""
species(
    label="co2",
    reactive=True,
    structure=SMILES("O=C=O"),
)

species(
    label="proton",
    reactive=True,
    structure=adjacencyList("""
        1 H u0 p0 c+1
                    """),
)

species(
    label='X',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)

species(
    label = 'cXo2',
    reactive = True,
    structure = adjacencyList("""
                1 O u0 p2 c0 {2,D}
                2 C u0 p0 c0 {1,D} {3,S} {4,S}
                3 O u1 p2 c0 {2,S}
                4 X u0 p0 c0 {2,S}
                              """),
)

species(
    label = 'co2X',
    reactive = True,
    structure = adjacencyList("""
                1 O u0 p2 c0 {2,D}
                2 C u1 p0 c0 {1,D} {3,S}
                3 O u0 p2 c0 {2,S} {4,S}
                4 X u0 p0 c0 {3,S} 
                              """),
)

species(
    label = 'co2X2',
    reactive = True,
    structure = adjacencyList("""
                1 O u0 p2 c0 {2,S} {5,S}
                2 C u0 p1 c0 {1,S} {3,S}
                3 O u0 p2 c0 {2,S} {4,S}
                4 X u0 p0 c0 {3,S} 
                5 X u0 p0 c0 {1,S}
                              """),
)

species(
    label="HX",
    reactive=True,
    structure=adjacencyList("""
        1 H u0 p0 c0 {2,S}
        2 X u0 p0 c0 {1,S}
                        """),
)

species(
    label="H2",
    reactive=True,
    structure=adjacencyList("""
        1 H u0 p0 c0 {2,S}
        2 H u0 p0 c0 {1,S}
                        """),
)

species(
    label="water",
    reactive=True,
    structure=adjacencyList("""
        1 O u0 p2 c0 {2,S} {3,S}
        2 H u0 p0 c0 {1,S}
        3 H u0 p0 c0 {1,S}
                        """),
)


liquidSurfaceReactor(
    temperature=(300,'K'),
    #initialPressure=(1.0, 'bar'),
    liqPotential=(0.0,'V'),
    surfPotential=(-1.2,'V'),
    initialConcentrations={
        "co2": (1.0e-3,'mol/cm^3'),
        "proton": (1.0e-3,'mol/cm^3'),
    },
    initialSurfaceCoverages={
        "HX": 0.0,
        "co2X": 0.0,
        "cXo2": 0.0,
        'co2X2': 0.0,
        "X": 1.0,
    },
    surfaceVolumeRatio=(1.0e5, 'm^-1'),
    terminationTime=(1.0e-3,'sec'),
)

solvation(
    solvent='water'
)

simulator(
    atol=1e-16,
    rtol=1e-6,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.1,
    toleranceInterruptSimulation=1e6,
    maximumEdgeSpecies=100000,
    filterReactions=False,
    #toleranceBranchReactionToCore=0.001,
    #filterReactions=True,
)