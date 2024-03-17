## ==============================================
## ========== Matrículas Portuguesas ============
## ==============================================
## ===== Script Python para Obter Diversas ======
## == Informações sobre Matrículas Portuguesas ==
## ==============================================

## Autor: José Rodrigues | https://github.com/joserodpt

class PortugueseLicensePlate2020:
    def __init__(self, plate="AA-00-AA"):
        self.allowed_letters = "ABCDEFGHIJLMNOPQRSTUVXZ"
        self.plate = plate.upper()
        if not self._validate_plate():
            raise ValueError("Invalid plate format")

    def _validate_plate(self):
        import re
        # Check if the plate matches the pattern and only contains allowed letters
        pattern = r"^[A-Z]{2}-\d{2}-[A-Z]{2}$"
        return bool(re.match(pattern, self.plate)) and all(c in self.allowed_letters for c in self.plate if c.isalpha())

    def _increment_letters(self, letters):
        max_index = len(self.allowed_letters) - 1

        first, second = letters
        second_index = self.allowed_letters.index(second)

        if second_index < max_index:
            second = self.allowed_letters[second_index + 1]
        else:
            first_index = self.allowed_letters.index(first)
            if first_index < max_index:
                first = self.allowed_letters[first_index + 1]
            else:
                # Reset to the start if both reach the end
                first = self.allowed_letters[0]
            second = self.allowed_letters[0]

        return first + second

    def increment_plate(self):
        parts = self.plate.split("-")
        number = int(parts[1])
        if number < 99:
            number += 1
            parts[1] = f"{number:02d}"
        else:
            parts[1] = "00"
            parts[2] = self._increment_letters(parts[2])
            if parts[2] == "AA":  # Rolled over the last part, increment the first part
                parts[0] = self._increment_letters(parts[0])

        self.plate = "-".join(parts)

    def get_plate(self):
        return self.plate

    def get_plate_without_sep(self):
        return self.plate.replace("-", "")


