# Mission 7 — How computers communicate

## 1. Task / objective
Explain network concepts, describe safe connectivity/DNS observations, and outline what happens when a website opens.

## 2. Work completed
| Concept | Explanation | Example |
|---|---|---|
| LAN | Network covering a small area. | Home network |
| MAN | Network spanning a city or large campus. | City government network |
| WAN | Network spanning large geographic areas. | The Internet |
| DNS | Looks up the address associated with a domain name. | Resolving `example.com` |
| Router | Forwards data between networks. | Home router forwarding traffic to an ISP |
| Protocol | Agreed rules for communication. | HTTPS uses HTTP over TLS |
| Packet switching | Breaks data into packets sent across networks. | Web request/response traffic |
| Client-server | A client requests a service; a server provides it. | Browser requesting a page |

A connectivity test can indicate whether a destination responds over the tested route and protocol; a failed ping alone does not prove a website is down because ICMP may be blocked. A DNS lookup shows returned DNS records such as addresses, which can vary by resolver, time and network. No successful live DNS/connectivity observation is recorded here; run `ping -c 1 example.com` and `nslookup example.com` locally and record only public example-domain results.

### What happens when a website opens
1. The user enters a domain name in a browser, which acts as the client.
2. The browser checks cached information and asks DNS to resolve the name if needed.
3. DNS returns an IP address for an available server.
4. The computer sends packets through its network connection and router toward that server.
5. The client and server establish the needed connection and communicate using protocols such as HTTPS.
6. The server sends a response containing page data and related resources.
7. The browser processes the response and displays the page to the user.

## 3. Commands / tools used
`ping` can test network reachability; `nslookup` can request DNS information. These have not been run successfully in this draft environment.

## 4. My understanding
DNS lets people use names instead of memorizing numeric addresses. Routers forward packets, while protocols define how clients and servers exchange requests and responses. Network failures can occur at different steps, so one test does not explain every failure.

## 5. Difficulties faced
A live DNS lookup could not be confirmed in the current environment.

## 6. How I resolved them
Run the lookup and connectivity test from the computer/network used for the assignment, and record the results without personal IP or Wi-Fi details.

## 7. Evidence / files
This README; add only privacy-safe public-domain lookup observations if required.

## 8. Commit details
Suggested message: `Explain networking concepts and website communication`. Push and verify on GitHub.
