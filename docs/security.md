## Security

1. What is directory traversal?

- Directory traversal (also known as file path traversal) is a web security vulnerability that allows an attacker to read arbitrary files on the server that is running an application. 
- This might include application code and data, credentials for back-end systems, and sensitive operating system files. 
- In some cases, an attacker might be able to write to arbitrary files on the server, allowing them to modify application data or behavior, and ultimately take full control of the server.

2. What is cross-site scripting (XSS)?

- Cross-site scripting (also known as XSS) is a web security vulnerability that allows an attacker to compromise the interactions that users have with a vulnerable application. 
- It allows an attacker to circumvent the same origin policy, which is designed to segregate different websites from each other. 
- Cross-site scripting vulnerabilities normally allow an attacker to masquerade as a victim user, to carry out any actions that the user is able to perform, and to access any of the user's data. 
- If the victim user has privileged access within the application, then the attacker might be able to gain full control over all of the application's functionality and data.

3. How does XSS work?

- Cross-site scripting works by manipulating a vulnerable web site so that it returns malicious JavaScript to users. 
- When the malicious code executes inside a victim's browser, the attacker can fully compromise their interaction with the application.

4. What is SQL injection (SQLi)?

- SQL injection is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. 
- It generally allows an attacker to view data that they are not normally able to retrieve. This might include data belonging to other users, or any other data that the application itself is able to access. 
- In many cases, an attacker can modify or delete this data, causing persistent changes to the application's content or behavior.
- In some situations, an attacker can escalate an SQL injection attack to compromise the underlying server or other back-end infrastructure, or perform a denial-of-service attack.

5. What is CSRF?

- Cross-site request forgery (also known as CSRF) is a web security vulnerability that allows an attacker to induce users to perform actions that they do not intend to perform. 
- It allows an attacker to partly circumvent the same origin policy, which is designed to prevent different websites from interfering with each other.

## OWASP Top 10 2017

A1:2017 - Injection 
A2:2017 - Broken Authentication
A3:2017 - Sensitive Data Exposure 
A4:2017 - XML External Entities (XXE)
A5:2017 - Broken Access Control
A6:2017 - Security Misconfiguration
A7:2017 - Cross-Site Scripting (XSS)
A8:2017 - Insecure Deserialization
A9:2017 - Using Components with Known Vulnerabilities 
A10:2017 - Insufficient Logging & Monitoring