municipios = {
    "ABT": "Abrantes",
    "AGD": "Águeda",
    "AGB": "Aguiar da Beira",
    "ADL": "Alandroal",
    "ABL": "Albergaria-a-Velha",
    "ABF": "Albufeira",
    "ASL": "Alcácer do Sal",
    "ACN": "Alcanena",
    "ACB": "Alcobaça",
    "ACH": "Alcochete",
    "ACT": "Alcoutim",
    "ALQ": "Alenquer",
    "AFE": "Alfândega da Fé",
    "ALJ": "Alijó",
    "AJZ": "Aljezur",
    "AJT": "Aljustrel",
    "ALM": "Almada",
    "ALD": "Almeida",
    "ALR": "Almeirim",
    "ADV": "Almodôvar",
    "APC": "Alpiarça",
    "ALT": "Alter do Chão",
    "AVZ": "Alvaiázere",
    "AVT": "Alvito",
    "AMD": "Amadora",
    "AMT": "Amarante",
    "AMR": "Amares",
    "AND": "Anadia",
    "AGH": "Angra do Heroísmo",
    "ANS": "Ansião",
    "AVV": "Arcos de Valdevez",
    "AGN": "Arganil",
    "AMM": "Armamar",
    "ARC": "Arouca",
    "ARL": "Arraiolos",
    "ARR": "Arronches",
    "ARV": "Arruda dos Vinhos",
    "AVR": "Aveiro",
    "AVS": "Avis",
    "AZB": "Azambuja",
    "BAO": "Baião",
    "BCL": "Barcelos",
    "BRC": "Barrancos",
    "BRR": "Barreiro",
    "BTL": "Batalha",
    "BJA": "Beja",
    "BMT": "Belmonte",
    "BNV": "Benavente",
    "BBR": "Bombarral",
    "BRB": "Borba",
    "BTC": "Boticas",
    "BRG": "Braga",
    "BGC": "Bragança",
    "CBC": "Cabeceiras de Basto",
    "CDV": "Cadaval",
    "CLD": "Caldas da Rainha",
    "CHT": "Calheta (Angra do Heroísmo)",
    "CLT": "Calheta (Funchal)",
    "CML": "Câmara de Lobos",
    "CMN": "Caminha",
    "CMR": "Campo Maior",
    "CNT": "Cantanhede",
    "CRZ": "Carrazeda de Ansiães",
    "CRS": "Carregal do Sal",
    "CTX": "Cartaxo",
    "CSC": "Cascais",
    "CPR": "Castanheira de Pêra",
    "CTB": "Castelo Branco",
    "CPV": "Castelo de Paiva",
    "CVD": "Castelo de Vide",
    "CDR": "Castro Daire",
    "CTM": "Castro Marim",
    "CVR": "Castro Verde",
    "CLB": "Celorico da Beira",
    "CBT": "Celorico de Basto",
    "CHM": "Chamusca",
    "CHV": "Chaves",
    "CNF": "Cinfães",
    "CBR": "Coimbra",
    "CDN": "Condeixa-a-Nova",
    "CTC": "Constância",
    "CCH": "Coruche",
    "CRV": "Corvo",
    "CVL": "Covilhã",
    "CRT": "Crato",
    "CUB": "Cuba",
    "ELV": "Elvas",
    "ENT": "Entroncamento",
    "ESP": "Espinho",
    "EPS": "Esposende",
    "ETR": "Estarreja",
    "ETZ": "Estremoz",
    "EVR": "Évora",
    "FAF": "Fafe",
    "FAR": "Faro",
    "FLG": "Felgueiras",
    "FAL": "Ferreira do Alentejo",
    "FZZ": "Ferreira do Zêzere",
    "FIG": "Figueira da Foz",
    "FCR": "Figueira de Castelo Rodrigo",
    "FVN": "Figueiró dos Vinhos",
    "FAG": "Fornos de Algodres",
    "FEC": "Freixo de Espada à Cinta",
    "FTR": "Fronteira",
    "FUN": "Funchal",
    "FND": "Fundão",
    "GAV": "Gavião",
    "GOI": "Góis",
    "GLG": "Golegã",
    "GDM": "Gondomar",
    "GVA": "Gouveia",
    "GDL": "Grândola",
    "GRD": "Guarda",
    "GMR": "Guimarães",
    "HRT": "Horta",
    "IDN": "Idanha-a-Nova",
    "ILH": "Ílhavo",
    "LGA": "Lagoa",
    "LAG": "Lagoa (Ponta Delgada)",
    "LGS": "Lagos",
    "LJF": "Lajes das Flores",
    "LJP": "Lajes do Pico",
    "LMG": "Lamego",
    "LRA": "Leiria",
    "LSB": "Lisboa",
    "LLE": "Loulé",
    "LRS": "Loures",
    "LNH": "Lourinhã",
    "LSA": "Lousã",
    "LSD": "Lousada",
    "MAC": "Mação",
    "MDC": "Macedo de Cavaleiros",
    "MCH": "Machico",
    "MAD": "Madalena",
    "MFR": "Mafra",
    "MAI": "Maia",
    "MGL": "Mangualde",
    "MTG": "Manteigas",
    "MCN": "Marco de Canaveses",
    "MGR": "Marinha Grande",
    "MRV": "Marvão",
    "MTS": "Matosinhos",
    "MLD": "Mealhada",
    "MDA": "Meda",
    "MLG": "Melgaço",
    "MTL": "Mértola",
    "MSF": "Mesão Frio",
    "MIR": "Mira",
    "MCV": "Miranda do Corvo",
    "MDR": "Miranda do Douro",
    "MDL": "Mirandela",
    "MGD": "Mogadouro",
    "MBR": "Moimenta da Beira",
    "MTA": "Moita",
    "MNC": "Monção",
    "MCQ": "Monchique",
    "MDB": "Mondim de Basto",
    "MFT": "Monforte",
    "MTR": "Montalegre",
    "MMN": "Montemor-o-Novo",
    "MMV": "Montemor-o-Velho",
    "MTJ": "Montijo",
    "MOR": "Mora",
    "MRT": "Mortágua",
    "MRA": "Moura",
    "MOU": "Mourão",
    "MUR": "Murça",
    "MRS": "Murtosa",
    "NZR": "Nazaré",
    "NLS": "Nelas",
    "NIS": "Nisa",
    "NRD": "Nordeste",
    "OBD": "Óbidos",
    "ODM": "Odemira",
    "ODV": "Odivelas",
    "OER": "Oeiras",
    "OLR": "Oleiros",
    "OLH": "Olhão",
    "OAZ": "Oliveira de Azeméis",
    "OFR": "Oliveira de Frades",
    "OBR": "Oliveira do Bairro",
    "OHP": "Oliveira do Hospital",
    "VNO": "Ourém",
    "ORQ": "Ourique",
    "OVR": "Ovar",
    "PFR": "Paços de Ferreira",
    "PLM": "Palmela",
    "PPS": "Pampilhosa da Serra",
    "PRD": "Paredes",
    "PCR": "Paredes de Coura",
    "PGR": "Pedrógão Grande",
    "PCV": "Penacova",
    "PNF": "Penafiel",
    "PCT": "Penalva do Castelo",
    "PNC": "Penamacor",
    "PND": "Penedono",
    "PNL": "Penela",
    "PNI": "Peniche",
    "PRG": "Peso da Régua",
    "PNH": "Pinhel",
    "PBL": "Pombal",
    "PDL": "Ponta Delgada",
    "PTS": "Ponta do Sol",
    "PTB": "Ponte da Barca",
    "PTL": "Ponte de Lima",
    "PSR": "Ponte de Sor",
    "PTG": "Portalegre",
    "PRL": "Portel",
    "PTM": "Portimão",
    "PRT": "Porto",
    "PMS": "Porto de Mós",
    "PMZ": "Porto Moniz",
    "PST": "Porto Santo",
    "PVL": "Póvoa de Lanhoso",
    "PVZ": "Póvoa de Varzim",
    "PVC": "Povoação",
    "PNV": "Proença-a-Nova",
    "RDD": "Redondo",
    "RMZ": "Reguengos de Monsaraz",
    "RSD": "Resende",
    "RBR": "Ribeira Brava",
    "RPN": "Ribeira de Pena",
    "RGR": "Ribeira Grande",
    "RMR": "Rio Maior",
    "SBR": "Sabrosa",
    "SBG": "Sabugal",
    "SMG": "Salvaterra de Magos",
    "SCD": "Santa Comba Dão",
    "SCR": "Santa Cruz",
    "SCG": "Santa Cruz da Graciosa",
    "SCF": "Santa Cruz das Flores",
    "VFR": "Santa Maria da Feira",
    "SMP": "Santa Marta de Penaguião",
    "STN": "Santana",
    "STR": "Santarém",
    "STC": "Santiago do Cacém",
    "STS": "Santo Tirso",
    "SBA": "São Brás de Alportel",
    "SJM": "São João da Madeira",
    "SJP": "São João da Pesqueira",
    "SPS": "São Pedro do Sul",
    "SRP": "São Roque do Pico",
    "SVC": "São Vicente",
    "SRD": "Sardoal",
    "SAT": "Sátão",
    "SEI": "Seia",
    "SXL": "Seixal",
    "SRN": "Sernancelhe",
    "SRT": "Sertã",
    "SSB": "Sesimbra",
    "STB": "Setúbal",
    "SVV": "Sever do Vouga",
    "SLV": "Silves",
    "SNS": "Sines",
    "SNT": "Sintra",
    "SMA": "Sobral de Monte Agraço",
    "SRE": "Soure",
    "SSL": "Sousel",
    "TBU": "Tábua",
    "TBC": "Tabuaço",
    "TRC": "Tarouca",
    "TVR": "Tavira",
    "TBR": "Terras de Bouro",
    "TMR": "Tomar",
    "TND": "Tondela",
    "TMC": "Torre de Moncorvo",
    "TNV": "Torres Novas",
    "TVD": "Torres Vedras",
    "TCS": "Trancoso",
    "TRF": "Trofa",
    "VGS": "Vagos",
    "VLC": "Vale de Cambra",
    "VLN": "Valença",
    "VLG": "Valongo",
    "VLP": "Valpaços",
    "VLS": "Velas",
    "VND": "Vendas Novas",
    "VNT": "Viana do Alentejo",
    "VCT": "Viana do Castelo",
    "VDG": "Vidigueira",
    "VRM": "Vieira do Minho",
    "VPV": "Vila da Praia da Vitória",
    "VLR": "Vila de Rei",
    "VBP": "Vila do Bispo",
    "VCD": "Vila do Conde",
    "VPT": "Vila do Porto",
    "VFL": "Vila Flor",
    "VFX": "Vila Franca de Xira",
    "VFC": "Vila Franca do Campo",
    "VNB": "Vila Nova da Barquinha",
    "VNC": "Vila Nova de Cerveira",
    "VNF": "Vila Nova de Famalicão",
    "VLF": "Vila Nova de Foz Côa",
    "VNG": "Vila Nova de Gaia",
    "VNP": "Vila Nova de Paiva",
    "PRS": "Vila Nova de Poiares",
    "VPA": "Vila Pouca de Aguiar",
    "VRL": "Vila Real",
    "VRS": "Vila Real de Santo António",
    "VVR": "Vila Velha de Ródão",
    "VVD": "Vila Verde",
    "VVC": "Vila Viçosa",
    "VMS": "Vimioso",
    "VNH": "Vinhais",
    "VIS": "Viseu",
    "VIZ": "Vizela",
    "VZL": "Vouzela",
}


