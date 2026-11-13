from tkinter import filedialog
import shutil

arquivo  = filedialog.askopenfilename()
destino = "C:/Users/User/Desktop/trabalho administracao/cartas_Antecipamento"

arquivo_copiado = shutil.copy(arquivo , destino)