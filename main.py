# V tomto souboru jsou definovány funkce, které překládají vstupní text

""" slovník - všechna písmena české abecedy + čisla + zhnaky 
            - odpovídající hodnoty jsou reprezentace daných znaků v morseově abecedě """

morse_Code_dictionary = {
    "A":".-",
    "a":".-",
    "á":".-",
    "Á":".-",
    "B":"-...",
    "b":"-...",
    "C":"-.-.",
    "c":"-.-.",
    "č":"-.-.",
    "Č":"-.-.",
    "D":"-..",
    "d":"-..",
    "ď":"-..",
    "Ď":"-..",
    "E":".",
    "é":".",
    "É":".",
    "Ě":".",
    "ě":".",
    "e":".",
    "F":"..-.",
    "f":"..-.",
    "G":"--.",
    "g":"--.",
    "H":"....",
    "h":"....",
    "Ch":"----",
    "ch":"----",
    "I":"..",
    "i":"..",
    "í":"..",
    "Í":"..",
    "J":".---",
    "j":".---",
    "K":"-.-",
    "k":"-.-",
    "L":".-..",
    "l":".-..",
    "M":"--",
    "m":"--",
    "N":"-.",
    "n":"-.",
    "ň":"-.",
    "Ň":"-.",
    "O":"---",
    "o":"---",
    "ó":"---",
    "Ó":"---",
    "P":".--.",
    "p":".--.",
    "Q":"--.-",
    "q":"--.-",
    "R":".-.",
    "r":".-.",
    "ř":".-.",
    "Ř":".-.",
    "S":"...",
    "s":"...",
    "š":"...",
    "Š":"...",
    "t":"-",
    "T":"-",
    "ť":"-",
    "Ť":"-",
    "U":"..-",
    "u":"..-",
    "ú":"..-",
    "Ú":"..-",
    "Ů":"..-",
    "ů":"..-",
    "V":"...-",
    "v":"...-",
    "W":".--",
    "w":".--",
    "X":"-..-",
    "x":"-..-",
    "Y":"-.--",
    "y":"-.--",
    "ý":"-.--",
    "Ý":"-.--",
    "z":"--..",
    "Z":"--..",
    "ž":"--..",
    "Ž":"--..",
    " ":" ",
    ".":".-.-.-",
    "?":"..--..",
    "!":"--..--",
    ",":"--..--",
    ";":"-.-.-.",
    "/":"-..-.",
    "=":"-...-",
    "-":"-....-",
    "+":".-.-.",
    ")":"-.--.-",
    "(":"-.--.",
    "\"":".-..-",
    ":":"---...",
    "_":"..--.-",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
    }


# Upozornění !!! Písmeno CH je reprezentováno jako dva znaky C a H

def t_funkce(text):   #fukce dostane jako vstup text v češtině a vrací řetězec znaků, který reprezentuje zápis v morseovce
    
    output=""
    first = True    #pomocná proměnná - správně oddělené znaky
    delimiter = ""
    for x in text:
        if x== "\n":
            output = output +"\n"
        elif x in morse_Code_dictionary: #při zadaní znaku, který není ve slovníku se překlad neprovede
            output = output+ delimiter + morse_Code_dictionary[x]
            if first:
               delimiter = "|"
               first = False
    return output



pole =["T","E","M","N","A","I","O","G","K","D","W","R","U","S"," ","O","Q","Z","Y","C","X","B","J","P","A","L","!","F","V","H","0","9",\
    "","8","N","","","7","","(","","","","/","=","6","1","","Á","","","+","","WAIT","2","","","É","3","UNDERSTOOD","4","5","","","","","","","",":","","","",\
    "",".","","","","","",")","","",";","","","","","","","","","-","","","'","","","","@","","","","",".","","",'"',"","","","","_","?"]
#znaky jsou uloženy v poli na odpovídající pozici podle toho, jaké hodnotě odpovídá jejich binární kód => '.'= 1 a '-' = 0


def m_funkce(text):  #tečky a čárky morseovy abecedy jsou kódovány do binárního čísla, který pak odpovídá indexu pozice odpovídajícího znaku v poli
    result=""
    a=1
    for x in text:
        if x=="." or x=="·":
            a=a*2+1
        elif x=="_" or x=="−"or x=="-":
            a*=2
        elif x=="|": #nebo je to poslední znak v textu
            a-=2  #index pole začíná od nuly
            if a<0:
                result =result + " "
                
            else:
                result=result + pole[a]
            a=1
        elif x == "\n":
            result = result + "\n"
        #else když je jiný znak
    return result