def get_municipio(digitos_identificadores):
    return municipios.get(digitos_identificadores)


codigos_regioes = {
    'A': 'Açores (Ponta Delgada)',
    'AN': 'Angra do Heroísmo',
    'AV': 'Aveiro',
    'BE': 'Beja',
    'BG': 'Bragança',
    'BR': 'Braga',
    'C': 'Coimbra',
    'CB': 'Castelo Branco',
    'D': 'Corpo Diplomático',
    'E': 'Évora',
    'F': 'Pessoal da Embaixada Diplomática',
    'FA': 'Faro',
    'GD': 'Guarda',
    'H': 'Horta (Açores)',
    'L': 'Lisboa',
    'LE': 'Leiria',
    'M': 'Madeira (Funchal)',
    'P': 'Porto',
    'PT': 'Portalegre',
    'SA': 'Santarém',
    'SE': 'Setúbal',
    'VC': 'Viana do Castelo',
    'VI': 'Viseu',
    'VR': 'Vila Real'
}

funcoes_gnr = {
    'B': 'Blindado',
    'C': 'Pesado de Transportes',
    'E': 'Função Especial',
    'F': 'Brigada Fiscal',
    'G': 'Ligeiro de Transportes',
    'J': 'Todo-o-Terreno',
    'L': 'Ligeiro de Passageiros',
    'M': 'Motociclo',
    'P': 'Pesado de Passageiros',
    'T': 'Brigada de Trânsito',
    'V': 'Ciclomotor'
}


