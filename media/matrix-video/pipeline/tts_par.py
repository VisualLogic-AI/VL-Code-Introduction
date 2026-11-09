import json, os, asyncio, edge_tts, time
S=json.load(open('script.json')); P=os.environ['HTTPS_PROXY']
jobs=[(f"audio/{s['id']}_{i}.mp3",l['t']) for s in S for i,l in enumerate(s['lines'])]
jobs=[j for j in jobs if not (os.path.exists(j[0]) and os.path.getsize(j[0])>2000)]
print('todo',len(jobs),flush=True); sem=asyncio.Semaphore(6)
async def one(path,text):
    async with sem:
        for k in range(5):
            try:
                t=time.time(); await edge_tts.Communicate(text,"en-US-AndrewNeural",rate="+30%",proxy=P).save(path+'.tmp'); os.replace(path+'.tmp',path); print('ok',path,round(time.time()-t,1),flush=True); return
            except Exception as e: print('retry',path,e,flush=True); await asyncio.sleep(2**k)
async def main(): await asyncio.gather(*[one(*j) for j in jobs])
asyncio.run(main())
