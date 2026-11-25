from fastapi import FastAPI
# 1. creiamo l'applicazione, cioè il server
app = FastAPI()

# 2. quando arriva una richiesta GET all'indirizzo /ping, rispondiamo pong
@app.get("/ping") #decoratore che serve a definire una rotta(route).
def ping():
    return {"risposta": "pong"}

@app.get("/pong")
def pong():
    return {"risposta": "ping"}



# 3. il colpo con GET: la parola arriva nell'indirizzo e il server decide che cosa
rispondere
@app.get("/gioca")
def gioca(parola: str):
if parola == "ping":
return {"risposta": "pong"}
return {"risposta": "Non ho capito: scrivi ping"}