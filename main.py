import os
import pygame
import time
import keyboard

def header() -> None:     
    print("─" * 84)
    print(r"""     _     ____    __  __              _         ____   _                           
    / \   / ___|  |  \/  | _   _  ___ (_)  ___  |  _ \ | |  __ _  _   _   ___  _ __ 
   / _ \  \___ \  | |\/| || | | |/ __|| | / __| | |_) || | / _` || | | | / _ \| '__|
  / ___ \  ___) | | |  | || |_| |\__ \| || (__  |  __/ | || (_| || |_| ||  __/| |   
 /_/   \_\|____/  |_|  |_| \__,_||___/|_| \___| |_|    |_| \__,_| \__, | \___||_|   
                                                                  |___/""")
    print("─" * 84)
    print("  Author       :  angslhn")
    print("  Repository   :  https://github.com/angslhn/AS-Music-Player")
    print("─" * 84)

def find_songs(path: str) -> list[str] :    
    return [song for song in os.listdir(path) if song.endswith(".mp3")]

def selection_sort(songs: list[str]) -> list[str]:
    n = len(songs)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if songs[j].lower() < songs[min_index].lower():
                min_index = j
                
        songs[min_index], songs[i] = songs[i], songs[min_index]
        
    return songs

def list_songs(songs: list[str]) -> None:
    print("  Daftar Lagu Tersedia")
    for no, song in enumerate(songs, start = 1):
        print(f"   {no}. {song[0:-4]}")
    
def play_songs(selected: int, path: str, stack_songs: list[str]):
    print("  [INFO] Tekan ESC jika anda ingin menghentikan pemutaran.")
    
    pygame.mixer.init()
    
    index = selected - 1
    
    while index < len(stack_songs):
        song = stack_songs[index]
        song_path = os.path.join(path, song)
        
        print(f"\n  ~ Memutar -> {song[0:-4]}")
        
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
            
        while pygame.mixer.music.get_busy():
            if keyboard.is_pressed("esc"):
                pygame.mixer.music.stop()
                print("\n  ~ Pemutaran lagu dihentikan.")
                return
            
            time.sleep(0.1)
            
        index += 1
    
    print("  Semua lagu telah selesai diputar.")

def main():
    songs_path = "./Songs"
    
    if not os.path.exists(songs_path):
        os.mkdir(songs_path)
    
    songs = find_songs(songs_path)
    
    if not songs:
        print("  Lagu tidak ditemukan didalam folder.")
        return

    stack_songs = [song for song in selection_sort(songs)]
    
    list_songs(stack_songs)
    
    print("─" * 84)
    
    try:
        selected = int(input("  Pilih lagu = "))
        
        if selected < 1 or selected > len(stack_songs):
            print("  Lagu yang anda pilih tidak ditemukan.")
            return
    except ValueError:
        print("  Masukan untuk pilihan lagu harus angka sesuai daftar lagu.")
        return
    
    print("─" * 84)
    
    play_songs(selected, songs_path, stack_songs)
    
    print("─" * 84)
    

if __name__ == "__main__":
    header()
    main()