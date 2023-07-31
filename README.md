# pac-parser
proxy auto configuration script validator

Ideas:
**Functionality:**

1. Input PAC script box with lines (maybe looks like VS code?)

2. URL box for full urls including the “https://”

3. Host box for hostnames like “[example.com](http://example.com/)”

4. Your IP box (should take IP from whatsmyip if left blank)

5. Errors should be clear if there are any syntax errors

6. Should clearly read URL/HOST X is being sent DIRECT or PROXIED to X and why (line number)

7. All JavaScript functions used in PAC should be listed underneath with TRUE or FALSE if called
8. Not called functions can be left blank
9. Advanced button would reveal all the rest of the lines in the script:
Line, Rule name, result = true/false
10. Dark mode light mode? 

- FindProxyForURL(url, host): The main function that is called by the web browser to determine the proxy server for a given URL.
- isPlainHostName(host): Returns true if the host does not contain a domain.
- dnsDomainIs(host, domain): Returns true if the domain of the host matches exactly with the provided domain.
- localHostOrDomainIs(host, hostdom): Returns true if the hostname matches exactly with either the hostname or domain name of the host.
- isResolvable(host): Returns true if the hostname can be resolved to an IP address.
- isInNet(host, pattern, mask): Returns true if the IP address of the host matches exactly with the specified IP address pattern and mask.
- dnsResolve(host): Resolves the hostname into an IP address.
- myIpAddress(): Returns the IP address of the machine that the script is running on.
- dnsDomainLevels(host): Returns the number of DNS domain levels (the number of dots) in the hostname.
- shExpMatch(str, shexp): Returns true if the string matches the specified shell expression.
- weekdayRange(wd1, wd2, gmt): Checks whether the current date is within the range of specified weekdays. It returns true if the current date is within the range. The gmt argument is optional and specifies that the time zone is GMT.
- dateRange(...args): Checks whether the current date is within the specified range. The arguments can be day, month, year (integer or string), and the optional GMT timezone.
- timeRange(...args): Checks whether the current time is within the specified range. The arguments can be hour, minute, second, and the optional GMT timezone.