def encontrar_regiao_reboque(codigo):
    codigo = codigo.upper()  # Convert to uppercase for case-insensitive comparison

    if codigo in codigos_regioes:
        return codigos_regioes[codigo]
    else:
        return "-"


def range_reboque_lisboa(numero_reboque_lisboa):
    if numero_reboque_lisboa >= 25000 and numero_reboque_lisboa < 50000:
        return "Entre Inícios de 1973 e Verão de 1979"
    elif numero_reboque_lisboa >= 50000 and numero_reboque_lisboa < 100000:
        return "Entre Verão de 1979 e Inícios de 1990"
    elif numero_reboque_lisboa >= 100000 and numero_reboque_lisboa < 150000:
        return "Entre Inícios de 1990 e Março de 2000"
    elif numero_reboque_lisboa >= 150000 and numero_reboque_lisboa < 200000:
        return "Entre Março de 2000 e Inícios de 2016"
    elif numero_reboque_lisboa >= 200000:
        return "Para Lá de Inícios de 2016"
    else:
        return "Impossível Determinar Data de Registo"


def encontrar_funcao_GNR(funcao):
    if funcao in funcoes_gnr:
        return funcoes_gnr[funcao]
    else:
        return "Função Desconhecida."


def info_matricula_gnr(matricula):
    if matricula.startswith("GNR") and matricula[4] == "-":
        return 'Informações de Matrícula GNR\n>>> ' + matricula + '\n' + \
            '\n> Função do Carro: ' + encontrar_funcao_GNR(matricula[3])
    else:
        return 'Matrícula da GNR Inválida.'


