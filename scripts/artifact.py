# -*- coding: utf-8 -*-
"""
Created on Sun May 16 17:39:27 2021

@author: Seo
"""

class Artifact:
    def __init__(self,
                 mainhpraw=None, mainatkraw=None, mainhpperc=None, mainatkperc=None,
                 maindefperc=None, mainer=None, mainem=None,
                 maincritrate=None, maincritdmg=None, mainhealing=None,
                 maincryo=None, mainanemo=None, maingeo=None,
                 mainpyro=None, mainhydro=None, mainelec=None, mainphys=None,
                 atkraw=None, atkperc=None, hpraw=None, hpperc=None,
                 critrate=None, critdmg=None, em=None, er=None,
                 defraw=None, defperc=None):
        
        # Main stats which may clash
        self.mainhpraw = mainhpraw
        self.mainatkraw = mainatkraw
        self.mainhpperc = mainhpperc
        self.mainatkperc = mainatkperc
        self.maindefperc = maindefperc
        self.mainer = mainer
        self.mainem = mainem
        self.maincritrate = maincritrate
        self.maincritdmg = maincritdmg
        
        # Main stats which cannot clash
        self.mainhealing = mainhealing
        self.maincryo = maincryo
        self.mainanemo = mainanemo
        self.maingeo = maingeo
        self.mainpyro = mainpyro
        self.mainhydro = mainhydro
        self.mainelec = mainelec
        self.mainphys = mainphys
        
        # Sub stats
        self.atkraw = atkraw
        self.atkperc = atkperc
        self.hpraw = hpraw
        self.hpperc = hpperc
        self.critrate = critrate
        self.critdmg = critdmg
        self.em = em
        self.er = er
        self.defraw = defraw
        self.defperc = defperc
        
        # Check only up to 1 main stat
        self.mainstatlist = [self.mainhpraw, self.mainatkraw, self.mainhpperc, self.mainatkperc,
                        self.maindefperc, self.mainer, self.mainem, self.maincritrate,
                        self.maincritdmg, self.mainhealing, self.maincryo,
                        self.mainanemo, self.maingeo, self.mainpyro,
                        self.mainhydro, self.mainelec, self.mainphys]
        self.mainstatstrs = ['HP', 'ATK', 'HP%', 'ATK%',
                            'DEF%', 'Energy Recharge', 'Elemental Mastery', 'CRIT Rate%',
                            'CRIT DMG%', 'Healing Bonus%', 'Cryo DMG Bonus%',
                            'Anemo DMG Bonus%', 'Geo DMG Bonus%', 'Pyro DMG Bonus%',
                            'Hydro DMG Bonus%', 'Electro DMG Bonus%', 'Physical DMG Bonus%']
        if len(self.mainstatlist) - self.mainstatlist.count(None) > 1:
            raise ValueError("Cannot have more than 1 main stat.")
        elif self.mainstatlist.count(None) == len(self.mainstatlist):
            raise ValueError("Must have at least 1 main stat.")
        
    
        # Check only up to 4 substats
        self.substatlist = [self.atkraw, self.atkperc, self.hpraw, self.hpperc,
                       self.critrate, self.critdmg, self.em, self.er,
                       self.defraw, self.defperc]
        if len(self.substatlist) - self.substatlist.count(None) > 4:
            raise ValueError("Cannot have more than 4 substats.")

        # Check no substat-mainstat clashes
        if self.mainhpraw is not None and self.hpraw is not None:
            raise ValueError("Cannot have both main/sub stats as HP.")
        if self.mainatkraw is not None and self.atkraw is not None:
            raise ValueError("Cannot have both main/sub stats as ATK.")
        if self.mainhpperc is not None and self.hpperc is not None:
            raise ValueError("Cannot have both main/sub stats as HP%.")
        if self.mainatkperc is not None and self.atkperc is not None:
            raise ValueError("Cannot have both main/sub stats as ATK%.")
        if self.maindefperc is not None and self.defperc is not None:
            raise ValueError("Cannot have both main/sub stats as DEF%.")
        if self.mainer is not None and self.er is not None:
            raise ValueError("Cannot have both main/sub stats as Energy Recharge.")
        if self.mainem is not None and self.em is not None:
            raise ValueError("Cannot have both main/sub stats as Elemental Mastery.")
        if self.maincritrate is not None and self.critrate is not None:
            raise ValueError("Cannot have both main/sub stats as CRIT Rate%.")
        if self.maincritdmg is not None and self.critdmg is not None:
            raise ValueError("Cannot have both main/sub stats as CRIT DMG%.")

    @classmethod
    def fromDictionary(cls, d):
        # Unpack dictionary for each stat if it exists
        mainhpraw = d['mainhpraw'] if 'mainhpraw' in d.keys() else None
        mainatkraw = d['mainatkraw'] if 'mainatkraw' in d.keys() else None
        mainhpperc = d['mainhpperc'] if 'mainhpperc' in d.keys() else None
        mainatkperc = d['mainatkperc'] if 'mainatkperc' in d.keys() else None
        maindefperc = d['maindefperc'] if 'maindefperc' in d.keys() else None
        mainer = d['mainer'] if 'mainer' in d.keys() else None
        mainem = d['mainem'] if 'mainem' in d.keys() else None
        maincritrate = d['maincritrate'] if 'maincritrate' in d.keys() else None
        maincritdmg = d['maincritdmg'] if 'maincritdmg' in d.keys() else None
        
        mainhealing = d['mainhealing'] if 'mainhealing' in d.keys() else None
        maincryo = d['maincryo'] if 'maincryo' in d.keys() else None
        mainanemo = d['mainanemo'] if 'mainanemo' in d.keys() else None
        maingeo = d['maingeo'] if 'maingeo' in d.keys() else None
        mainpyro = d['mainpyro'] if 'mainpyro' in d.keys() else None
        mainhydro = d['mainhydro'] if 'mainhydro' in d.keys() else None
        mainelec = d['mainelec'] if 'mainelec' in d.keys() else None
        mainphys = d['mainphys'] if 'mainphys' in d.keys() else None
        
        atkraw = d['atkraw'] if 'atkraw' in d.keys() else None
        atkperc = d['atkperc'] if 'atkperc' in d.keys() else None
        hpraw = d['hpraw'] if 'hpraw' in d.keys() else None
        hpperc = d['hpperc'] if 'hpperc' in d.keys() else None
        critrate = d['critrate'] if 'critrate' in d.keys() else None
        critdmg = d['critdmg'] if 'critdmg' in d.keys() else None
        em = d['em'] if 'em' in d.keys() else None
        er = d['er'] if 'er' in d.keys() else None
        defraw = d['defraw'] if 'defraw' in d.keys() else None
        defperc = d['defperc'] if 'defperc' in d.keys() else None
        
        # note, it is important to leave this as positional keywords i.e.
        # do not simply leave each arg as XX, but rather XX=XX. this maintains
        # the classmethod for the derived classes as they use keyword forwarding
        return cls(mainhpraw=mainhpraw, mainatkraw=mainatkraw, mainhpperc=mainhpperc, mainatkperc=mainatkperc,
                    maindefperc=maindefperc, mainer=mainer, mainem=mainem,
                    maincritrate=maincritrate, maincritdmg=maincritdmg, mainhealing=mainhealing,
                    maincryo=maincryo, mainanemo=mainanemo, maingeo=maingeo,
                    mainpyro=mainpyro, mainhydro=mainhydro, mainelec=mainelec, mainphys=mainphys,
                    atkraw=atkraw, atkperc=atkperc, hpraw=hpraw, hpperc=hpperc,
                    critrate=critrate, critdmg=critdmg, em=em, er=er,
                    defraw=defraw, defperc=defperc)
        

    def print(self):
        idx = [i for i, val in enumerate(self.mainstatlist) if val != None][0]
        # pretty printing based on if its % => move to end of string
        if self.mainstatstrs[idx][-1] == '%':
            self.mainstatstr = '(Main) %s +%.1f%%' % (self.mainstatstrs[idx][:-1], self.mainstatlist[idx])
        else:
            self.mainstatstr = '(Main) %s +%.1f' % (self.mainstatstrs[idx], self.mainstatlist[idx])
        print(self.mainstatstr)
        
        # substat printing
        if self.atkraw is not None:
            print("ATK+%d" % self.atkraw)
        if self.atkperc is not None:
            print("ATK+%.1f%%" % self.atkperc)
        if self.hpraw is not None:
            print("HP+%d" % self.hpraw)
        if self.hpperc is not None:
            print("HP+%.1f%%" % self.hpperc)
        if self.critrate is not None:
            print("CRIT Rate+%.1f%%" % self.critrate)
        if self.critdmg is not None:
            print("CRIT DMG+%.1f%%" % self.critdmg)
        if self.em is not None:
            print("Elemental Mastery+%d" % self.em)
        if self.er is not None:
            print("Energy Recharge+%.1f%%" % self.er)
        if self.defraw is not None:
            print("DEF+%d" % self.defraw)
        if self.defperc is not None:
            print("DEF+%.1f%%" % self.defperc)
            
            