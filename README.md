# 🤖 WhatsApp Automation - Invio Messaggi Automatici GRATIS

- 👋 Hi, I'm @Gamber07
- 👀 I'm interested in computer automatize
- 🌱 I'm currently learning python
- 📫 You can contact me on ig: @giacomo.gamberi

## 📱 Invio di Messaggi WhatsApp Automatici Senza Costi

Questo repository contiene una soluzione **completamente gratuita** per inviare messaggi WhatsApp automatici senza alcun costo. Utilizza WhatsApp Web e librerie Python gratuite.

### ✨ Caratteristiche

- ✅ **Completamente gratuito** - Nessun costo, nessuna API a pagamento
- ✅ **Facile da usare** - Interfaccia semplice e intuitiva
- ✅ **Programmazione messaggi** - Invia messaggi ora o programma per dopo
- ✅ **Gestione contatti** - Salva e gestisci i tuoi contatti
- ✅ **Invio multiplo** - Invia lo stesso messaggio a più persone
- ✅ **Sicuro** - Usa WhatsApp Web, nessun accesso a dati privati

### 🚀 Installazione Rapida

1. **Clona il repository:**
```bash
git clone https://github.com/Gamber07/Gamber07.git
cd Gamber07
```

2. **Installa le dipendenze:**
```bash
pip install -r requirements.txt
```

3. **Inizia a usare:**
```bash
python whatsapp_automation.py
```

### 📖 Come Funziona

Il programma utilizza la libreria `pywhatkit` che automatizza WhatsApp Web:
- Apre WhatsApp Web nel browser
- Accede automaticamente (devi essere già loggato)
- Invia i messaggi che specifichi
- Chiude la finestra (opzionale)

### 🎯 Esempi di Uso

#### Invio Immediato
```python
from whatsapp_automation import WhatsAppAutomation

wa = WhatsAppAutomation()
wa.add_contact("Amico", "+393xxxxxxxxx")
wa.send_to_contact("Amico", "Ciao! Messaggio automatico!")
```

#### Programmazione Messaggio
```python
# Programma per le 15:30
wa.send_to_contact("Amico", "Buon pomeriggio!", scheduled_time=(15, 30))
```

#### Invio Multiplo
```python
contatti = ["Amico1", "Amico2", "Famiglia"]
wa.bulk_send_messages(contatti, "Messaggio per tutti!", delay_between_messages=30)
```

### 🛠️ Configurazione

Il programma crea automaticamente un file `whatsapp_config.json` per salvare:
- I tuoi contatti
- Impostazioni predefinite
- Preferenze di invio

### ⚡ Modalità Interattiva

Esegui il programma per accedere al menu interattivo:

```bash
python whatsapp_automation.py
```

**Opzioni disponibili:**
1. Aggiungi contatto
2. Lista contatti
3. Invia messaggio immediato
4. Programma messaggio
5. Invia a contatto salvato
6. Invio multiplo
7. Rimuovi contatto
8. Esci

### 📝 Esempi Pratici

Esegui gli esempi pre-configurati:

```bash
python examples.py
```

### ⚠️ Requisiti Importanti

1. **WhatsApp Web**: Devi essere loggato su WhatsApp Web
2. **Browser**: Chrome/Chromium installato sul sistema
3. **Numeri di telefono**: Devono includere il prefisso internazionale (+39 per Italia)
4. **Prima esecuzione**: Mantieni il browser aperto durante l'invio

### 🔒 Sicurezza e Privacy

- ✅ Nessun dato viene inviato a servizi terzi
- ✅ I tuoi contatti sono salvati solo localmente
- ✅ Usa l'accesso ufficiale di WhatsApp Web
- ✅ Nessuna violazione dei termini di servizio

### 📋 Formato Numeri di Telefono

**Esempi corretti:**
- Italia: `+393xxxxxxxxx`
- Germania: `+49xxxxxxxxxx`
- Francia: `+33xxxxxxxxx`
- UK: `+44xxxxxxxxxx`

### 🔧 Risoluzione Problemi

**Errore "Browser non trovato":**
```bash
# Su Ubuntu/Debian
sudo apt-get install chromium-browser

# Su macOS
brew install chromium
```

**Errore di timeout:**
- Aumenta il `wait_time` nelle impostazioni
- Assicurati che WhatsApp Web sia già aperto e loggato

**Messaggio non inviato:**
- Verifica il formato del numero di telefono
- Controlla la connessione internet
- Assicurati che il contatto sia su WhatsApp

### 🤝 Contributi

Contributi benvenuti! Sentiti libero di:
- Aprire issue per bug o suggerimenti
- Proporre miglioramenti
- Aggiungere nuove funzionalità

### ⚖️ Disclaimer

Questo strumento è per uso educativo e personale. Rispetta sempre:
- I termini di servizio di WhatsApp
- Le leggi sulla privacy del tuo paese
- Non inviare spam o messaggi non richiesti

### 📞 Supporto

Per domande o supporto:
- Instagram: @giacomo.gamberi
- GitHub Issues: Apri un issue in questo repository

---

**Made with ❤️ by @Gamber07**

<!---
Gamber07/Gamber07 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->