import constantes
from constantes import *


class Level:
    def __init__(self, level_id: int) -> None:
        self.background = pygame.image.load(f"images/lvl_{level_id}_bg.png").convert_alpha()
        self.enemies_group = []
        self.physical_group = []
        self.ending_sword = None
        self.player = Frog(frog_skin)
        self.scrolled = 0
        self.scroll_speed = 0
        self.level = level_id
        self.spawn = [0, 0]
        pass

    def scroll(self, status: bool) -> None:
        if status and self.scrolled > -1000:
            screen.blit(self.background, (0, self.scrolled))
            for enemy in self.enemies_group:
                enemy.rect.y -= self.scroll_speed
            for physical_object in self.physical_group:
                physical_object.rect.y -= self.scroll_speed
            for sword in self.ending_sword:
                sword.rect.y -= self.scroll_speed
            self.player.rect.y -= self.scroll_speed
            self.scrolled -= self.scroll_speed
        elif status and self.scrolled <= -1000:
            screen.blit(self.background, (0, self.scrolled))
        else:
            screen.blit(self.background, (0, 0))
        pass

    def load_objects(self) -> None:
        with open(f"levels/level{self.level}.json") as json_file:
            level_map = json.load(json_file)

            self.scroll_speed = level_map["properties"]["scroll_speed"]
            self.spawn = level_map["checkpoints"]["spawn"]


            for item_type in level_map["enemies"].keys():
                for item in level_map["enemies"][item_type]:
                    if item_type == "reverse_wooden_log":
                        item_type = "wooden_log"
                    self.enemies_group.append(Obstacle(item[0],
                                                       item[1],
                                                       textures_dimensions[item_type][0],
                                                       textures_dimensions[item_type][1],
                                                       textures_loader(f"enemies/{item_type}",
                                                                       textures_dimensions[item_type][2]),
                                                       item[2])
                    )
            for item_type in level_map["obstacles"].keys():
                for item in level_map["obstacles"][item_type]:
                    self.physical_group.append(Obstacle(item[0],
                                                        item[1],
                                                        textures_dimensions[item_type][0],
                                                        textures_dimensions[item_type][1],
                                                        textures_loader(f"obstacles/{item_type}"),
                                                        0
                    ))

            win = level_map["checkpoints"]["win"]
            self.ending_sword = Obstacle(win[0],
                                         win[1],
                                         textures_dimensions["sword"][0],
                                         textures_dimensions["sword"][1],
                                         textures_loader(f"win_sword"),
                                         0
            )



        pass

    def build(self):
        self.enemies_group = pygame.sprite.Group(self.enemies_group)
        self.physical_group = pygame.sprite.Group(self.physical_group)
        self.ending_sword = pygame.sprite.Group(self.ending_sword)