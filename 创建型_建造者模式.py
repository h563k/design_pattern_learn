from abc import ABCMeta, abstractmethod


class Player:
    def __init__(self, face, body, arm, leg):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return f"{self.face},{self.body},{self.arm},{self.leg}"


# 抽象建造者
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.player = Player('', '', '', '')

    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


# 具体建造者
class SexyGirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player('', '', '', '')

    def build_face(self):
        self.player.face = '刘亦菲的脸'

    def build_body(self):
        self.player.body = '魔鬼身材'

    def build_arm(self):
        self.player.arm = '漂亮胳膊'

    def build_leg(self):
        self.player.leg = '大长腿'


class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player('', '', '', '')

    def build_face(self):
        self.player.face = '哥斯拉的脸'

    def build_body(self):
        self.player.face = '大脚怪'

    def build_arm(self):
        self.player.face = '八爪鱼'

    def build_leg(self):
        self.player.leg = '八爪鱼的脚'


# 指挥者
class PlayrtDirector:
    def build_player(self, builder: PlayerBuilder):
        # 这里可以进行复杂的构造
        builder.build_face()
        builder.build_body()
        builder.build_arm()
        builder.build_leg()
        return builder.player


"""
将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示

"""
builder = SexyGirlBuilder()
director = PlayrtDirector()
p = director.build_player(builder)
print(p)
