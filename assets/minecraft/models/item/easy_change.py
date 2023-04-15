MainString = '''{
  "parent": "minecraft:item/generated",
  "overrides": [
    {
      "model": "minecraft:item/ARMOR_PARTS_quartz_trim",
      "predicate": {
        "trim_type": 0.1
      }
    },
    {
      "model": "pillow:item/ARMOR_PARTS_white_stained_glass_trim",
      "predicate": {
        "trim_type": 0.15
      }
    },
    {
      "model": "pillow:item/ARMOR_PARTS_coal_block_trim",
      "predicate": {
        "trim_type": 0.16
      }
    },
    {
      "model": "pillow:item/ARMOR_PARTS_gold_block_trim",
      "predicate": {
        "trim_type": 0.17
      }
    },
    {
      "model": "minecraft:item/ARMOR_PARTS_iron_trim",
      "predicate": {
        "trim_type": 0.2
      }
    },
    {
      "model": "minecraft:item/ARMOR_PARTS_netherite_trim",
      "predicate": {
        "trim_type": 0.3
      }
    },
    {
      "model": "minecraft:item/ARMOR_PARTS_redstone_trim",
      "predicate": {
        "trim_type": 0.4
      }
    },
    {
      "model": "minecraft:item/ARMOR_PARTS_copper_trim",
      "predicate": {
        "trim_type": 0.5
      }
    },
    {
      "model": "minecraft:item/ARMOR_PARTS_gold_trim",
      "predicate": {
        "trim_type": 0.6
      }
    },
    {
      "model": "minecraft:item/ARMOR_PARTS_emerald_trim",
      "predicate": {
        "trim_type": 0.7
      }
    },
    {
      "model": "minecraft:item/ARMOR_PARTS_diamond_trim",
      "predicate": {
        "trim_type": 0.8
      }
    },
    {
      "model": "minecraft:item/ARMOR_PARTS_lapis_trim",
      "predicate": {
        "trim_type": 0.9
      }
    },
    {
      "model": "minecraft:item/ARMOR_PARTS_amethyst_trim",
      "predicate": {
        "trim_type": 1.0
      }
    }
  ],
  "textures": {
    "layer0": "minecraft:item/ARMOR_PARTS"
  }
}
        '''

Armors = ["chainmail", "diamond", "golden", "iron", "leather", "netherite"]
Armor_Parts = ["boots", "chestplate", "helmet", "leggings"]

def change(A, B):
    if A == "leather":
       bef = '''"layer0": "minecraft:item/ARMOR_PARTS"'''
       aft = '''"layer0": "minecraft:item/ARMOR_PARTS",
    "layer1": "minecraft:item/ARMOR_PARTS_overlay"'''
       temp = MainString.replace(bef, aft, 1)
       ST = temp.replace("ARMOR", A, 100).replace("PARTS", B, 100)
    else:
       ST = MainString.replace("ARMOR", A, 100).replace("PARTS", B, 100)
    fs = open(f'{A}_{B}.json',"w")
    if A == "diamond":
      fs.write(ST.replace("diamond_trim", "diamond_darker_trim", 100))
      fs.close()
      return
    if A == "golden":
      fs.write(ST.replace("gold_trim", "gold_darker_trim", 100))
      fs.close()
      return
    if A == "iron":
      fs.write(ST.replace("iron_trim", "iron_darker_trim", 100))
      fs.close()
      return
    if A == "netherite":
      fs.write(ST.replace("netherite_trim", "netherite_darker_trim", 100))
      fs.close()
      return
    
    fs.write(ST)
    fs.close()
    
for A in Armors:
    for B in Armor_Parts:
       change(A, B)
        

A = "turtle"
B = "helmet"
change(A, B)
        