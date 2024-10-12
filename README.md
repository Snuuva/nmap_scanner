# Nmap Skanner

Den här applikationen är ett enkelt gränssnitt för att utföra olika typer av nätverksskanningar med hjälp av Nmap. Programmet stöder flera skanningsalternativ som snabb skanning, långsam skanning av alla portar samt skanningar med Nmap-skript.

## Funktioner

- **Snabb skanning (-sV)**: Skannar snabbt och identifierar tjänster och deras versioner.
- **Långsam skanning av alla portar (-p- -sV)**: Skannar alla portar och identifierar tjänster och deras versioner.
- **Snabb skanning med scripts (-sC -sV)**: Kör Nmap-skript för att samla in ytterligare information under en snabb skanning.
- **Långsam skanning med scripts (-p- -sC -sV)**: Skannar alla portar och kör Nmap-skript för djupare analys.

## Användning

1. Klona eller ladda ner detta repo.
2. Installera beroenden genom att köra följande kommando:
    ```bash
    pip install -r requirements.txt
    ```
3. Kör skriptet med:
    ```bash
    python3 nmap_scanner.py
    ```
4. Ange den IP-adress du vill skanna och välj skanningstyp.

## Skanningstyper

1. **Snabb skanning (-sV)** - Skannar de vanligaste portarna.
2. **Långsam skanning (-p- -sV)** - Skannar alla portar på det angivna målet.
3. **Snabb skanning med scripts (-sC -sV)** - Utför en snabb skanning med Nmap-skript.
4. **Långsam skanning med scripts (-p- -sC -sV)** - Skannar alla portar med tillämpning av Nmap-skript.

### Spara resultat

Efter varje skanning kan användaren välja att spara resultaten i en textfil. Filnamnet baseras på aktuell tid och datum.

## OBS!

Skanningar på externa nätverk måste vara lagliga. Se till att du har tillåtelse innan du skannar externa IP-adresser.

## Exempel

Vid körning kommer programmet att fråga efter IP-adress och skanningstyp:

```plaintext
Välkommen till Nmap-skanner!
Ange IP-adressen du vill skanna (eller 'exit' för att avsluta): 192.168.1.1
Detta är en intern IP-adress.

Välj vilken typ av skanning du vill utföra:
1. Snabb skanning (-sV)
2. Långsam skanning (alla portar) (-p- -sV)
3. Snabb skanning med scripts (-sC -sV)
4. Långsam skanning med scripts (alla portar) (-p- -sC -sV)
5. Avsluta
