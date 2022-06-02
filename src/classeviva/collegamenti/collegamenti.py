class Collegamenti:
    base: str = "https://web.spaggiari.eu/rest"
    accesso: str = f"{base}/v1/auth/login"
    stato: str = f"{base}/v1/auth/status"
    biglietto: str = f"{base}/v1/auth/ticket"
    documenti: str = f"{base}/v1/students/{{}}/documents"
    controllo_documento: str = f"{base}/v1/students/{{}}/documents/check/{{}}"
    leggi_documento: str = f"{base}/v1/students/{{}}/documents/read/{{}}"
    assenze: str = f"{base}/v1/students/{{}}/absences/details"
    assenze_da: str = f"{base}/v1/students/{{}}/absences/details/{{}}"
    assenze_da_a: str = f"{base}/v1/students/{{}}/absences/details/{{}}/{{}}"
    agenda_da_a: str = f"{base}/v1/students/{{}}/agenda/all/{{}}/{{}}"