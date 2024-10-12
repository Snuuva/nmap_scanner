import nmap
import datetime

def perform_scan(ip, scan_type):
    nm = nmap.PortScanner()  # Återinitiera Nmap-skanner varje gång annars visar den bara resultat första scanningen

    if scan_type == '1':  # Snabb skanning
        print(f"Utför snabb skanning på {ip}...")
        nm.scan(ip, arguments='-sV')
    elif scan_type == '2':  # Långsam skanning (alla portar)
        print(f"Utför långsam skanning på {ip} (alla portar)...")
        nm.scan(ip, arguments='-p- -sV')
    elif scan_type == '3':  # Snabb skanning med scripts
        print(f"Utför snabb skanning med scripts på {ip}...")
        nm.scan(ip, arguments='-sC -sV')
    elif scan_type == '4':  # Långsam skanning med scripts
        print(f"Utför långsam skanning med scripts på {ip}...")
        nm.scan(ip, arguments='-p- -sC -sV')
    
    return nm

def format_scan_results(nm, ip):
    # Kontrollera om det finns resultat för IP-adressen
    if ip not in nm.all_hosts():
        return "Inga resultat hittades för denna IP."

    result = []
    result.append(f"\nSkanningsresultat för {ip}:")

    for proto in nm[ip].all_protocols():
        result.append(f"\nProtokoll: {proto}")
        lport = nm[ip][proto].keys()
        
        for port in sorted(lport):
            state = nm[ip][proto][port]['state']
            name = nm[ip][proto][port].get('name', 'okänd tjänst')
            version = nm[ip][proto][port].get('version', 'ingen version')
            product = nm[ip][proto][port].get('product', '')
            extrainfo = nm[ip][proto][port].get('extrainfo', '')
            
            # Resultat per port
            result.append(f"  Port: {port} | Status: {state} | Tjänst: {name} | Version: {version} {product} {extrainfo}")

    return "\n".join(result)

def save_to_file(scan_result):
    # Namn baserat på datum och tid
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"nmap_scan_{timestamp}.txt"
    
    with open(filename, 'w') as file:
        file.write(scan_result)
    print(f"Resultatet har sparats till {filename}")

def main():
    while True:
        print("Välkommen till Nmap-skanner!")
        ip = input("Ange IP-adressen du vill skanna (eller 'exit' för att avsluta): ")
        
        if ip.lower() == 'exit':
            print("Avslutar programmet.")
            break
        
        # Kontrollera om IP-adressen är intern eller extern
        first_octet = int(ip.split('.')[0])
        if (first_octet == 10) or (first_octet == 172 and 16 <= int(ip.split('.')[1]) <= 31) or (first_octet == 192 and ip.split('.')[1] == '168'):
            print("Detta är en intern IP-adress.")
        else:
            print("Detta är en extern IP-adress. Kom ihåg att skanningar på externa nätverk måste vara lagliga.")
            # Fråga om användaren vill fortsätta
            continue_choice = input("Vill du fortsätta med att skanna den här externa IP-adressen? (ja/nej): ").lower()
            if continue_choice == 'nej':
                print("Återgår till att ange en ny IP-adress...")
                continue  # Gå tillbaka till att ange en ny IP
        
        while True:
            # Skanningsalternativ
            print("\nVälj vilken typ av skanning du vill utföra:")
            print("1. Snabb skanning (-sV)")
            print("2. Långsam skanning (alla portar) (-p- -sV)")
            print("3. Snabb skanning med scripts (-sC -sV)")
            print("4. Långsam skanning med scripts (alla portar) (-p- -sC -sV)")
            print("5. Avsluta")
            
            scan_choice = input("Ange ditt val (1-5): ")
            
            if scan_choice == '5':
                print("Avslutar programmet.")
                return
            
            if scan_choice in ['1', '2', '3', '4']:
                # Utför skanningen
                nm = perform_scan(ip, scan_choice)
                
                # Skanningsresultatet
                scan_result = format_scan_results(nm, ip)
                
                # Visa resultatet i terminalen
                print("\n--- Skanningsresultat ---")
                print(scan_result)
                
                # Fråga om att spara till fil
                save_choice = input("\nVill du spara resultatet till en textfil? (ja/nej): ").lower()
                if save_choice == 'ja':
                    save_to_file(scan_result)
                
                # Fråga om att göra en ny skanning
                again_choice = input("\nVill du göra en ny skanning på samma IP? (ja/nej): ").lower()
                if again_choice == 'nej':
                    break  # Gå tillbaka till att ange en ny IP
            else:
                print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main()
