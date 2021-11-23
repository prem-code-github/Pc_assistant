import ctypes

SPI_WALLPAPER=0x14
SPIF_UPDATINGFILE =0x2

source=r"C:\Users\user\Downloads\black.jpg"

ctypes.windll.user32.SystemParametersInfoW(SPI_WALLPAPER,0,source,SPIF_UPDATINGFILE)