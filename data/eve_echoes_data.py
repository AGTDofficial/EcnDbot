"""
EVE Echoes Game Data Models
Ships and Skills data structures for the EVE Corp Navigator Bot
"""

# Ship Categories and Ships Data
SHIP_CATEGORIES = {
    "Frigate": {
        "description": "Small, fast, and agile ships",
        "Basic Frigates": {
            "ships": {
                "Condor": {"type": "Combat", "tier": 1, "description": "Basic combat frigate"},
                "Slasher": {"type": "Combat", "tier": 1, "description": "Basic combat frigate"},
                "Executioner": {"type": "Combat", "tier": 1, "description": "Basic combat frigate"},
                "Atron": {"type": "Combat", "tier": 1, "description": "Basic combat frigate"}
            }
        },
        "Frigates": {
            "ships": {
                "Griffin": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Merlin": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Kestrel": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Condor II": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Heron": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Vigil": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Rifter": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Bleacher": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Slasher II": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Probe": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Crucifier": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Tormentor": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Punisher": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Executioner II": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Magnate": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Maulus": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Tristan": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Incursus": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Atron II": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Imicus": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"}
            }
        },
        "Faction Frigates": {
            "ships": {
                "Pacifier": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Worm": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Dramiel": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Cruor": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Astero": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Garmur": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Succubus": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Daredevil": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"}
            }
        },
        "Interceptor Frigates": {
            "ships": {
                "Condor Interceptor": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Condor Interceptor II": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Slasher Interceptor": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Slasher Interceptor II": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Executioner Interceptor": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Executioner Interceptor II": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Atron Interceptor": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Atron Interceptor II": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"}
            }
        },
        "Assault Frigates": {
            "ships": {
                "Merlin Assault": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Breacher Assault": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Punisher Assault": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Incursus Assault": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"}
            }
        },
        "Covert Frigates": {
            "ships": {
                "Heron Covert Ops": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Heron Explorer": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Probe Covert Ops": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Probe Explorer": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Magnate Covert Ops": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Magnate Explorer": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Imicus Covert Ops": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Imicus Explorer": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"}
            }
        },
        "Stealth Bombers": {
            "ships": {
                "Manticore": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Manticore II": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Manticore III": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Hound": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Hound II": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Hound III": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Purifier": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Purifier II": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Purifier III": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Nemesis": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Nemesis II": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Nemesis III": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"}
            }
        },
        "Logistics Frigates": {
            "ships": {
                "Bantam": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Bantam II": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Burst": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Burst II": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Inquisitor": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Inquisitor II": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Navitas": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Navitas II": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"}
            }
        },
        "Navy Issue Frigates": {
            "ships": {
                "Kestrel Navy Issue": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Rifter Fleet Issue": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"},
                "Punisher Navy Issue": {"type": "Combat", "tier": 2, "description": "Caldari combat frigate"},
                "Incursus Navy Issue": {"type": "Combat", "tier": 2, "description": "Minmatar combat frigate"},
                "Tristan Navy Issue": {"type": "Combat", "tier": 2, "description": "Amarr combat frigate"}
            }
        }
    },
    "Destroyer": {
        "description": "Medium-sized ships with good firepower",
        "Basic Destroyers": {
            "ships": {
                "Cormorant": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Corax": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Cormorant II": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Cormorant Navy Issue": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"},
                "Corax Trainer": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Thrasher": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Talwar": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Thrasher II": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"},
                "Thrasher Fleet Issue": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Talwar Trainer": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Coercer": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Dragoon": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"},
                "Coercer II": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Coercer Navy Issue": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Dragoon Trainer": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Catalyst": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"},
                "Algos": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Catalyst II": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Catalyst Navy Issue": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Algos Trainer": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"}
            }
        },
        "Interdictor Destroyers": {
            "ships": {
                "Cormorant Interdictor": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Cormorant II Interdictor": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Cormorant III Interdictor": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Thrasher Interdictor": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"},
                "Thrasher II Interdictor": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Thrasher III Interdictor": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Coercer Interdictor": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Coercer II Interdictor": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"},
                "Coercer III Interdictor": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Catalyst Interdictor": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Catalyst II Interdictor": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Catalyst III Interdictor": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"}
            }
        },
        "Command Destroyers": {
            "ships": {
                "Corax Command": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Talwar Command": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Dragoon Command": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Algos Command": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"}
            }
        },
        "Tactical Destroyers": {
            "ships": {
                "Corax Sniper": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Talwar Sniper": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Dragoon Sniper": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Algos Sniper": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"},
                "Allegiance": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Xian-Yue": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Nightcrow": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Salamander": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"},
                "Endurer": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Erato": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"}
            }
        },
        "Force Field  Destroyers": {
            "ships": {
                "Cormorant Guardian": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Thrasher Guardian": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Coercer Guardian": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Catalyst Guardian": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"}
            }
        },
        "Assault Destroyers": {
            "ships": {
                "Corax Assault": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Corax II Assault": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Talwar Assault": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Talwar II Assault": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"},
                "Dragoon Assault": {"type": "Combat", "tier": 1, "description": "Caldari combat destroyer"},
                "Dragoon II Assault": {"type": "Combat", "tier": 1, "description": "Gallente combat destroyer"},
                "Algos Assault": {"type": "Combat", "tier": 1, "description": "Minmatar combat destroyer"},
                "Algos II Assault": {"type": "Combat", "tier": 1, "description": "Amarr combat destroyer"}
            }
        }           
    },
    "Cruiser": {
        "description": "Large, versatile ships with multiple roles",
        "Basic Cruisers": {
            "ships": {
                "Blackbird": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Caracal": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Moa": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Caracal Navy Issue": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Caracal Trainer": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Moa Trainer": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Caracal II": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Bellicose": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Stabber": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Stabber Fleet Issue": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Rupture": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Stabber Trainer": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Rupture Trainer": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Stabber II": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Arbitrator": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Omen": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Omen Navy Issue": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Omen Trainer": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Maller": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Maller Trainer": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Omen II": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Celestis": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Vexor": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Vexor Navy Issue": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Thorax": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Vexor Trainer": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Thorax Trainer": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Thorax Prototype": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Vexor II": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"}
            }
        },
        "Faction Heavy  Cruisers": {
            "ships": {
                "Enforcer": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Gila": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Chameleon": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Cynabal": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Saleos": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Ashimmu": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Stratios": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Orthrus": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Phantasm": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Fiend": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Vigilant": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Adrestia": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"}
            }
        },
        "Force Recon Cruisers": {
            "ships": {
                "Blackbird Covert Ops": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Blackbird II Covert Ops": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Blackbird III Covert Ops": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Bellicose Covert Ops": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Bellicose II Covert Ops": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Bellicose III Covert Ops": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Arbitrator Covert Ops": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Arbitrator II Covert Ops": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Arbitrator III Covert Ops": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Celestis Covert Ops": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Celestis II Covert Ops": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Celestis III Covert Ops": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
            "Blackbird Interdictor": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"}
            }
        },
        "Heavy Interdiction Cruisers": {
            "ships": {
                "Moa Interdictor": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Bellicose Interdictor": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Rupture Interdictor": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Arbitrator Interdictor": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Maller Interdictor": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Celestis Interdictor": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Thorax Interdictor": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"}
            }
        },
        "Force Field Cruisers": {
            "ships": {
                "Moa Guardian": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Moa II Guardian": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Rupture Guardian": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Rupture II Guardian": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Maller Guardian": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Maller II Guardian": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Thorax Guardian": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Thorax II Guardian": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"}
            }
        },
        "Sniper Cruisers": {
            "ships": {
                "Caracal Sniper": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Stabber Sniper": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Omen Sniper": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Vexor Sniper": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"}
            }
        },
        "Logistics Cruisers": {
            "ships": {
                "Osprey": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Osprey II": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Scythe": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Scythe II": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"},
                "Augoror": {"type": "Combat", "tier": 1, "description": "Gallente cruiser"},
                "Augoror II": {"type": "Combat", "tier": 1, "description": "Minmatar cruiser"},
                "Exequror": {"type": "Combat", "tier": 1, "description": "Amarr cruiser"},
                "Exequror II": {"type": "Combat", "tier": 1, "description": "Caldari cruiser"}
            }
        }
    },
    "Battlecruiser": {
        "description": "Heavy combat ships with powerful weapons",
        "Combat Battlecruisers": {
            "ships": {
                "Ferox": {"type": "Combat", "tier": 1, "description": "Caldari battlecruiser"},
                "Drake": {"type": "Combat", "tier": 1, "description": "Gallente battlecruiser"},
                "Cyclone": {"type": "Combat", "tier": 1, "description": "Minmatar battlecruiser"},
                "Hurricane": {"type": "Combat", "tier": 1, "description": "Amarr battlecruiser"},
                "Hurricane Prototype": {"type": "Combat", "tier": 1, "description": "Caldari advanced battlecruiser"},
                "Prophecy": {"type": "Combat", "tier": 2, "description": "Gallente advanced battlecruiser"},
                "Harbinger": {"type": "Combat", "tier": 2, "description": "Minmatar advanced battlecruiser"},
                "Harbinger Prototype": {"type": "Combat", "tier": 2, "description": "Amarr advanced battlecruiser"},
                "Myrmidon": {"type": "Combat", "tier": 3, "description": "Caldari elite battlecruiser"},
                "Brutix": {"type": "Combat", "tier": 3, "description": "Gallente elite battlecruiser"},
                "Can-Yue": {"type": "Combat", "tier": 3, "description": "Minmatar elite battlecruiser"}
            }
        },
        "Assault Battlecruisers": {
            "ships": {
                "Naga": {"type": "Combat", "tier": 3, "description": "Amarr elite battlecruiser"},
                "Naga II": {"type": "Combat", "tier": 3, "description": "Caldari elite battlecruiser"},
                "Naga III": {"type": "Combat", "tier": 3, "description": "Gallente elite battlecruiser"},
                "Tornado": {"type": "Combat", "tier": 3, "description": "Minmatar elite battlecruiser"},
                "Tornado II": {"type": "Combat", "tier": 3, "description": "Amarr elite battlecruiser"},
                "Tornado III": {"type": "Combat", "tier": 3, "description": "Caldari elite battlecruiser"},
                "Oracle": {"type": "Combat", "tier": 3, "description": "Gallente elite battlecruiser"},
                "Oracle II": {"type": "Combat", "tier": 3, "description": "Minmatar elite battlecruiser"},
                "Oracle III": {"type": "Combat", "tier": 3, "description": "Amarr elite battlecruiser"},
                "Talos": {"type": "Combat", "tier": 3, "description": "Caldari elite battlecruiser"},
                "Talos II": {"type": "Combat", "tier": 3, "description": "Gallente elite battlecruiser"},
                "Talos III": {"type": "Combat", "tier": 3, "description": "Minmatar elite battlecruiser"}
            }
        },
        "Command Ships": {
            "ships": {
                "Ferox Command": {"type": "Combat", "tier": 3, "description": "Amarr elite battlecruiser"},
                "Ferox II Command": {"type": "Combat", "tier": 3, "description": "Caldari elite battlecruiser"},
                "Cyclone Command": {"type": "Combat", "tier": 3, "description": "Gallente elite battlecruiser"},
                "Cyclone II Command": {"type": "Combat", "tier": 3, "description": "Minmatar elite battlecruiser"},
                "Prophecy Command": {"type": "Combat", "tier": 3, "description": "Amarr elite battlecruiser"},
                "Prophecy II Command": {"type": "Combat", "tier": 3, "description": "Caldari elite battlecruiser"},
                "Myrmidon Command": {"type": "Combat", "tier": 3, "description": "Gallente elite battlecruiser"},
                "Myrmidon II Command": {"type": "Combat", "tier": 3, "description": "Minmatar elite battlecruiser"}
            }
        },
        "Logistics Battlecruisers": {
            "ships": {
                "Drake Logistics": {"type": "Combat", "tier": 3, "description": "Amarr elite battlecruiser"},
                "Hurricane Logistics": {"type": "Combat", "tier": 3, "description": "Caldari elite battlecruiser"},
                "Harbinger Logistics": {"type": "Combat", "tier": 3, "description": "Gallente elite battlecruiser"},
                "Brutix Logistics": {"type": "Combat", "tier": 3, "description": "Minmatar elite battlecruiser"}
            }
        },
        "Force Field Battlecruisers": {
            "ships": {
                "Ferox Guardian": {"type": "Combat", "tier": 3, "description": "Amarr elite battlecruiser"},
                "Drake Guardian": {"type": "Combat", "tier": 3, "description": "Caldari elite battlecruiser"},
                "Cyclone Guardian": {"type": "Combat", "tier": 3, "description": "Gallente elite battlecruiser"},
                "Hurricane Guardian": {"type": "Combat", "tier": 3, "description": "Minmatar elite battlecruiser"},
                "Prophecy Guardian": {"type": "Combat", "tier": 3, "description": "Amarr elite battlecruiser"},
                "Harbinger Guardian": {"type": "Combat", "tier": 3, "description": "Caldari elite battlecruiser"},
                "Myrmidon Guardian": {"type": "Combat", "tier": 3, "description": "Gallente elite battlecruiser"},
                "Brutix Guardian": {"type": "Combat", "tier": 3, "description": "Minmatar elite battlecruiser"}
            }
        }
    },
    "Industrial Ships": {
        "description": "Industrial ships for resource extraction and Transport",
        "Transport Ships": {
            "ships": {
                "Tayra": {"type": "Industrial", "tier": 1, "description": "Caldari industrial ship"},
                "Badger": {"type": "Industrial", "tier": 1, "description": "Gallente industrial ship"},
                "Badger II": {"type": "Industrial", "tier": 1, "description": "Minmatar industrial ship"},
                "Wreathe": {"type": "Industrial", "tier": 1, "description": "Amarr industrial ship"},
                "Mammoth": {"type": "Industrial", "tier": 2, "description": "Caldari advanced industrial ship"},
                "Wreathe II": {"type": "Industrial", "tier": 2, "description": "Gallente advanced industrial ship"},
                "Bestower": {"type": "Industrial", "tier": 2, "description": "Minmatar advanced industrial ship"},
                "Sigil": {"type": "Industrial", "tier": 2, "description": "Amarr advanced industrial ship"},
                "Sigil II": {"type": "Industrial", "tier": 2, "description": "Caldari advanced industrial ship"},
                "Kryos": {"type": "Industrial", "tier": 2, "description": "Gallente advanced industrial ship"},
                "Nereus": {"type": "Industrial", "tier": 2, "description": "Minmatar advanced industrial ship"},
                "Nereus II": {"type": "Industrial", "tier": 2, "description": "Amarr advanced industrial ship"},
                "Nereus High Mobility": {"type": "Industrial", "tier": 2, "description": "Caldari advanced industrial ship"},
                "Nereus Combat": {"type": "Industrial", "tier": 2, "description": "Gallente advanced industrial ship"},
                "Nereus Hauling": {"type": "Industrial", "tier": 2, "description": "Minmatar advanced industrial ship"},
                "Imicus High Mobility": {"type": "Industrial", "tier": 2, "description": "Amarr advanced industrial ship"},
                "Humpback High Mobility": {"type": "Industrial", "tier": 2, "description": "Caldari advanced industrial ship"},
                "Humpback Combat": {"type": "Industrial", "tier": 2, "description": "Gallente advanced industrial ship"},
                "Humpback Hauling": {"type": "Industrial", "tier": 2, "description": "Minmatar advanced industrial ship"},
                "Noctis": {"type": "Industrial", "tier": 2, "description": "Amarr advanced industrial ship"},
                "Noctis II": {"type": "Industrial", "tier": 2, "description": "Caldari advanced industrial ship"}
            }
        },
        "Expedition Vessels": {
            "ships": {
                "Venture Trainer": {"type": "Industrial", "tier": 2, "description": "Gallente advanced industrial ship"},
                "Venture": {"type": "Industrial", "tier": 2, "description": "Minmatar advanced industrial ship"},
                "Venture II": {"type": "Industrial", "tier": 2, "description": "Amarr advanced industrial ship"},
                "Venture III": {"type": "Industrial", "tier": 2, "description": "Caldari advanced industrial ship"},
                "Venture IV": {"type": "Industrial", "tier": 2, "description": "Gallente advanced industrial ship"},
                "Venture Covert Ops": {"type": "Industrial", "tier": 2, "description": "Minmatar advanced industrial ship"}
            }
        },
        "Mining Barges": {
            "ships": {
                "Retriever": {"type": "Industrial", "tier": 2, "description": "Amarr advanced industrial ship"},
                "Procurer": {"type": "Industrial", "tier": 2, "description": "Caldari advanced industrial ship"},
                "Covetor": {"type": "Industrial", "tier": 2, "description": "Gallente advanced industrial ship"},
                "Covetor II": {"type": "Industrial", "tier": 2, "description": "Minmatar advanced industrial ship"}
            }
        },
        "Industrial Command Ships": {
            "ships": {
                "Orca": {"type": "Industrial", "tier": 2, "description": "Amarr advanced industrial ship"}
            }
        }
    },
    "Battleship": {
        "description": "Massive ships with overwhelming firepower",
        "Battleships": {
            "ships": {
                "Scorpion": {"type": "Combat", "tier": 1, "description": "Caldari battleship"},
                "Raven": {"type": "Combat", "tier": 1, "description": "Gallente battleship"},
                "Rokh": {"type": "Combat", "tier": 2, "description": "Minmatar battleship"},
                "Scorpion II": {"type": "Combat", "tier": 2, "description": "Amarr battleship"},
                "Tempest": {"type": "Combat", "tier": 2, "description": "Caldari advanced battleship"},
                "Typhoon": {"type": "Combat", "tier": 2, "description": "Gallente advanced battleship"},
                "Typhoon II": {"type": "Combat", "tier": 2, "description": "Minmatar advanced battleship"},
                "Maelstrom": {"type": "Combat", "tier": 2, "description": "Amarr advanced battleship"},
                "Armageddon": {"type": "Combat", "tier": 2, "description": "Caldari advanced battleship"},
                "Apocalypse": {"type": "Combat", "tier": 2, "description": "Gallente advanced battleship"},
                "Abaddon": {"type": "Combat", "tier": 2, "description": "Minmatar advanced battleship"},
                "Armageddon II": {"type": "Combat", "tier": 2, "description": "Amarr advanced battleship"},
                "Dominix": {"type": "Combat", "tier": 2, "description": "Caldari advanced battleship"},
                "Megathron": {"type": "Combat", "tier": 2, "description": "Gallente advanced battleship"},
                "Hyperion": {"type": "Combat", "tier": 2, "description": "Minmatar advanced battleship"},
                "Dominix II": {"type": "Combat", "tier": 2, "description": "Amarr advanced battleship"}
            }
        },
        "Siege Battleships": {
            "ships": {
                "Raven Striker": {"type": "Combat", "tier": 2, "description": "Caldari advanced battleship"},
                "Tempest Striker": {"type": "Combat", "tier": 2, "description": "Gallente advanced battleship"},
                "Apocalypse Striker": {"type": "Combat", "tier": 2, "description": "Minmatar advanced battleship"},
                "Megathron Striker": {"type": "Combat", "tier": 2, "description": "Amarr advanced battleship"}
            }
        },
        "Faction Battleships": {
            "ships": {
                "Marshal": {"type": "Combat", "tier": 2, "description": "Caldari advanced battleship"},
                "Rattlesnake": {"type": "Combat", "tier": 2, "description": "Gallente advanced battleship"},
                "Machariel": {"type": "Combat", "tier": 2, "description": "Minmatar advanced battleship"},
                "Bhaalgorn": {"type": "Combat", "tier": 2, "description": "Amarr advanced battleship"},
                "Nestor": {"type": "Combat", "tier": 2, "description": "Caldari advanced battleship"},
                "Barghest": {"type": "Combat", "tier": 2, "description": "Gallente advanced battleship"},
                "Nightmare": {"type": "Combat", "tier": 2, "description": "Minmatar advanced battleship"},
                "Vindicator": {"type": "Combat", "tier": 2, "description": "Amarr advanced battleship"},
                "Cobra": {"type": "Combat", "tier": 2, "description": "Caldari advanced battleship"},
                "Marzio": {"type": "Combat", "tier": 2, "description": "Gallente advanced battleship"},
                "Azazel": {"type": "Combat", "tier": 2, "description": "Minmatar advanced battleship"},
                "Anubis": {"type": "Combat", "tier": 2, "description": "Amarr advanced battleship"},
                "Annihilator": {"type": "Combat", "tier": 2, "description": "Caldari advanced battleship"}
            }
        },
        "Navy Issue Battleships": {
            "ships": {
                "Raven Navy Issue": {"type": "Combat", "tier": 2, "description": "Gallente advanced battleship"},
                "Tempest Fleet Issue": {"type": "Combat", "tier": 2, "description": "Minmatar advanced battleship"},
                "Apocalypse Navy Issue": {"type": "Combat", "tier": 2, "description": "Amarr advanced battleship"},
                "Megathron Navy Issue": {"type": "Combat", "tier": 2, "description": "Caldari advanced battleship"},
                "Dominix Navy Issue": {"type": "Combat", "tier": 2, "description": "Gallente advanced battleship"},
            }
        },
        "Special Ops Battleships": {
            "ships": {
                "Scorpion Special Ops": {"type": "Combat", "tier": 2, "description": "Minmatar advanced battleship"},
                "Typhoon Special Ops": {"type": "Combat", "tier": 2, "description": "Amarr advanced battleship"},
                "Armageddon Special Ops": {"type": "Combat", "tier": 2, "description": "Caldari advanced battleship"},
                "Dominix Special Ops": {"type": "Combat", "tier": 2, "description": "Gallente advanced battleship"},
            }
        },
        "Bomber Battleships": {
            "ships": {   
                "Rokh Bomber": {"type": "Combat", "tier": 2, "description": "Minmatar advanced battleship"},
                "Maelstrom Bomber": {"type": "Combat", "tier": 2, "description": "Amarr advanced battleship"},
                "Abaddon Bomber": {"type": "Combat", "tier": 2, "description": "Caldari advanced battleship"},
                "Hyperion Bomber": {"type": "Combat", "tier": 2, "description": "Gallente advanced battleship"}
            }
        }
    },
    "Capital Ship": {
        "description": "Massive capital ships for fleet operations",
        "Freighters": {
            "ships": {
                "Charon": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Fenrir": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Providence": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Obelisk": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
            }
        },
        "Jump Freighters": {
            "ships": {
                "Rhea": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Nomad": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Ark": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Anshar": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
            }
        },
        "Dreadnoughts": {
            "ships": {
                "Phoenix": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Karura": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Phoenix Bodyguard": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Naglfar": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Valravn": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Naglfar Bodyguard": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Revelation": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Bane": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Revelation Bodyguard": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Moros": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Hubris": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Moros Bodyguard": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
            }
        },
        "Force Auxiliary": {
            "ships": {
                "Minokawa": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Lif": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Apostle": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Ninazu": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Lucent-Moon": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
            }
        },
        "Carriers": {
            "ships": {
                "Chimera": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Chimera Navy Issue": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Nidhoggur": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Nidhoggur Fleet Issue": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Archon": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Archon Navy Issue": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Thanatos": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Thanatos Navy Issue": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "CyanSea": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Shanhai": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
            }
        }, 
        "Super Carriers": {
            "ships": {     
                "Wyvern": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Hel": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Aeon": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Nyx": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Rahab": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Midgard": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Superbia": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Hades": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
            }
        },
        "Carriers Industrial Ships": {
            "ships": {
                "Rorqual": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
            }
        },
        "Assault Carriers": {
            "ships": {
                "Anaconda": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Vassago": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Astarte": {"type": "Mining", "tier": 1, "description": "Mining capital ship"},
                "Villain": {"type": "Mining", "tier": 1, "description": "Mining capital ship"}
            }
        }
    }
}

