import dns.resolver

def find_subdomains(domain):
    subdomains = []

    # DNS sorgusu yaparak alt alan adlarını tara
    try:
        for subdomain in dns.resolver.resolve(domain, 'CNAME'):
            subdomains.append(subdomain.target.to_text()[:-1])
    except dns.resolver.NXDOMAIN:
        pass

    return subdomains

# Kullanıcıdan web sitesi alan adını al
domain = input("Web sitesi alan adı: ")

# Alt alan adlarını bul
subdomains = find_subdomains(domain)

# Bulunan alt alan adlarını yazdır
for subdomain in subdomains:
    print(subdomain)
