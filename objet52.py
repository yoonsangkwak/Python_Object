from abc import ABC, abstractmethod

class MusicPlayer(ABC):
    @abstractmethod
    def play(self) -> str:
        return "노래 가사를 리턴합니다"


class RnBPlayer(MusicPlayer):
    def play(self):
        return "미안해 미안해하지마..."


class RockPlayer(MusicPlayer):
    def play(self):
        return "말 달리자~!..."


class RapPlayer(MusicPlayer):
    def play(self):
        return -1


music_player = RnBPlayer()
print(music_player.play())

music_player = RockPlayer()
print(music_player.play())

music_player = RapPlayer()
print(music_player.play())