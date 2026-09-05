"""Generate original percussion samples, encoded as MP3 using local ffmpeg.
No third-party audio recordings. Deterministic with seed 808.
"""
import math, random, wave, struct, subprocess
from pathlib import Path
random.seed(808)
out = Path(__file__).resolve().parents[1] / 'assets' / 'audio'
out.mkdir(parents=True, exist_ok=True)
rate = 44100
def render(name, length, fn):
    samples = [fn(i / rate) for i in range(int(length * rate))]
    peak = max(abs(v) for v in samples) or 1
    wav = out / (name + '.wav')
    with wave.open(str(wav), 'wb') as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(rate)
        f.writeframes(b''.join(struct.pack('<h', int(max(-1, min(1, v / peak * .82)) * 32767)) for v in samples))
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(wav),'-codec:a','libmp3lame','-b:a','192k',str(out / (name+'.mp3'))],check=True)
    wav.unlink()
def noise(): return random.uniform(-1, 1)
tau = math.tau
render('kick', .7, lambda t: math.sin(tau*(48*t+100*.025*(1-math.exp(-t/.025))))*math.exp(-t*8)+noise()*.08*math.exp(-t*180))
render('snare', .38, lambda t: (noise()*.75*math.exp(-t*19)+(math.sin(tau*182*t)+math.sin(tau*331*t))*.22*math.exp(-t*28))*(1-math.exp(-t*2500)))
render('clap', .32, lambda t: noise()*(sum(math.exp(-(t-s)*150) if t>=s else 0 for s in [0,.012,.023])*.45+math.exp(-t*18)*.35))
def metal(t): return sum(1 if math.sin(tau*f*t)>0 else -1 for f in [3170,4210,5330,6190,7430,8520])/6
render('hat', .13, lambda t: (metal(t)*.6+noise()*.4)*math.exp(-t*55))
render('openhat', .52, lambda t: (metal(t)*.6+noise()*.4)*math.exp(-t*9)*(1-math.exp(-t*1700)))
render('tom', .5, lambda t: math.sin(tau*(92*t+40*.03*(1-math.exp(-t/.03))))*math.exp(-t*11)+noise()*.035*math.exp(-t*80))
render('rim', .15, lambda t: (math.sin(tau*820*t)*.6+math.sin(tau*1730*t)*.3+noise()*.1)*math.exp(-t*70))
render('cowbell', .35, lambda t: (math.sin(tau*540*t)+math.sin(tau*800*t)*.65)*math.exp(-t*16)*(1-math.exp(-t*1800)))
print('Generated 8 original MP3 samples.')