# Skills Data Structure
SKILLS_DATA = {
    "Combat Skills": {
        "Cruising Technology": {
            "Spaceship Command": {
                "Frigate Command": {"max_level": 5, "description": "Command frigates effectively"},
                "Destroyer Command": {"max_level": 5, "description": "Command destroyers effectively"},
                "Cruiser Command": {"max_level": 5, "description": "Command cruisers effectively"},
                "Battlecruiser Command": {"max_level": 5, "description": "Command battlecruisers effectively"},
                "Battleship Command": {"max_level": 5, "description": "Command battleships effectively"},
                "Industrial Ship Command": {"max_level": 5, "description": "Command industrial ships effectively"},
                "Industrial Command Ship Command": {"max_level": 5, "description": "Command industrial command ships effectively"}
            },
            "Capital Ship Command": {
                "Freighter Command": {"max_level": 5, "description": "Command freighters effectively"},
                "Dreadnought Command": {"max_level": 5, "description": "Command dreadnoughts effectively"},
                "Carrier Command": {"max_level": 5, "description": "Command carriers effectively"},
                "Capital Industrial Ship Command": {"max_level": 5, "description": "Command capital industrial ships effectively"},
                "Jump Freighter Command": {"max_level": 5, "description": "Command jump freighters effectively"},
                "Force Auxiliary Command": {"max_level": 5, "description": "Command force auxiliaries effectively"}
            },
            "Navigation": {
                "Afterburner": {"max_level": 5, "description": "Afterburner operation"},
                "Microwarpdrive Operation": {"max_level": 5, "description": "Microwarpdrive operation"},
                "Engine Operation": {"max_level": 5, "description": "Engine operation"},
                "Jump Drive Operation": {"max_level": 5, "description": "Jump drive operation"},
                "Covert Jump Drive Operation": {"max_level": 5, "description": "Covert jump drive operation"},
                "Micro Jump Drive Operation": {"max_level": 5, "description": "Micro jump drive operation"}
            }
        },
        "Maintenance Technology": {
            "Shield Operation": {
                "Shield Operation": {"max_level": 5, "description": "Shield operation"},
                "Shield Hardening": {"max_level": 5, "description": "Shield hardening"},
                "Capital Shield Operation": {"max_level": 5, "description": "Capital shield operation"},
                "Shield Hardening Array": {"max_level": 5, "description": "Shield hardening array"},
                "Shield Generation Array": {"max_level": 5, "description": "Shield generation array"},
                "Shield Generation": {"max_level": 5, "description": "Shield generation"},
                "Shield Coordination Array": {"max_level": 5, "description": "Shield coordination array"},
                "Shield Coordination": {"max_level": 5, "description": "Shield coordination"} 
            },
            "Remote Shield": {
                "Remote Shield Operation":{"max_level": 5, "description": "Remote Shield"},
			    "Capital Shield Support Operation":{"max_level": 5, "description": "Remote Shield"},
			    "Remote Shield Reinforcement Theory":{"max_level": 5, "description": "Shield operation"},
			    "Remote Shield Reinforcement Array Theory":{"max_level": 5, "description": "Shield operation"},
			    "Remote Shield Transmission Theory":{"max_level": 5, "description": "Shield operation"},
			    "Remote Shield Transmission Array Theory":{"max_level": 5, "description": "Shield operation"},
			    "Remote Shield Optimisation Theory":{"max_level": 5, "description": "Shield operation"}
            },
            "Armor Operation": {
                "Armor Operation":{"max_level": 5, "description": "Armor operation"},
			    "Armor Hardening":{"max_level": 5, "description": "Armor operation"},
			    "Capital Armor Operation":{"max_level": 5, "description": "Armor operation"},
			    "Armor Hardening Array":{"max_level": 5, "description": "Armor operation"},
			    "Armor Convergance Array":{"max_level": 5, "description": "Armor operation"},
			    "Armor Convergance":{"max_level": 5, "description": "Armor operation"},
			    "Armor Layering Array":{"max_level": 5, "description": "Armor operation"},
			    "Armor Layering":{"max_level": 5, "description": "Armor operation"},

            },
            "Remote Armor": {
                "Remote Armor Operation":{"max_level": 5, "description": "Remote Armor"},
			    "Capital Armor Support Operation":{"max_level": 5, "description": "Remote Armor"},
			    "Remote Armor Reinforcement Theory":{"max_level": 5, "description": "Remote Armor"},
			    "Remote Armor Reinforcement Array Theory":{"max_level": 5, "description": "Remote Armor"},   
			    "Remote Armor Transmission Theory":{"max_level": 5, "description": "Remote Armor"},
			    "Remote Armor Transmission Array Theory":{"max_level": 5, "description": "Remote Armor"},
			    "Remote Armor Optimisation Theory":{"max_level": 5, "description": "Remote Armor"},
            },
            "Defense Upgrade": {
                "Frigate Defense Upgrade":{"max_level": 5, "description": "Defense upgrade"},
			    "Destroyer Defense Upgrade":{"max_level": 5, "description": "Defense upgrade"},
			    "Cruiser Defense Upgrade":{"max_level": 5, "description": "Defense upgrade"},
			    "Battlecruiser Defense Upgrade":{"max_level": 5, "description": "Defense upgrade"},
			    "Battleship Defense Upgrade":{"max_level": 5, "description": "Defense upgrade"},
			    "Industrial Ship Defense Upgrade":{"max_level": 5, "description": "Defense upgrade"},
			    "Industrial Command Ship Defense Upgrade":{"max_level": 5, "description": "Defense upgrade"},
            },
            "Capital Ship Structure": {
                "Freighter Defense Upgrade": {"max_level": 5, "description": "Capital Ship Structure    "},
			    "Dreadnought Defense Upgrade": {"max_level": 5, "description": "Capital Ship Structure"},
			    "Carrier Defense Upgrade": {"max_level": 5, "description": "Capital Ship Structure"},
			    "Capital Industrial Ship Defense Upgrade": {"max_level": 5, "description": "Capital Ship Structure"},
			    "Jump Freighter Defense Upgrade": {"max_level": 5, "description": "Capital Ship Structure"}
            },
            "Support Drones": {
			    "Logistics Drone Operation": {"max_level": 5, "description": "Logistics Drone Operation"}
            }
        },
        "Electronics": {
            "Engineering": {
                "Frigate Engineering": {"max_level": 5, "description": "Engineering"},
			    "Destroyer Engineering": {"max_level": 5, "description": "Engineering"},
			    "Cruiser Engineering": {"max_level": 5, "description": "Engineering"},
			    "Battlecruiser Engineering": {"max_level": 5, "description": "Engineering"},
			    "Battleship Engineering": {"max_level": 5, "description": "Engineering"},
			    "Industrial Ship Engineering": {"max_level": 5, "description": "Engineering"},
			    "Industrial Command Ship Engineering": {"max_level": 5, "description": "Engineering"}
            },
            "Capital Ship Engineering": {
                "Freighter Engineering": {"max_level": 5, "description": "Engineering"},
			    "Dreadnought Engineering": {"max_level": 5, "description": "Engineering"},
			    "Carrier Engineering": {"max_level": 5, "description": "Engineering"},
			    "Capital Industrial Ship Engineering": {"max_level": 5, "description": "Engineering"},
			    "Jump Freighter Engineering": {"max_level": 5, "description": "Engineering"}
            },
            "Electronic Systems": {
                "Electronic Warfare": {"max_level": 5, "description": "Electronic Warfare"},
			    "Propulsion Jamming": {"max_level": 5, "description": "Propulsion Jamming"},
			    "Signal Disruption": {"max_level": 5, "description": "Signal Disruption"},
			    "Tactical Distruptor Operation": {"max_level": 5, "description": "Tactical Distruptor Operation"}
            },
            "Targeting": {
                "Target Management": {"max_level": 5, "description": "Target Management"},
			    "Cynosural Field Technology": {"max_level": 5, "description": "Cynosural Field Technology"}
            },
            "Fleet Support": {
                "Mining Foreman": {"max_level": 5, "description": "Mining Foreman"},
			    "Shield Command": {"max_level": 5, "description": "Shield Command"},
			    "Skirmish Command": {"max_level": 5, "description": "Skirmish Command"},
			    "Armored Command": {"max_level": 5, "description": "Armored Command"},
			    "Industrial Command": {"max_level": 5, "description": "Industrial Command"},
			    "Cover Module Operation": {"max_level": 5, "description": "Cover Module Operation"},
			    "Jump Command Technology": {"max_level": 5, "description": "Jump Command Technology"},
			    "Mothership Command Technology": {"max_level": 5, "description": "Mothership Command Technology"}
            },
            "Team Combat": {
                "Team Combat": {"max_level": 5, "description": "Team Combat"},
			    "Mothership Defense Coordination": {"max_level": 5, "description": "Mothership Defense Coordination"},
			    "Damage Transfer": {"max_level": 5, "description": "Damage Transfer"},
			    "Mothership Defense": {"max_level": 5, "description": "Mothership Defense"},
			    "Team Combat Enhancement": {"max_level": 5, "description": "Team Combat Enhancement"},
			    "Team Combat Support": {"max_level": 5, "description": "Team Combat Support"}
            },
            "Burst": {
                "Energy Neutralizer Burst Operation": {"max_level": 5, "description": "Energy Neutralizer Burst Operation"},
			    "Fire Control Distruption Burst Operation": {"max_level": 5, "description": "Fire Control Distruption Burst Operation"},
			    "Radar Distruption Burst Operation": {"max_level": 5, "description": "Radar Distruption Burst Operation"},
			    "Engine Distruption Burst Operation": {"max_level": 5, "description": "Engine Distruption Burst Operation"},
			    "Power Distruption Burst Operation": {"max_level": 5, "description": "Power Distruption Burst Operation"},
			    "Defense Distruption Burst Operation": {"max_level": 5, "description": "Defense Distruption Burst Operation"}
            },

            "Quantum Entanglement": {
                "Quantum Entanglement Generator Operation": {"max_level": 5, "description": "Quantum Entanglement Generator Operation"}
            }
        },
        "Weapon Systems": {
            "Laser": {
                "Small Laser Operation": {"max_level": 5, "description": "Small Laser Operation"},
			    "Small Laser Upgrade": {"max_level": 5, "description": "Small Laser Upgrade"},
			    "Medium Laser Operation": {"max_level": 5, "description": "Medium Laser Operation"},
			    "Medium Laser Upgrade": {"max_level": 5, "description": "Medium Laser Upgrade"},
			    "Large Laser Operation": {"max_level": 5, "description": "Large Laser Operation"},
			    "Large Laser Upgrade": {"max_level": 5, "description": "Large Laser Upgrade"},
			    "Capital Laser Operation": {"max_level": 5, "description": "Capital Laser Operation"},
			    "Capital Laser Upgrade": {"max_level": 5, "description": "Capital Laser Upgrade"}
            },
            "Railgun": {
                "Small Railgun Operation": {"max_level": 5, "description": "Small Railgun Operation"},
			    "Small Railgun Upgrade": {"max_level": 5, "description": "Small Railgun Upgrade"},
			    "Medium Railgun Operation": {"max_level": 5, "description": "Medium Railgun Operation"},
			    "Medium Railgun Upgrade": {"max_level": 5, "description": "Medium Railgun Upgrade"},
			    "Large Railgun Operation": {"max_level": 5, "description": "Large Railgun Operation"},
			    "Large Railgun Upgrade": {"max_level": 5, "description": "Large Railgun Upgrade"},
			    "Capital Railgun Operation": {"max_level": 5, "description": "Capital Railgun Operation"},
			    "Capital Railgun Upgrade": {"max_level": 5, "description": "Capital Railgun Upgrade"}
            },
            "Cannon": {
                "Small Cannon Operation": {"max_level": 5, "description": "Small Cannon Operation"},
			    "Small Cannon Upgrade": {"max_level": 5, "description": "Small Cannon Upgrade"},
			    "Medium Cannon Operation": {"max_level": 5, "description": "Medium Cannon Operation"},
			    "Medium Cannon Upgrade": {"max_level": 5, "description": "Medium Cannon Upgrade"},
			    "Large Cannon Operation": {"max_level": 5, "description": "Large Cannon Operation"},
			    "Large Cannon Upgrade": {"max_level": 5, "description": "Large Cannon Upgrade"},
			    "Capital Cannon Operation": {"max_level": 5, "description": "Capital Cannon Operation"},
			    "Capital Cannon Upgrade": {"max_level": 5, "description": "Capital Cannon Upgrade"}
            },
            "Missiles": {
                "Small Missiles/Torpedo Operation": {"max_level": 5, "description": "Small Missiles/Torpedo Operation"},
			    "Small Missiles/Torpedo Upgrade": {"max_level": 5, "description": "Small Missiles/Torpedo Upgrade"},
			    "Medium Missiles/Torpedo Operation": {"max_level": 5, "description": "Medium Missiles/Torpedo Operation"},
			    "Medium Missiles/Torpedo Upgrade": {"max_level": 5, "description": "Medium Missiles/Torpedo Upgrade"},
			    "Large Missiles/Torpedo Operation": {"max_level": 5, "description": "Large Missiles/Torpedo Operation"},
			    "Large Missiles/Torpedo Upgrade": {"max_level": 5, "description": "Large Missiles/Torpedo Upgrade"},
			    "Capital Missiles/Torpedo Operation": {"max_level": 5, "description": "Capital Missiles/Torpedo Operation"},
			    "Capital Missiles/Torpedo Upgrade": {"max_level": 5, "description": "Capital Missiles/Torpedo Upgrade"},
                "Precision Guidance": {"max_level": 5, "description": "Precision Guidance"},
			    "Target Navigation Prediction": {"max_level": 5, "description": "Target Navigation Prediction"},
			    "Missiles Bombardment": {"max_level": 5, "description": "Missiles Bombardment"},
			    "Missiles Projection": {"max_level": 5, "description": "Missiles Projection"},
			    "Missiles Propulsion": {"max_level": 5, "description": "Missiles Propulsion"}
            },
            "Drone": {
                "Small Drone Operation": {"max_level": 5, "description": "Small Drone Operation"},
			    "Small Drone Upgrade": {"max_level": 5, "description": "Small Drone Upgrade"},
			    "Medium Drone Operation": {"max_level": 5, "description": "Medium Drone Operation"},
			    "Medium Drone Upgrade": {"max_level": 5, "description": "Medium Drone Upgrade"},
			    "Large Drone Operation": {"max_level": 5, "description": "Large Drone Operation"},
			    "Large Drone Upgrade": {"max_level": 5, "description": "Large Drone Upgrade"},
			    "Drone": {"max_level": 5, "description": "Drone"},
			    "Drone Interfacing": {"max_level": 5, "description": "Drone Interfacing"},
			    "Drone Navigation": {"max_level": 5, "description": "Drone Navigation"},
			    "Drone Combat": {"max_level": 5, "description": "Drone Combat"},
			    "Drone Gunnery": {"max_level": 5, "description": "Drone Gunnery"}
            },
            "Fighter": {
                "Light Fighter Operation": {"max_level": 5, "description": "Light Fighter Operation"},
			    "Light Fighter Upgrade": {"max_level": 5, "description": "Light Fighter Upgrade"},
			    "Fighter": {"max_level": 5, "description": "Fighter"},
			    "Heavy Fighter Operation": {"max_level": 5, "description": "Heavy Fighter Operation"},
			    "Heavy Fighter Upgrade": {"max_level": 5, "description": "Heavy Fighter Upgrade"},
			    "Fighter Fighting Theory": {"max_level": 5, "description": "Fighter Fighting Theory"},
			    "Fighter Navigation": {"max_level": 5, "description": "Fighter Navigation"},
			    "Fighter Combat Theory": {"max_level": 5, "description": "Fighter Combat Theory"},
			    "Fighter Defense": {"max_level": 5, "description": "Fighter Defense"}
            },
            "Lightweight Ship": {
                "Lightweight Ships": {"max_level": 5, "description": "Lightweight Ships"},
			    "Lightweight Ship Defense": {"max_level": 5, "description": "Lightweight Ship Defense"},
			    "Lightweight Ship Combat": {"max_level": 5, "description": "Lightweight Ship Combat"},
			    "Lightweight Ship Navigation": {"max_level": 5, "description": "Lightweight Ship Navigation"},
			    "Lightweight Ship Gunnery": {"max_level": 5, "description": "Lightweight Ship Gunnery"}
            },
            "Decomposer": {
                "Small Decomposer Operation": {"max_level": 5, "description": "Small Decomposer Operation"},
			    "Small Decomposer Upgrade": {"max_level": 5, "description": "Small Decomposer Upgrade"},
			    "Medium Decomposer Operation": {"max_level": 5, "description": "Medium Decomposer Operation"},
			    "Medium Decomposer Upgrade": {"max_level": 5, "description": "Medium Decomposer Upgrade"},
			    "Large Decomposer Operation": {"max_level": 5, "description": "Large Decomposer Operation"},
			    "Large Decomposer Upgrade": {"max_level": 5, "description": "Large Decomposer Upgrade"}
            },
            "Gunnery": {
                "Motion Prediction": {"max_level": 5, "description": "Motion Prediction"},
			    "Controlled Bursts": {"max_level": 5, "description": "Controlled Bursts"},
			    "Gunnery": {"max_level": 5, "description": "Gunnery"},
			    "Sharshooter": {"max_level": 5, "description": "Sharshooter"},
			    "Trajectory Analysis": {"max_level": 5, "description": "Trajectory Analysis"}
            },
            "Special Weapon": {
                "Disruptive Lance Operation": {"max_level": 5, "description": "Disruptive Lance Operation"},
			    "Disruptive Lance Theory Upgrade": {"max_level": 5, "description": "Disruptive Lance Theory Upgrade"},
			    "Bomb Deployment": {"max_level": 5, "description": "Bomb Deployment"},
			    "Capital Close-in Defense Gun Operation": {"max_level": 5, "description": "Capital Close-in Defense Gun Operation"}
            },
            "Structure Weapon": {
                "Structure Missiles Systems Operation": {"max_level": 5, "description": "Structure Missiles Systems Operation"},
			    "Structure Missiles Systems Upgrade": {"max_level": 5, "description": "Structure Missiles Systems Upgrade"},
			    "Structure Close-in Defense Gun Operation": {"max_level": 5, "description": "Structure Close-in Defense Gun Operation"}
            }
        }
    },
    "Industrial Skills": {
        "Industrial Technology": {
            "Production": {
                "Frigate Manafacture": {"max_level": 5, "description": "Frigate Manafacture"},
			    "Destroyer Manafacture": {"max_level": 5, "description": "Destroyer Manafacture"},
			    "Cruiser Manafacture": {"max_level": 5, "description": "Cruiser Manafacture"},
			    "Battlecruiser Manafacture": {"max_level": 5, "description": "Battlecruiser Manafacture"},
			    "Battleship Manafacture": {"max_level": 5, "description": "Battleship Manafacture"},
			    "Industrial Ship Manafacture": {"max_level": 5, "description": "Industrial Ship Manafacture"}
            },
            "Capital Ship Production": {
                "Freighter Manafacture": {"max_level": 5, "description": "Freighter Manafacture"},
			    "Dreadnought Manafacture": {"max_level": 5, "description": "Dreadnought Manafacture"},
			    "Carrier Manafacture": {"max_level": 5, "description": "Carrier Manafacture"},
			    "Capital Ship Manafacture": {"max_level": 5, "description": "Capital Ship Manafacture"},
			    "Capital Industrial Ship Manafacture": {"max_level": 5, "description": "Capital Industrial Ship Manafacture"},
			    "Jump Freighter Manafacture": {"max_level": 5, "description": "Jump Freighter Manafacture"},
			    "Structure Construction": {"max_level": 5, "description": "Structure Construction"}
            },
            "Component Manafacturing": {
                "Capital Ship Component Manafacturing": {"max_level": 5, "description": "Capital Ship Component Manafacturing"},
			    "Maintenance System Production Optimisation": {"max_level": 5, "description": "Maintenance System Production Optimisation"},
			    "Weapon System Production Optimisation": {"max_level": 5, "description": "Weapon System Production Optimisation"},
			    "Power System Production Optimisation": {"max_level": 5, "description": "Power System Production Optimisation"},
			    "Propulsion System Production Optimisation": {"max_level": 5, "description": "Propulsion System Production Optimisation"},
			    "Defense System Production Optimisation": {"max_level": 5, "description": "Defense System Production Optimisation"},
			    "Control System Production Optimisation": {"max_level": 5, "description": "Control System Production Optimisation"}
            },
            "Module Manafacture": {
                "Module Manafacture": {"max_level": 5, "description": "Module Manafacture"},
			    "Rig Manafacture": {"max_level": 5, "description": "Rig Manafacture"},
			    "Capital Module Manafacture": {"max_level": 5, "description": "Capital Module Manafacture"},
			    "Capital Rig Manafacture": {"max_level": 5, "description": "Capital Rig Manafacture"},
			    "Implant Manafacture": {"max_level": 5, "description": "Implant Manafacture"},
			    "Chip Manafacture": {"max_level": 5, "description": "Chip Manafacture"},
			    "Polymer Material Manafacture": {"max_level": 5, "description": "Polymer Material Manafacture"},
			    "Ammunition Manafacture": {"max_level": 5, "description": "Ammunition Manafacture"}
            },
            "Mining": {
                "Mining": {"max_level": 5, "description": "Mining"},
			    "Strip Mining": {"max_level": 5, "description": "Strip Mining"},
			    "Auto Salvage Technology": {"max_level": 5, "description": "Auto Salvage Technology"},
			    "Mining Drone Technology": {"max_level": 5, "description": "Mining Drone Technology"},
			    "Exhumer Drone Technology": {"max_level": 5, "description": "Exhumer Drone Technology"},
			    "Exhumer Drone Structure": {"max_level": 5, "description": "Exhumer Drone Structure"},
			    "Mining Drone Structure": {"max_level": 5, "description": "Mining Drone Structure"},
			    "Strip Miner Structure": {"max_level": 5, "description": "Strip Miner Structure"},
			    "Mining Laser Structure": {"max_level": 5, "description": "Mining Laser Structure"}
            },
            "Ore Reprocessing": {
                "Common Ore Reprocessing": {"max_level": 5, "description": "Common Ore Reprocessing"},
			    "Uncommon Ore Reprocessing": {"max_level": 5, "description": "Uncommon Ore Reprocessing"},
			    "Special Ore Reprocessing": {"max_level": 5, "description": "Special Ore Reprocessing"},
			    "Rare Ore Reprocessing": {"max_level": 5, "description": "Rare Ore Reprocessing"},
			    "Precision Ore Reprocessing": {"max_level": 5, "description": "Precision Ore Reprocessing"},
			    "Moon Ore Reprocessing": {"max_level": 5, "description": "Moon Ore Reprocessing"}
            },
            "Resource Processing": {
                "Scrap Metal Processing": {"max_level": 5, "description": "Scrap Metal Processing"},
			    "Ore Compression": {"max_level": 5, "description": "Ore Compression"},
			    "Neuron Repair Technology": {"max_level": 5, "description": "Neuron Repair Technology"},
			    "Implant Unit Processing": {"max_level": 5, "description": "Implant Unit Processing"}
            }
            
        },
        "Social Science": {
            "Trade": {
                "Trade": {"max_level": 5, "description": "Trade"},
			    "Accounting": {"max_level": 5, "description": "Accounting"},
			    "Freight": {"max_level": 5, "description": "Freight"}
            }
        },
        "Applied Science": {
            "Invention": {
                "Amaar Invention Principles": {"max_level": 5, "description": "Amaar Invention Principles"},
			    "Caldari Invention Principles": {"max_level": 5, "description": "Caldari Invention Principles"},
			    "Gallente Invention Principles": {"max_level": 5, "description": "Gallente Invention Principles"},
			    "Minmatar Invention Principles": {"max_level": 5, "description": "Minmatar Invention Principles"}
            },
            "Capital Ship Invention": {
                "Amaar Capital Ship Invention Principles": {"max_level": 5, "description": "Amaar Capital Ship Invention Principles"},
			    "Caldari Capital Ship Invention Principles": {"max_level": 5, "description": "Caldari Capital Ship Invention Principles"},
			    "Gallente Capital Ship Invention Principles": {"max_level": 5, "description": "Gallente Capital Ship Invention Principles"},
			    "Minmatar Capital Ship Invention Principles": {"max_level": 5, "description": "Minmatar Capital Ship Invention Principles"},
			    "ORE Capital Ship Invention Principles": {"max_level": 5, "description": "ORE Capital Ship Invention Principles"},
			    "CONCORD Capital Ship Invention Principles": {"max_level": 5, "description": "CONCORD Capital Ship Invention Principles"}
            },
            "Faction Technology": {
                "Angel Invention Principles": {"max_level": 5, "description": "Angel Invention Principles"},
			    "Blood Invention Principles": {"max_level": 5, "description": "Blood Invention Principles"},
			    "Guristas Invention Principles": {"max_level": 5, "description": "Guristas Invention Principles"},
			    "Serpentis Invention Principles": {"max_level": 5, "description": "Serpentis Invention Principles"},
			    "Sansha Invention Principles": {"max_level": 5, "description": "Sansha Invention Principles"},
			    "Angel Capital Ship Invention Principles": {"max_level": 5, "description": "Angel Capital Ship Invention Principles"},
			    "Blood Raider Capital Ship Invention Principles": {"max_level": 5, "description": "Blood Raider Capital Ship Invention Principles"},
			    "Guristas Capital Ship Invention Principles": {"max_level": 5, "description": "Guristas Capital Ship Invention Principles"},
			    "Serpentis Capital Ship Invention Principles": {"max_level": 5, "description": "Serpentis Capital Ship Invention Principles"}
            },
            "Corporation Technology": {
                "ORE Invention Principles": {"max_level": 5, "description": "ORE Invention Principles"},
			    "Mordu's Legion Invention Principles": {"max_level": 5, "description": "Mordu's Legion Invention Principles"},
			    "SOE Invention Principles": {"max_level": 5, "description": "SOE Invention Principles"},
			    "InterBus Invention Principles": {"max_level": 5, "description": "InterBus Invention Principles"},
			    "CONCORD Invention Principles": {"max_level": 5, "description": "CONCORD Invention Principles"}
            },
			"Module Invention": {
                "Module Invention Principles": {"max_level": 5, "description": "Module Invention Principles"},
			    "Capital Module Invention Principles": {"max_level": 5, "description": "Capital Module Invention Principles"},
			    "Implant Invention": {"max_level": 5, "description": "Implant Invention"},
			    "Module Invention Specialization": {"max_level": 5, "description": "Module Invention Specialization"},
			    "Capital Module Invention Specialization": {"max_level": 5, "description": "Capital Module Invention Specialization"},
			    "Implant Unit Invention Principles": {"max_level": 5, "description": "Implant Unit Invention Principles"}
            }
        },
        "Natural Science": {
            "Planet Management": {
                "Planetology": {"max_level": 5, "description": "Planetology"}
            },
            "Planet Exploration": {
                "Hacking": {"max_level": 5, "description": "Hacking"},
			    "Space Exploration Technology": {"max_level": 5, "description": "Space Exploration Technology"}
            },
            "Biology": {
                "Cognitive Neuroscience": {"max_level": 5, "description": "Cognitive Neuroscience"},
			    "Infomorph Synchronizing": {"max_level": 5, "description": "Infomorph Synchronizing"}
            }
        }
    }
}

def get_ship_categories():
    return list(SHIP_CATEGORIES.keys())

def get_ship_subcategories(category):
    return SHIP_CATEGORIES.get(category, [])

def get_skill_types():
    return list(SKILLS_DATA.keys())

def get_skill_categories(skill_type):
    return list(SKILLS_DATA.get(skill_type, {}).keys())

def get_skill_subcategories(skill_type, category):
    return list(SKILLS_DATA.get(skill_type, {}).get(category, {}).keys())
