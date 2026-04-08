from enum import Enum

class regions(Enum):
    marcolian = "marcolian"
    shroud = "shroud"
    kathari = "kathari"
    augencore = "augencore"
    earthen = "earthen"

parallel = {
    # kathari
    "CB-371": "Gnaeus Valerus Alpha",
    "CB-373": "Scipius Magnus Alpha",
    "CB-375": "Aetio, Exalted Hydrolist",
    # augencore
    "CB-9": "Jahn, Chief Engineer",
    "CB-376": "Juggernaut Workshop",
    "CB-21": "Arak, Combat Overseer",
    # earthen
    "CB-62": "Gaffar, Arbiter of Earth",
    "CB-389": "Shoshanna, Rebuilder of Earth",
    "CB-390": "Nehemiah, Defender of Earth",
    # marcolian
    "CB-171": "Lemieux, Master Commando",
    "CB-197": "Catherine Lapointe, The Mad General",
    "CB-277": "Armored Division HQ",
    # shroud
    "CB-379": "Niamh, Wielder of Faith",
    "CB-380":"The New Dawn",
    "CB-378": "Brand, Steward Eternal",
}

def code_info(code: str):
    # example code:
    # CB-379,CB-240,3xCB-204,....
    id_parallel = code.split(",")[0]
    parallel_name = parallel.get(id_parallel, None)
    return parallel_name

if  __name__ == "__main__":
    result = code_info("CB-379,CB-240,3xCB-204")
    print(result)
    #> Niamh, Wielder of Faith