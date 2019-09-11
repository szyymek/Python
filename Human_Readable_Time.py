def make_readable(seconds):
    hh=0
    mm=0
    ss=0
    minuty=int(seconds/60)
    if minuty>0:
        godziny=int(minuty/60)
        if godziny>0:
            hh=godziny
            mm=minuty%60
            ss=seconds%60
        else:
            mm=minuty
            ss=seconds%60
    else:
        ss=seconds
        
    if ss>9:
        sekundy=str(ss)
    else:
        sekundy="0"+str(ss)
        
    if mm>9:
        minuty=str(mm)
    else:
        minuty="0"+str(mm)
        
    if hh>9:
        godziny=str(hh)
    else:
        godziny="0"+str(hh)
    
    return godziny+":"+minuty+":"+sekundy