def info_matricula_reboque(matricula):
    if len(matricula) == 7 and matricula[0] == 'E' and matricula[1] == '-':
        return 'Informações da Matrícula Reboque\n>>> ' + matricula + '\n' + \
            '\n> Tipo Reboque: Reboque Militar [Força Aérea]'

    if len(matricula) == 8 and matricula[0] == 'A' and matricula[1] == 'P':
        return 'Informações da Matrícula Reboque\n>>> ' + matricula + '\n' + \
            '\n> Tipo Reboque: Reboque Militar [Marinha]'

    try:
        regiao, numero = matricula.split('-')
    except Exception:
        return 'Formato de Matricula Inválido.'

    if numero == 'M':
        return 'Informações da Matrícula Reboque\n>>> ' + matricula + '\n' + \
            '\n> Tipo Reboque: Reboque Militar [Exército]' + \
            '\n> Número: ' + str(regiao)

    try:
        numero = int(numero)
    except Exception:
        return 'Número da Matrícula Inválido.'

    if not isinstance(numero, int):
        return 'Número da Matrícula Inválido.'

    if len(regiao) >= 3 and len(regiao) <= 1:
        return 'Região da Matrícula Inválida'
    else:
        replyRegiao = encontrar_regiao_reboque(regiao)
        if replyRegiao == '-':
            return 'Região ' + regiao + ' inválida.'
        else:
            out = 'Informações da Matrícula Reboque\n>>> ' + matricula + '\n' + \
                  '\n> Tipo Reboque: Reboque Civil' + \
                  '\n> Número: ' + str(numero) + \
                  '\n> Região: ' + replyRegiao + ' [Código: ' + regiao + ']\n'

            if regiao.lower() == 'l':
                out = out + '\nInformação Adicional para Matrículas Reboque de Lisboa:\n> Data de Registo: ' + range_reboque_lisboa(
                    numero)

            return out


def validar_matricula_pre1937(matricula):
    return matricula[0].lower() in ['n', 'c', 's', 'a', 'm'] and matricula[1] == '-' and len(matricula) > 2


def press_enter_to_continue():
    input("\nPressiona Enter para Continuar...")


def verificar_matricula_veiculos():
    matricula = input('Inserir Matrícula:\n> ')

    # detetar matrículas de 1911
    if matricula[1] == '-':
        # matrícula de 1911
        print("Matrícula de Série X-000 (1911-1937)")  # TODO: conversão para 1937
        if matricula[0] == 'N':
            print('Região da Matrícula: Norte')
        elif matricula[0] == 'C':
            print('Região da Matrícula: Centro')
        elif matricula[0] == 'S':
            print('Região da Matrícula: Sul')
        elif matricula[0] == 'A':
            print('Região da Matrícula: Açores')
        elif matricula[0] == 'M':
            print('Região da Matrícula: Madeira')
        else:
            print('Região da Matrícula: Não Identificada')

        if matricula[-2] == '-' and matricula[-1] == 'A':
            print('Dados Adicionais:\n> Matrícula de Carro de Aluguer')
        if matricula[-3] == '-' and matricula[-2] == 'W' and matricula[-1] == 'W':
            print('Dados Adicionais:\n> Matrícula Provisória')

    elif matricula[2] == '-':
        # matrículas no formato
        # XX-XX-XX
        # 01234567

        if matricula[0:2].isalpha() and matricula[6:7].isalpha():
            print("Matrícula de Série XX-00-XX (2020-)")
        elif matricula[0:2].isalpha() and not matricula[6:7].isalpha():
            print("Matrícula de Série XX-00-00 (1937-1991)")
        elif not matricula[0:2].isalpha() and matricula[6:7].isalpha():
            print("Matrícula de Série 00-00-XX (1992-2005)")
        elif matricula[3:4].isalpha():
            print("Matrícula de Série 00-XX-00 (2005-2020)")

    else:
        print('Formato de Matrícula Não Reconhecido.')

    press_enter_to_continue()


