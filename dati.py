from asyncio import run_coroutine_threadsafe


def ierakstit(teksts):
    fails = open("teksts.txt", "w", encoding="utf-8") # r - read; w - write; a - append
    fails.write(teksts+"\n")
    fails.close()
return

ierakstit("Mani sauc Andruss")

def pierakstit_klat(teksts):
    fails = open("teksts.txt", "a", endcoding="utf-8")
    fails.write(teksts)
    fails.close()
return

# pierakstit_klat("Es esmu skolnieks")

def nolasit_visu():
    fails = open("teksts.txt", "r", encoding="utf-8")
    teksts = fails.read()
   return teksts

# print(nolasit_visu())

def dabut_rindinas():
    fails = open("teksts.txt", "r", encoding="utf-8")
    rindas = fails.readlines()
    for i in range(len(rindas)):
        rindas[i] = rindas[i].strip()
    return rindas

# saraksts = dabut_rindas()
# print(saraksts)

for rinda in saraksts:
    rinda = rinda.strip("\n")