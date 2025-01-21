
from classes.frog_class import *
from classes.object_class import *

textures_dimensions = {
    "wooden_log": [200, 100, 18],
    "reverse_wooden_log": [200, 100, 18],
    "rabbit": [200, 100, 16],
    "bush": [100, 100, 1],
    "rock": [100, 100, 1],
    "tree": [400, 400, 1],
    "sword": [100, 180, 1]
}

def textures_loader(relative_texture_path, frames=1):
    textures_collection = []
    for frame in range(0, frames):
        if frames > 1:
            loaded_sprite = pygame.image.load(f"images/{relative_texture_path}/{str(frame)}.png")
        else:
            loaded_sprite = pygame.image.load(f"images/{relative_texture_path}.png")
        loaded_sprite = pygame.transform.scale(loaded_sprite, (100, 100))
        textures_collection.append(loaded_sprite)
    return textures_collection


class Level:
    def __init__(self, level_id: int) -> None:
        self.water_zones = []
        self.background = pygame.image.load(f"images/level_background/lvl_{level_id}_bg.png").convert_alpha()
        self.enemies_group = []
        self.physical_group = []
        self.ending_sword = None
        self.player = Frog(frog_skin)
        self.scrolled = 0
        self.scroll_speed = 0
        self.level = level_id
        self.spawn = [0, 0]
        self.next_scene = None

    def scroll(self, status: bool) -> None:
        max_scroll = 1000
        if self.level == 0:
            max_scroll= 4320
        if status and self.scrolled > -max_scroll:
            screen.blit(self.background, (0, self.scrolled))
            for enemy in self.enemies_group:
                enemy.rect.y -= self.scroll_speed
            for physical_object in self.physical_group:
                physical_object.rect.y -= self.scroll_speed
            for sword in self.ending_sword:
                sword.rect.y -= self.scroll_speed
            self.player.rect.y -= self.scroll_speed
            self.scrolled -= self.scroll_speed
        elif status and self.scrolled <= -max_scroll:
            screen.blit(self.background, (0, self.scrolled))
        else:
            screen.blit(self.background, (0, 0))
        pass

    def load_objects(self, level_map) -> None:
        self.scroll_speed = level_map["properties"]["scroll_speed"]
        self.spawn = level_map["checkpoints"]["spawn"]


        for item_type in level_map["enemies"].keys():
            for item in level_map["enemies"][item_type]:
                if item_type == "reverse_wooden_log":
                    item_type = "wooden_log"
                self.enemies_group.append(Object(item[0],
                                                 item[1],
                                                 textures_dimensions[item_type][0],
                                                 textures_dimensions[item_type][1],
                                                 textures_loader(f"enemies/{item_type}",
                                                                   textures_dimensions[item_type][2]),
                                                 item[2])
                                          )
        for item_type in level_map["obstacles"].keys():
            for item in level_map["obstacles"][item_type]:
                self.physical_group.append(Object(item[0],
                                                  item[1],
                                                  textures_dimensions[item_type][0],
                                                  textures_dimensions[item_type][1],
                                                  textures_loader(f"obstacles/{item_type}"),
                                                  0
                                                  ))

        win = level_map["checkpoints"]["win"]
        self.ending_sword = Object(win[0],
                                   win[1],
                                   textures_dimensions["sword"][0],
                                   textures_dimensions["sword"][1],
                                   textures_loader(f"win_sword"),
                                   0
                                   )



        pass

    def build(self):
        with open(f"levels/level{self.level}.json") as json_file:
            level_map = json.load(json_file)
        self.load_objects(level_map)
        if "water" in level_map.keys():
            if "full_line" in level_map["water"].keys():
                for line in level_map["water"]["full_line"]:
                    # x0, y0, x1, y1, speed
                    self.water_zones.append([0, line[0], 1920, line[1] + 100, line[2]])
            if "partial_line" in level_map["water"].keys():
                for line in level_map["water"]["partial_line"]:
                    # x0, y0, x1, y1, speed
                    self.water_zones.append([line[0], line[1], line[2], line[3] + 100, line[4]])
        if "story_scene_next" in level_map["properties"].keys():
            self.next_scene = level_map["properties"]["story_scene_next"]
        self.enemies_group = pygame.sprite.Group(self.enemies_group)
        self.physical_group = pygame.sprite.Group(self.physical_group)
        self.ending_sword = pygame.sprite.Group(self.ending_sword)