def verificar_matricula_reboques():
    matricula = input('Inserir Matrícula-Reboque:\n> ')
    print(info_matricula_reboque(matricula))
    press_enter_to_continue()


def verificar_matricula_carros_gnr():
    matricula = input('Inserir Matrícula Veículo GNR (ex: GNRL-1234)\n> ')

    print(info_matricula_gnr(matricula))

    press_enter_to_continue()


def verificar_matricula_motas_ate_2006():
    matric = input('Inserir Matrícula Motas Até 2006 (ex: 2-OER-20-75):\n> ')

    print('Informações da Matrícula de Mota Até 2006\n>>> ' + matric + '\n' + \
          '\n> Município de Registo: ' + get_municipio(matric.split("-")[1]))

    press_enter_to_continue()


def verificar_matricula_veiculos_exportacao():
    matric = input('Inserir Matrícula de Veículos de Exportação (ex: 123456-L):\n> ')
    letra = matric.split("-")[1]

    porto = "Porto de Exportação: "

    if letra == "L":
        porto = porto + "Lisboa"
    elif letra == "P":
        porto = porto + "Porto"
    elif letra == "A":
        porto = porto + "Açores"
    elif letra == "M":
        porto = porto + "Madeira"
    else:
        porto = porto + "Não Identificado"

    print('Informações da Matrícula de Exportação\n>>> ' + matric + '\n' + \
          '\n> ' + porto)

    press_enter_to_continue()


def numbers_to_letters(s):
    # Define the mapping from numbers to letters
    mapping = {
        '0': 'O',  # Example mapping
        '1': 'I',  # Adjust based on your needs
        '2': 'Z',  # This is just an example; replace with correct mappings
        '3': 'E',
        '4': 'A',  # Adjust based on your needs
        '5': 'S',
        '6': 'G',  # Adjust based on your needs
        '7': 'T',  # This is just an example; replace with correct mappings
        '8': 'B',
        '9': 'P'  # Adjust based on your needs
    }

    # Convert the string
    converted_string = "".join(mapping.get(char, char) for char in s)

    return converted_string



def combinacoesMatriculas6Letras():
    plate_generator = PortugueseLicensePlate2020("AA-00-AA")

    conteudo = []

    with open("palavras6letrasUNICAS.txt", 'r') as file:
        conteudo = file.read().splitlines()
        conteudo = [element.lower() for element in conteudo]

        # print(numbers_to_letters("AZ31TE"))

        # letras: 23
        # todas: 27 984 100
        # apenas serie A: 1 216 700

        with open("matriculas6LetrasOut.txt", 'a') as escrita:

            for i in range(0, 27984100):
                # print(plate_generator.get_plate_without_sep())  # Initial plate
                stringPlaca = numbers_to_letters(plate_generator.get_plate_without_sep())
                # print(stringPlaca)

                if stringPlaca.lower() in conteudo:
                    new_line = plate_generator.get_plate() + ' encontrado como: ' + stringPlaca.upper()
                    print(new_line)

                    escrita.write(new_line + '\n')

                plate_generator.increment_plate()

    press_enter_to_continue()


def main_menu():
    while True:
        print("\n- Matrículas Portuguesas -\n")
        print("1. Verificar Matrícula de Veículos")
        print("2. Verificar Matrícula de Reboques")
        print("3. Verificar Matrícula de Carros da GNR")
        print("4. Verificar Matrícula de Motas Até 2006")
        print("5. Verificar Matrícula de Veículos para Exportação")
        print("9. Combinações Matrículas ZZ-00-ZZ")
        print("0. Sair\n")

        option = input("> ")

        if option == "1":
            verificar_matricula_veiculos()
        elif option == "2":
            verificar_matricula_reboques()
        elif option == "3":
            verificar_matricula_carros_gnr()
        elif option == "4":
            verificar_matricula_motas_ate_2006()
        elif option == "5":
            verificar_matricula_veiculos_exportacao()
        elif option == "9":
            combinacoesMatriculas6Letras()
        elif option == "0":
            break
        else:
            print("Opção inválida.")


main_menu()
