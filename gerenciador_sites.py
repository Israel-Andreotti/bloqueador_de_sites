import tkinter as tk
from tkinter import messagebox
import os

# Descobre o caminho do Windows automaticamente (ex: C:\Windows ou D:\Windows)
windir = os.environ.get('SystemRoot', 'C:\\Windows')
hosts_path = os.path.join(windir, 'System32', 'drivers', 'etc', 'hosts')

redirect_ip = "127.0.0.1"
# Lista expandida para garantir que o bloqueio funcione em várias versões da URL
blocked_sites = ["www.youtube.com", "youtube.com", "m.youtube.com"]

def bloquear():
    try:
        with open(hosts_path, 'r+') as file:
            content = file.read()
            file.seek(0, 2) # Vai para o final do arquivo
            
            adicionado = False
            for site in blocked_sites:
                if site not in content:
                    file.write(f"\n{redirect_ip} {site}")
                    adicionado = True
            
        os.system("ipconfig /flushdns")
        if adicionado:
            messagebox.showinfo("Sucesso", "Sites Bloqueados! Lembre-se de reiniciar o navegador.")
        else:
            messagebox.showinfo("Aviso", "Os sites já estão na lista de bloqueio.")
    except PermissionError:
        messagebox.showerror("Erro", "Direito de Administrador negado!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao acessar arquivo: {e}")

def desbloquear():
    try:
        with open(hosts_path, 'r') as file:
            lines = file.readlines()
        
        with open(hosts_path, 'w') as file:
            for line in lines:
                # Mantém a linha apenas se nenhum site bloqueado estiver nela
                if not any(site in line for site in blocked_sites):
                    file.write(line)
        
        os.system("ipconfig /flushdns")
        messagebox.showinfo("Sucesso", "Sites Desbloqueados!")
    except PermissionError:
        messagebox.showerror("Erro", "Direito de Administrador negado!")

# Interface Gráfica
root = tk.Tk()
root.title("Foco Total - Bloqueador")
root.geometry("350x220")
root.resizable(False, False)

tk.Label(root, text="Gerenciador de Acesso", font=("Arial", 14, "bold")).pack(pady=15)
tk.Label(root, text="Bloqueia o YouTube para aumentar o foco.", font=("Arial", 9)).pack()

tk.Button(root, text="ATIVAR BLOQUEIO", bg="#d9534f", fg="white", font=("Arial", 10, "bold"),
          width=25, height=2, command=bloquear).pack(pady=10)

tk.Button(root, text="DESATIVAR BLOQUEIO", bg="#5cb85c", fg="white", font=("Arial", 10, "bold"),
          width=25, height=2, command=desbloquear).pack()

root.mainloop()