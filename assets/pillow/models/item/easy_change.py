MainString = '''{
  "parent": "minecraft:item/generated",
  "textures": {
    "layer0": "minecraft:item/ARMOR_PARTS",
    "layer1": "minecraft:trims/items/PARTS_trim_MATERIAL"
  }
}'''

Armors = ["chainmail", "diamond", "golden", "iron", "leather", "netherite"]
Armor_Parts = ["boots", "chestplate", "helmet", "leggings"]
Materials = ["white_stained_glass", "coal_block", "gold_block"]


def change(A, B, C):
    if A == "leather":
        MS = '''{
  "parent": "minecraft:item/generated",
  "textures": {
    "layer0": "minecraft:item/ARMOR_PARTS",
    "layer1": "minecraft:item/ARMOR_PARTS_overlay",
    "layer2": "minecraft:trims/items/PARTS_trim_MATERIAL"
  }
}'''
    else : MS = MainString
    fs = open(f'{A}_{B}_{C}_trim.json',"w")
    fs.write(MS.replace("ARMOR", A, 100).replace("PARTS", B, 100).replace("MATERIAL", C, 100))
    fs.close()
    
for A in Armors:
    for B in Armor_Parts:
        for C in Materials:
            change(A, B, C)

A = "turtle"
B = "helmet"
for C in Materials:
  change(A, B, C)
        

