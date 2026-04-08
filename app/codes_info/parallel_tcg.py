from enum import Enum

class regions(Enum):
    marcolian = "marcolian"
    shroud = "shroud"
    kathari = "kathari"
    augencore = "augencore"
    earthen = "earthen"

parallel = {
    # kathari
    "CB-371": ("Gnaeus Valerus Alpha", regions.kathari),
    "CB-373": ("Scipius Magnus Alpha", regions.kathari),
    "CB-375": ("Aetio, Exalted Hydrolist", regions.kathari),
    # augencore
    "CB-9": ("Jahn, Chief Engineer", regions.augencore),
    "CB-376": ("Juggernaut Workshop", regions.augencore),
    "CB-21": ("Arak, Combat Overseer", regions.augencore),
    # earthen
    "CB-62": ("Gaffar, Arbiter of Earth", regions.earthen),
    "CB-389": ("Shoshanna, Rebuilder of Earth", regions.earthen),
    "CB-390": ("Nehemiah, Defender of Earth", regions.earthen),
    # marcolian
    "CB-171": ("Lemieux, Master Commando", regions.marcolian),
    "CB-197": ("Catherine Lapointe, The Mad General", regions.marcolian),
    "CB-277": ("Armored Division HQ", regions.marcolian),
    # shroud
    "CB-379": ("Niamh, Wielder of Faith", regions.shroud),
    "CB-380": ("The New Dawn", regions.shroud),
    "CB-378": ("Brand, Steward Eternal", regions.shroud),
}

def code_info(code: str) -> dict[str,str] | None:
    # example code:
    # CB-379,CB-240,3xCB-204,....
    id_parallel = code.split(",")[0]
    parallel_info = parallel.get(id_parallel, None)
    if parallel_info is None:
        return None
    
    parallel_name, parallel_region = parallel_info
    return {"paragon": parallel_name, "region": parallel_region.value}

if  __name__ == "__main__":
    result = code_info("CB-379,CB-240,3xCB-204")
    print(result)
    #> Niamh, Wielder of Faith