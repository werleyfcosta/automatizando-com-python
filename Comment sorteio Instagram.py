import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(r'C:\Users\corte\Desktop\chromedriver.exe')

driver.get('https://www.instagram.com')
time.sleep(60)
driver.get('''link da publicação do sorteio''')
time.sleep(5)
x = 12
y = 1
z = 0
tempo_all = 0 

while x < 253:
    try:
        list= [
        "@amandamaxima_",
        "@dopradomanuela_of",
        "@maria.nascimento.31",    
        "@moniquericardo_",
        "@pripvc",
        "@rute.b.rocha",
        "@duda_braga122",
        "@souzarol27",
        "@geovane.11malhotmail.com3",
        "@__isabellaofc",
        "@mariiaaraujo7",
        "@ja.zz8086",
        "@este.fany7162",
        "@anarosanasofia",
        "@anaxxds",
        "@kelryvale",
        "@santosjacquelinedejesus",
        "@eloa2447",
        "@will_lopes.7",
        "@maspirozzi",
        "@raquelaraujo17_",
        "@negraveri",
        "@vito.ria4588",
        "@erlane150",
        "@cris_liima",
        "@sd.oliveira16",
        "@luis.sanabria.50702769",
        "@ramon.ribeiro2020",
        "@gaby_oliiver_",
        "@beatriizaraujo2",
        "@annaduarte2910",
        "@kamiladanini",
        "@luanabombom58",
        "@ise_falcao",
        "@sedliana12342020",
        "@mylennahsantos",
        "@juanzinhosantoos",
        "@marilene_ribeiro2016",
        "@lindy_ohanas",
        "@maria_alvexsz",
        "@alvex.sz",
        "@powers_blacks",
        "@anabeatriz_dinizs",
        "@_aishabarbosa",
        "@juan_castro5964",
        "@lucasbe_20",
        "@lehle_alves",
        "@luuh_5ilva",
        "@flavio.ofc15",
        "@brunooalves11",
        "@lucenajuhsilva",
        "@eduardomiranda847",
        "@macoullynlippi",
        "@anasouza.as782",
        "@duda___sillva",
        "@mary13nanber",
        "@fabianosilvah",
        "@daieleassis278",
        "@rosselagoa",
        "@annygabriely200055",
        "@dyegoferreira6",
        "@sarasantana2530",
        "@luanna_mariiaah",
        "@ericamartinsx5",
        "@jheksonlima",
        "@junior.afran.oficial",
        "@joseeduardo12_",
        "@gtgonzalo28",
        "@_maicons",
        "@fab_siilvaa",
        "@_rodrigoyandell",
        "@babizinhapires",
        "@raphaely.ribeiro",
        "@katielydesing",
        "@vansouzamontiel",
        "@grasiele.rodri",
        "@magalhaeskaliane20",
        "@maah_ferreira_314",
        "@dulce_m227",
        "@oxi_francine",
        "@bruninha_nayara07",
        "@bruninha.nayara",
        "@santossilvajunioredvaldo",
        "@brenda_maciels",
        "@gabriellsort",
        "@marya_m.m0717",
        "@samue_lsilvaaoficial",
        "@gabrielamontcarv",
        "@eduarda_landim17",
        "@_talitaa___",
        "@lilia_silva16",
        "@anacarlagastronomia",
        "@santosmariabdo",
        "@oliverdiguim",
        "@matheussilva7781",
        "@milenedemoura",
        "@marianafreitastmt",
        "@eu.juliana.souza",
        "@nataliaalbino88",
        "@sampaiomariaa",
        "@anabiah80",
        "@chamel_cortez",
        "@morenah5252",
        "@juuliaxz1",
        "@tah.santos.2019",
        "@bolao1997",
        "@ariza1209",
        "@suellen_vitooria",
        "@anapaulamacena8",
        "@luizameenezes",
        "@grazielaferreiira",
        "@francielledejsantos",
        "@itsjen00",
        "@angelpopcorna",
        "@juli_a010",
        "@francielle7782",
        "@06.cris",
        "@melissazioto",
        "@daniielagomes_",
        "@amandaf.jara",
        "@gescarvalho96",
        "@maioliveira26",
        "@alicia_goncal",
        "@oliwexxtt",
        "@juliana_alves_90",
        "@sara_layra",
        "@julianascimentx",
        "@laisvitoriat",
        "@nicoly6014",
        "@jdmoura07",
        "@kahboechat",
        "@mamae_do_deyverson",
        "@an.tony_07",
        "@eliane_soaresh",
        "@reuseth",
        "@tgabriele233",
        "@claudiaaaparecida223",
        "@kevencosta27",
        "@biazinha_bella",
        "@lissandraoliveiraslv",
        "@lorranykettl",
        "@anajoyyce2020",
        "@mariasilva56028",
        "@tn_brazz",
        "@calucioonunes",
        "@mmichaelle016",
        "@opaulac",
        "@mello_jheny",
        "@gabriela_a_silva",
        "@carlaazevedorslh",
        "@jonathanimperiio",
        "@lea.s.nascimento",
        "@kelivane_carvalho",
        "@freire8557",
        "@andre9fe118",
        "@betinha3456l",
        "@schrerika",
        "@mah_santos68",
        "@danisouza3217",
        "@adrianacosta202",
        "@jeferson_santos_b",
        "@heitoraugustodamas",
        "@ka_evelyn14",
        "@miguelwill724",
        "@allananjos760",
        "@guilhermeemk",
        "@ely___albuquerque",
        "@kerolynsd",
        "@layanemarcia090",
        "@yasm.im1814",
        "@vanessamaria____",
        "@bheatriixz",
        "@steffaany_",
        "@nanypatu",
        "@_xx.mts.xx_",
        "@essa_moto_e_minha",
        "@_brenda_off",
        "@paulovieira88",
        "@clei.tonalves",
        "@morenah_santos",
        "@_nandaraphael",
        "@deizyelle_borges",
        "@re_monteir",
        "@marcelomachado119",
        "@dudasilvamac_",
        "@karolvitoria911",
        "@tamirescrisss",
        "@andeezzapriscylla",
        "@macia.regis",
        "@miladudafernandes",
        "@_nicoly.ferreira",
        "@anaalves.2006",
        "@onlyalef",
        "@1234133m",
        "@janaenymariano",
        "@_gabii_smoreira",
        "@rainaraaztg5489",
        "@railtonlive",
        "@belly_kayanne",
        "@elaynes0uza18",
        "@leo_soares.22",
        "@thaimsantosx",
        "@j.caico",
        "@luanjesusdantas",
        "@luizfeliperibeirodossan",
        "@kevinwil_",
        "@annaaraujo311",
        "@_brunabarcelosfernandes",
        "@mariduartts",
        "@marlon_maciel__",
        "@tatah_olivera34",
        "@_sry_lohanyxx",
        "@danny.batalha",
        "@duda_soares059",
        "@nathy__silv_",
        "@barbaraxguilherme",
        "@guilhermesilva6812",
        "@murilobeluci",
        "@lorenarangel165",
        "@geehvenanciofc",
        "@vitor_rodrigues2020",
        "@patricia_netta03",
        "@gabrielianni",
        "@heltonjohnatas",
        "@babiffonseca_",
        "@rayelesiilva",
        "@eduardafeliciano66",
        "@pelegrineli.ju",
        "@jhe_souza123",
        "@dixx.dafiny18",
        "@rafaelavieira.a",
        "@jana_24.04",
        "@mariana9878_",
        "@emille_ananda",
        "@nalimsantana",
        "@biapereira164",
        "@paulaaoliveira._",
        "@vieiraaa_k",
        "@alanda_almeida24",
        "@thaissampaiop",
        "@eueel_es",
        "@bruh.curcio",
        "@franciellyap08",
        "@larissasantos5461",
        "@heeyagnes",
        "@cris_macedo19",
        "@brenda_chavees",
        "@sabrinam_melo",
        "@cris.fatima",
        "@luizavaladares225",
        "@eliaanee_soares",
        "@analu_tgv",
        "@tatisantos943"
        ]
        
        list1 = [62, 64, 68, 70, 75, 73, 80, 72, 81, 85, 65, 90, 83, 78, 92]
        list2 = [10, 12, 14, 15, 23, 27, 18, 21, 35, 25, 16, 13]
        
        
        sorteio_coment = random.choice(list1)
        sorteio_post = random.choice(list2)
        
        
        sorteio_c = int(sorteio_coment)
        sorteio_p = int(sorteio_post)
        
        print('Tempo do comentário: %s' %(sorteio_c))
        print('Tempo de envio do comentário: %s' %(sorteio_p))
        
        site = str(list[x])
        site1 = str(list[y])
        
        
        time.sleep(sorteio_c)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys('Eu quero %s %s' %(site, site1))
        
        time.sleep(sorteio_p)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()
                                        
        if y < 252:
            y += 1
        elif x <= 253:
            x += 1
            y = 0
        z += 1
        
        tempo_all += sorteio_c + sorteio_p
        print('Tempo total de execução até agora %s segundos em %s vezes' %(tempo_all, z))
        print("|______________________________________________________________|")
        
    except:
        print('tá dando errado')
        
        time.sleep(sorteio_c)
        driver.get('''link da publicação do sorteio''')
        
        tempo_all += sorteio_c + sorteio_p
        pass

    
    