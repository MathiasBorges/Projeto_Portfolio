import customtkinter as ctk
import os
import sys

# Garante que os outros módulos possam ser importados
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from forms import PortfolioForms
from personaliza import PortfolioPersonalizacao
from gerar_pdf import PortfolioPDFGenerator

# Configura o tema do customtkinter
ctk.set_appearance_mode("System")  # Ou "Dark", "Light"
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    """
    Classe principal da aplicação que gerencia a troca de telas.
    """
    def __init__(self):
        super().__init__()
        
        self.title("Criador de Portfólio Profissional")
        # Define um tamanho inicial para a janela
        self.geometry("700x500") 
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Estrutura para manter todas as telas
        self.frames = {}
        
        # Variável para armazenar os dados coletados e configurações de design
        self.portfolio_data = {}
        self.design_config = {"cor_principal": "#3498db", "cor_secundaria": "#ecf0f1"}

        # Adiciona todas as telas à estrutura de frames
        self._add_frames()
        
        # Mostra a tela inicial
        self.show_frame("WelcomeFrame")

    def _add_frames(self):
        """Inicializa e armazena todas as telas da aplicação."""
        
        # Tela de Boas-vindas
        self.frames["WelcomeFrame"] = WelcomeFrame(master=self, controller=self)
        self.frames["WelcomeFrame"].grid(row=0, column=0, sticky="nsew")

        # Tela de Formulário
        self.frames["FormsFrame"] = PortfolioForms(master=self, controller=self)
        self.frames["FormsFrame"].grid(row=0, column=0, sticky="nsew")

        # Tela de Personalização
        self.frames["PersonalizacaoFrame"] = PortfolioPersonalizacao(master=self, controller=self)
        self.frames["PersonalizacaoFrame"].grid(row=0, column=0, sticky="nsew")

        # Tela de Geração de PDF
        self.frames["PDFGeneratorFrame"] = PortfolioPDFGenerator(master=self, controller=self)
        self.frames["PDFGeneratorFrame"].grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        """Traz a tela solicitada para o topo."""
        frame = self.frames[page_name]
        frame.tkraise()
        # Atualiza o conteúdo da tela se necessário
        if page_name == "PDFGeneratorFrame":
            self.frames["PDFGeneratorFrame"].update_data()
        
    def set_portfolio_data(self, data):
        """Atualiza os dados do portfólio."""
        self.portfolio_data.update(data)
        
    def set_design_config(self, config):
        """Atualiza as configurações de design."""
        self.design_config.update(config)


class WelcomeFrame(ctk.CTkFrame):
    """
    Tela inicial de boas-vindas.
    """
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 4), weight=1) # Espaço vazio em cima e embaixo
        
        # Título principal (Baseado na imagem 1)
        title_text = "Crie seu Portfólio Profissional\nem Minutos"
        self.title_label = ctk.CTkLabel(
            self, 
            text=title_text, 
            font=ctk.CTkFont(size=30, weight="bold")
        )
        self.title_label.grid(row=1, column=0, padx=20, pady=(40, 20))

        # Descrição (Baseado na imagem 1)
        desc_text = "Preencha seus dados, personalize o design e gere um PDF pronto para impressionar recrutadores."
        self.desc_label = ctk.CTkLabel(
            self, 
            text=desc_text, 
            font=ctk.CTkFont(size=16),
            wraplength=500 # Quebra de linha para textos longos
        )
        self.desc_label.grid(row=2, column=0, padx=20, pady=(0, 40))

        # Botão para começar (Baseado na imagem 1)
        self.start_button = ctk.CTkButton(
            self, 
            text="Começar Agora", 
            command=lambda: controller.show_frame("FormsFrame"),
            height=40,
            width=200,
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.start_button.grid(row=3, column=0, padx=20, pady=(0, 40))


if __name__ == "__main__":
    # Garante que os arquivos de template existam para rodar sem erros
    if not os.path.exists("templates"):
        os.makedirs("templates")
        
    # Inicializa o aplicativo
    app = App()
    app.mainloop()